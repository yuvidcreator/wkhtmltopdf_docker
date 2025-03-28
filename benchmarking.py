import time
import requests
import json

# Define test files and API endpoints
wkhtmltopdf_url = "http://localhost:8000/upload-excel/"
weasyprint_url = "http://localhost:8001/upload-excel/"
test_file_path = "test_data/large_excel.xlsx"



def upload_and_track(api_url):
    with open(test_file_path, "rb") as file:
        response = requests.post(api_url, files={"file": file})
        if response.status_code == 200:
            order_id = response.json()["order_id"]
            print(f"Order ID: {order_id} submitted for {api_url}")
        else:
            print(f"Failed to submit file to {api_url}: {response.text}")
            return None
    
    # Track the processing time
    start_time = time.time()
    status_url = api_url.replace("upload-excel/", f"status/{order_id}")
    while True:
        status_response = requests.get(status_url).json()
        if status_response["status"] == "completed":
            break
        elif status_response["status"] == "failed":
            print(f"Processing failed for {api_url}")
            return None
        time.sleep(5)  # Poll every 5 seconds
    
    end_time = time.time()
    print(f"PDF generation completed in {end_time - start_time:.2f} seconds for {api_url}")
    return end_time - start_time

# Run Benchmark
times = {}
times["wkhtmltopdf"] = upload_and_track(wkhtmltopdf_url)
# times["weasyprint"] = upload_and_track(weasyprint_url)

print("Benchmark Results:", json.dumps(times, indent=4))
