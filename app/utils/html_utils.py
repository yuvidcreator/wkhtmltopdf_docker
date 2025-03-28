import os
import json
import subprocess




# Utility: Generate PDF using wkhtmltopdf
def generate_pdf(order_id: str, json_data: dict, charts_path: str):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Arial'; }}
            .page-break {{ page-break-before: always; }}
        </style>
    </head>
    <body>
        <h1>Report: {order_id}</h1>
        <h2>Data Analysis</h2>
        <pre>{json.dumps(json_data, indent=4)}</pre>
        <div class='page-break'></div>
        <h2>Charts</h2>
    """
    
    for chart in os.listdir(charts_path):
        html_content += f'<img src="{charts_path}/{chart}" style="width:100%;"><div class="page-break"></div>'
    
    html_content += "</body></html>"
    html_file = f"templates/{order_id}.html"
    pdf_file = f"output/{order_id}.pdf"
    
    os.makedirs("output", exist_ok=True)
    with open(html_file, "w") as file:
        file.write(html_content)
    
    subprocess.run(["wkhtmltopdf", html_file, pdf_file])
    return pdf_file


