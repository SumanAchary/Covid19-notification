# COVID-19 Notification System Documentation

This program retrieves COVID-19 statistics from the Ministry of Health and Family Welfare website of India (https://www.mohfw.gov.in/) and displays notifications for selected states in Linux systems.

## Requirements

To run this program smoothly on a Linux system, the following dependencies are required:

- `beautifulsoup4==4.9.1`
- `bs4==0.0.1`
- `certifi==2020.4.5.2`
- `chardet==3.0.4`
- `idna==2.9`
- `requests==2.23.0`
- `ruamel.yaml==0.16.10`
- `ruamel.yaml.clib==0.2.0`
- `soupsieve==2.0.1`
- `urllib3==1.25.9`
- `vext==0.7.3`
- `vext.gi==0.7.0`

Note: For Windows systems, the `plyer==1.4.3` library is required, but not necessary for Linux systems.

## Usage

This program utilizes web scraping to fetch COVID-19 data from the specified Ministry of Health and Family Welfare website. To run the program:

1. Ensure that all the listed dependencies are installed on your Linux system.
2. Run the Python script.

Upon execution, the program retrieves data, extracts COVID-19 statistics for selected states (modifiable within the code), and triggers notifications for the selected states with the following information:

- State
- Active Cases
- Deaths
- Cured/Discharged/Migrated
- Total Cases

Modify the `selStates` list in the script to include or remove states for which you wish to receive notifications.

## Functionality

- `notifyMe()`: Utilizes `gi` in Linux to create and display notifications, specifying a title and message with COVID-19 statistics.
- `getData(url)`: Retrieves HTML data from the specified URL (`https://www.mohfw.gov.in/` in this case).
- Extracts and processes COVID-19 statistics for various states and triggers notifications for selected states.

## Note

Make sure to have an internet connection for data retrieval, and ensure the code has access to the specified URL.
