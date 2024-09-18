import requests
import re
import json
import argparse
from datetime import datetime
import os

def extract_title(html_content):
    """
    Extracts the title text from the HTML content.

    Args:
        html_content (str): The HTML content of the web page.

    Returns:
        str: The extracted title text.
    """
    # Use regex to find the title text in the HTML
    title_pattern = re.compile(r'<table width="500" cellpadding="3" cellspacing="1" bgcolor="#A1B1BB">.*?<td height="25" colspan="3" class="table1"><span class="m1">(.*?)</span>', re.DOTALL)
    match = title_pattern.search(html_content)
    if not match:
        raise Exception("Couldn't find the title text in the HTML")

    # Return the extracted title text
    return match.group(1).strip()

def fetch_data(year, month, pid):
    """
    Fetches data from the specified URL and returns the extracted data array as floats,
    and the title text from the HTML.

    Args:
        year (str): The year in YYYY format.
        month (str): The month in MM format.
        pid (int): The pid value.

    Returns:
        tuple: A tuple containing the extracted data array with float values and the title text.
    """
    # Construct the URL using the variables
    url = f"https://www.metnet.hu/napi-adatok?sub=4&pid={pid}&date={year}-{month}-1"

    # Fetch the web page content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the web page. Status code: {response.status_code}")

    # Extract the title from the HTML
    title = extract_title(response.text)

    # Use regex to find the `chartData2` variable
    pattern = re.compile(r"var chartData2 = ({.*?});", re.DOTALL)
    match = pattern.search(response.text)
    if not match:
        raise Exception("Couldn't find 'chartData2' variable in the HTML")

    # Extract the JSON-like string
    chart_data2_str = match.group(1)

    # Use regex to extract the `data` array from `datasets[0].data`
    data_pattern = re.compile(r'data:\s*(\[[^\]]*\])')
    data_match = data_pattern.search(chart_data2_str)
    if not data_match:
        raise Exception("Couldn't find 'data' array in the 'chartData2' variable")

    # Extract the data array string and convert it to a Python list
    data_str = data_match.group(1)
    data_list_str = json.loads(data_str)

    # Convert the list of strings to a list of floats
    data_list = [float(value) for value in data_list_str]

    return data_list, title

def update_json(pid, year_str, month_str, data_list, title):
    """
    Updates or creates a JSON file for the given PID with the new data.

    Args:
        pid (int): The PID value.
        year_str (str): The year in YYYY format.
        month_str (str): The month in MM format.
        data_list (list): The list of float data.
        title (str): The title text to include in the JSON.
    """
    # Directory for the PID JSON files
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # File path for the specific PID
    file_path = os.path.join(directory, f'pid{pid}.json')

    # Initialize the organized data structure
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            organized_data = json.load(json_file)
    else:
        organized_data = {"title": title, "data": {}}

    # Update the data for the specified PID
    if year_str not in organized_data["data"]:
        organized_data["data"][year_str] = {}

    organized_data["data"][year_str][month_str] = data_list

    # Save the organized data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(organized_data, json_file, indent=4)

    print(f"Data for PID {pid} has been saved to '{file_path}'")

def main(pid):
    # Define the start and end dates
    start_year = 2024
    start_month = 1
    current_year = datetime.now().year
    current_month = datetime.now().month

    # Fetch data for each month from May 2024 to the month before the current month
    for year in range(start_year, current_year + 1):
        for month in range(start_month if year == start_year else 1, 13):
            if year == current_year and month > current_month:
                break

            month_str = f"{month:02d}"
            year_str = f"{year}"
            print(f"Fetching data for {year_str}-{month_str}")

            data_list, title = fetch_data(year_str, month_str, pid)
            update_json(pid, year_str, month_str, data_list, title)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and organize data from the MetNet website.")
    parser.add_argument('pid', type=int, help="The PID value to use for fetching data.")
    args = parser.parse_args()
    main(args.pid)
