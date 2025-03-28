from app.models import ProcessTable
from app.utils.pdf_utils import generate_charts, process_excel
from app.utils.html_utils import generate_pdf
from worker import celery_app

# Celery Task
from app.db import SessionLocal

@celery_app.task(bind=True)
def process_report_task(self, order_id: str, file_path: str):
    db = SessionLocal()
    try:
        db.query(ProcessTable).filter(ProcessTable.order_id == order_id).update({"status": "processing"})
        db.commit()
        
        data = process_excel(file_path)
        charts_path = generate_charts(data, order_id)
        pdf_path = generate_pdf(order_id, data, charts_path)
        
        db.query(ProcessTable).filter(ProcessTable.order_id == order_id).update({"status": "completed", "file_path": pdf_path})
        db.commit()
    except Exception as e:
        db.query(ProcessTable).filter(ProcessTable.order_id == order_id).update({"status": "failed"})
        db.commit()
        print(str(e))
    finally:
        db.close()