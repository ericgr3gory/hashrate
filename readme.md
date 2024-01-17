# Hashrate.no API Tools

This Python script provides an interface to interact with the Hashrate.no API. It allows users to fetch and display data about cryptocurrency mining profitability for various compute devices.

## Features

- Retrieve and display the most profitable coins and highest revenue for your mining devices.
- Support for GPU and CPU data retrieval.
- Ability to reload data directly from the API.
- Listing available compute devices.
- Customizable power cost and compute type settings.

## Usage

The script is designed to be run from the command line with various options:

- `--reload`: Reload data from the API.
- `--compute`: Specify the compute type (`gpu` or `cpu`). Default is `gpu`.
- `--power`: Set the cost of power in kWh. Default is `0.18` USD.
- `--list_devices`: List all available devices from the API.
- `--devices`: Specify which devices to return data for. Accepts multiple values.

## Configuration

Before running the script, ensure you have an API key from Hashrate.no. Store this key in a separate file (`apikey.py`) and import it into the script.

## Functions

- `get_hashratedotno_data(power, compute)`: Fetches data from the Hashrate.no API.
- `write(hash_json)`: Writes JSON data to a file.
- `read()`: Reads JSON data from a file.
- `check_for_file()`: Checks if the data file exists.
- `display_results(json_data, devices)`: Displays the results for the specified devices.
- `list_compute_devices(json_data)`: Lists all compute devices available from the API.

## Error Handling

The script includes basic error handling for API request failures and file operations.

## Requirements

- Python 3
- `requests` library

## Contributing

Contributions to the script are welcome. Please adhere to standard Python coding conventions.

## License

[Specify License Here]

## Disclaimer

This script is provided as-is, and the author is not responsible for any misuse or damage caused by the script.
