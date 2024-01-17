# HashRate API Tool

## Overview

This Python script interacts with the HashRate.no API to retrieve estimates for cryptocurrency mining profitability based on power costs and device specifications. It provides features to reload data from the API, display information about mining devices, and more.

## Prerequisites

- Python 3.x
  - requests
  - argparse

## Usage

## Command-line Options

- `--reload`: Reload data from the HashRate.no API.
- `--compute`: Specify the compute type (gpu or cpu, default is gpu).
- `--power`: Set the cost of power in kWh (default is 0.18 USD).
- `--list_devices`: List available mining devices from the API.
- `--devices`: Return data for specific devices (default: ["5700g", "3060", "1660s", "2060s"]).
