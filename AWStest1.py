import requests
import time
import socket
from datetime import datetime
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Test connectivity and latency of URLs, reporting in milliseconds.")
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
args = parser.parse_args()

# Define the list of URLs to test
urls = [
    "https://omniverse-content-production.s3.ap-southeast-1.amazonaws.com",
    "https://omniverse-content-production.s3-ap-southeast-1.amazonaws.com",
    "https://twinbru.s3.ap-southeast-1.amazonaws.com/omniverse",
    "https://d1aiacozzchaiq.cloudfront.net",
    "https://dw290v42wisod.cloudfront.net",
    "https://dcb18d6mfegct.cloudfront.net",
    "https://kit-extensions.ov.nvidia.com",
    "https://ovextensionsprod.blob.core.windows.net",
    "https://content-production.omniverse.nvidia.com",
    "https://login.nvidia.com",
    "https://api.launcher.omniverse.nvidia.com",
    "https://data.launcher.omniverse.nvidia.com",
    "https://gdpr.launcher.omniverse.nvidia.com",
    "https://install.launcher.omniverse.nvidia.com",
    "https://messages.launcher.omniverse.nvidia.com",
    "https://index.launcher.omniverse.nvidia.com"
]

def test_url(url):
    result = ""
    try:
        # Extract hostname from URL
        hostname = url.split("//")[-1].split("/")[0]
        # Resolve IP address
        ip_address = socket.gethostbyname(hostname)
        # Record the start time
        start_time = time.time()
        # Send a GET request with a timeout, only fetching headers initially
        response = requests.get(url, stream=True, timeout=5)
        # Calculate the latency in milliseconds
        latency_ms = (time.time() - start_time) * 1000
        # Check the status code to determine connectivity
        connectivity = "Connected" if response.status_code == 200 else "Not Connected"
        # Format the test report to be on a single line
        result = f"URL: {url}, IP: {ip_address}, Latency: {latency_ms:.2f} ms, Connectivity: {connectivity}"
    except Exception as e:
        result = f"URL: {url}, IP: N/A, Error: {str(e)}, Connectivity: Not Connected"
    return result

# Open the file in append mode
with open("test_results.txt", "a") as file:
    # Write the current datetime at the beginning of new test results
    test_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(f"Test Results - {test_time}")
    if args.verbose:
        file.write(" - Detailed")
    file.write("\n")
    
    # Test each URL and append the results to the file
    total_urls = len(urls)
    for index, url in enumerate(urls, start=1):
        result = test_url(url)
        file.write(result + "\n")
        # Print progress to the console
        print(f"Progress: {index}/{total_urls} - {result}")

print("Testing completed.")
