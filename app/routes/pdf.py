import uuid
# from main import app as route
from fastapi import UploadFile, BackgroundTasks, HTTPException, APIRouter
from app.db import SessionLocal
from app.utils.pdf_utils import save_uploaded_file
from app.models import ProcessTable
from app.utils.tasks import process_report_task



route = APIRouter()



# API: Upload Excel and Request PDF Generation
@route.post("/upload-excel/")
def upload_excel(file: UploadFile, background_tasks: BackgroundTasks):
    order_id = str(uuid.uuid4())
    file_path = save_uploaded_file(file)
    
    db = SessionLocal()
    db.add(ProcessTable(order_id=order_id, status="pending"))
    db.commit()
    db.close()
    # task = process_report_task.apply_async(args=[order_id, file_path])
    background_tasks.add_task(process_report_task, order_id, file_path)
    return {"order_id": order_id, "status": "processing"}


# API: Get PDF Status
@route.get("/status/{order_id}")
def get_status(order_id: str):
    db = SessionLocal()
    request = db.query(ProcessTable).filter(ProcessTable.order_id == order_id).first()
    db.close()
    if not request:
        raise HTTPException(status_code=404, detail="Order ID not found")
    return {"order_id": order_id, "status": request.status, "file_path": request.file_path}


# API: Download PDF
@route.get("/download/{order_id}")
def download_pdf(order_id: str):
    db = SessionLocal()
    request = db.query(ProcessTable).filter(ProcessTable.order_id == order_id).first()
    db.close()
    if not request or not request.file_path:
        raise HTTPException(status_code=404, detail="PDF not found")
    return {"file_url": request.file_path}
