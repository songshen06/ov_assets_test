import requests
import time
import socket
from datetime import datetime
import csv
import argparse
import geocoder

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Test connectivity and latency of URLs, and record results in CSV format.")
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
parser.add_argument("-g", "--geo", action="store_true", help="Record the geolocation of the test execution")
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

def check_port(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)  # Timeout for the socket operation
    result = sock.connect_ex((hostname, port))
    sock.close()
    return "Open" if result == 0 else "Closed"

def get_location():
    g = geocoder.ip('me')
    return g.city if g.city else "City not available"

def test_url(url, index):
    try:
        # Extract hostname from URL
        hostname = url.split("//")[-1].split("/")[0]
        # Test TCP ports
        tcp80 = check_port(hostname, 80)
        tcp443 = check_port(hostname, 443)
        # Record the test time
        test_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Record the test result
        result = [index, test_time, url, tcp80, tcp443]
        if args.geo:
            location = get_location()
            result.append(location)
    except Exception as e:
        result = [index, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), url, "Error", "Error"]
        if args.geo:
            result.append("City error")
    return result

# Write results to a CSV file
with open("test_results.csv", "w", newline='') as file:
    writer = csv.writer(file)
    # Write the header
    header = ["Number", "Test Time", "URL Address", "TCP 80", "TCP 443"]
    if args.geo:
        header.append("City")
    writer.writerow(header)
    # Test each URL and append the results to the CSV file
    for index, url in enumerate(urls, start=1):
        result = test_url(url, index)
        writer.writerow(result)
        # Optionally print progress to the console if verbose is enabled
        if args.verbose:
            print(f"Progress: {index}/{len(urls)} - {result}")

print("Testing completed.")
