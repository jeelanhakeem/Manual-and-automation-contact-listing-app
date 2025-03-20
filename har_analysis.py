import time
import json
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 🔹 Update this path to the extracted browsermob-proxy location
BROWSER_MOB_PATH = r"C:\Users\HMD Jeelan\Downloads\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
# Start the BrowserMob Proxy server
server = Server(BROWSER_MOB_PATH)
server.start()
proxy = server.create_proxy()

# Configure Chrome options to use the proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy.proxy}")

# Start Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Enable HAR capture
proxy.new_har("exactspace", options={'captureHeaders': True, 'captureContent': True})

# Navigate to the website
driver.get("https://exactspace.co/")
time.sleep(5)  # Allow time for network requests

# Save HAR file
har_data = proxy.har
with open("network_log.har", "w") as har_file:
    json.dump(har_data, har_file, indent=4)

# Stop WebDriver and Proxy
driver.quit()
server.stop()

# Process HAR file to count status codes
def process_har(har_path):
    with open(har_path, "r") as file:
        har_data = json.load(file)

    total_requests = len(har_data["log"]["entries"])
    status_counts = {"1XX": 0, "2XX": 0, "3XX": 0, "4XX": 0, "5XX": 0}

    # Count occurrences of each status code category
    for entry in har_data["log"]["entries"]:
        status_code = entry["response"]["status"]
        category = f"{status_code // 100}XX"
        if category in status_counts:
            status_counts[category] += 1

    # Compute percentages
    status_summary = []
    for category, count in status_counts.items():
        percentage = round((count / total_requests) * 100, 2) if total_requests > 0 else 0
        status_summary.append({"category": category, "count": count, "percentage": percentage})

    # Save results as JSON
    output_data = {"total_requests": total_requests, "status_summary": status_summary}
    with open("network_summary.json", "w") as json_file:
        json.dump(output_data, json_file, indent=4)

# Run the function to generate the JSON summary
process_har("network_log.har")

print("✅ Process completed! Generated files: network_log.har & network_summary.json")
