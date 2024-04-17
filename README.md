Base on the https://docs.omniverse.nvidia.com/nucleus/latest/ports_connectivity.html , to check customer's network conectivity to NVIDIA assests.
Script will generate a test_resutlt.csv file



---

# URL Connectivity and Latency Tester

This Python script tests the connectivity and latency of specified URLs and records the results in a CSV format. It also includes optional geolocation reporting for the test execution environment.

## Features

- **Connectivity Testing**: Checks if URLs are accessible and measures their response times.
- **Port Testing**: Tests the connectivity on TCP ports 80 and 443 for each URL.
- **Geolocation**: Optionally records the city location of the test execution when enabled.
- **Output in CSV**: Saves the test results in a CSV file for easy data processing.

## Prerequisites

Before running the script, ensure that Python 3 is installed on your system. Additionally, you'll need to install several Python libraries, which are listed in the `requirements.txt` file.

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with optional arguments:

```bash
python AWStest3.py [-v] [-g]
```

- `-v, --verbose`: Increase output verbosity. This prints progress and detailed information on the console.
- `-g, --geo`: Record the geolocation (city) of the test execution. This appends city information to each test result in the CSV file.

## Output

The script generates a CSV file named `test_results.csv` in the current directory. It includes the following columns:

- `Number`: The sequence number of the URL tested.
- `Test Time`: The timestamp when the test was conducted.
- `URL Address`: The URL that was tested.
- `TCP 80`: The status of TCP port 80 (Open/Closed).
- `TCP 443`: The status of TCP port 443 (Open/Closed).
- `City`: (Optional) The city from where the script was run, if geolocation is enabled.

## Example of Output CSV

Here's what an example row in `test_results.csv` might look like:

```csv
Number,Test Time,URL Address,TCP 80,TCP 443,City
1,2023-04-01 12:00:00,https://example.com,Open,Closed,New York
```

## Contributions

Contributions are welcome! If you find a bug or would like to suggest a feature, please open an issue or submit a pull request.

---

This README provides a comprehensive guide for users on how to set up, run, and understand the output of your script. Adjust the `<repository-url>` and `<repository-directory>` placeholders accordingly before publishing on GitHub.
