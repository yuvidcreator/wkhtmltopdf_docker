import os
import uuid
import shutil
from fastapi import UploadFile
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# from dotenv import load_dotenv

# load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")


# Utility: Save Uploaded File
def save_uploaded_file(uploaded_file: UploadFile) -> str:
    file_location = f"uploads/{uuid.uuid4()}_{uploaded_file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return file_location

# Utility: Process Excel Data
def process_excel(file_path: str) -> dict:
    df = pd.read_excel(file_path)
    analysis = df.describe().to_dict()
    return analysis

# Utility: Generate Charts
def generate_charts(data: dict, order_id: str):
    os.makedirs(f"charts/{order_id}", exist_ok=True)
    matplotlib.use('agg')
    for name, value in data.items():
        plt.figure()
        plt.bar(value.keys(), value.values())
        plt.title(f"Analysis for {name}")
        chart_path = f"charts/{order_id}/{name}.png"
        plt.savefig(chart_path)
        plt.close()
    return f"charts/{order_id}/"
