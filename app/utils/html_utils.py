import os
import json
import subprocess


# config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

# Utility: Generate PDF using wkhtmltopdf
def generate_pdf(order_id: str, json_data: dict, charts_path: str):
    print("Generating PDF --> JSON Data --> ", json_data)
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

    options = {
        "quiet": "",
        "enable-local-file-access": "",  # ✅ Allows local file access
        "page-size": "A4",
        "dpi": 300
    }
    
    for chart in os.listdir(charts_path):
        print(chart[1])
        html_content += f'<img src="{charts_path}{chart}" style="width:100%;"><div class="page-break"></div>'
        # html_content += f'<img src="{charts_path}{chart.replace("/","")}" style="width:100%;"><div class="page-break"></div>'

    html_content += "</body></html>"
    html_file = f"templates/{order_id}.html"
    # os.path.abspath
    pdf_file = f"output/{order_id}.pdf"
    
    os.makedirs("output", exist_ok=True)
    
    try:
        with open(html_file, "w") as file:
            file.write(html_content)
        subprocess.run(["wkhtmltopdf", html_file, pdf_file, options])
        return pdf_file
    except Exception as e:
        print(f"Error ----->  {e}")
        # return f"{e}"
        return None


