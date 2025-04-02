import os
import uuid
import shutil
from fastapi import UploadFile, File
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# from dotenv import load_dotenv

# load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")


# Utility: Save Uploaded File
def save_uploaded_file(uploaded_file: UploadFile, order_id: str) -> str:
    file_location = f"uploads/{order_id}_{uploaded_file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    # files_abs_path = os.path.abspath(file_location)
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
    print("In Generate Charts Func ----> ", data.items())
    for name, value in data.items():
        plt.figure()
        plt.bar(value.keys(), value.values())
        plt.title(f"Analysis for {name}")
        chart_path = f"charts/{order_id}/{name}.png"
        plt.savefig(chart_path)
        plt.close()
    return f"charts/{order_id}/"


# def generate_charts(data: dict, order_id: str):
#     """Generate and save a doughnut chart from Excel data."""
#     os.makedirs(f"charts/{order_id}", exist_ok=True)
#     filename=f"charts/{order_id}/chart.webp"
#     if not data:
#         raise ValueError("No data available for chart generation.")

#     labels = list(data.keys())
#     sizes = list(data.values())

#     matplotlib.use('agg')
#     fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
#     wedges, texts, autotexts = ax.pie(
#         sizes, labels=labels, autopct="%1.1f%%", startangle=90,
#         wedgeprops={"linewidth": 2, "edgecolor": "white"},
#         pctdistance=0.85
#     )

#     for text in autotexts:
#         text.set_color("white")

#     ax.set_facecolor("white")
#     ax.axis("equal")

#     plt.savefig(filename, format="webp", pil_kwargs={"lossless": False})
#     plt.close()

#     # files_abs_path = os.path.abspath(filename)
#     # print(files_abs_path)
#     # return files_abs_path
#     return f"charts/{order_id}/"