# Network Scanner

## Overview

The Network Scanner script is designed for penetration testing, specifically for scanning network devices by identifying their IP and MAC addresses. The script utilizes Python libraries such as `scapy` for crafting and sending network packets.

## Dependencies

- `scapy`: For crafting and sending network packets.
- `argparse`: For parsing command-line arguments.

## Usage

The script is intended to be run from the command line. It requires the target IP address or range to scan.

## Functions

### `get_arguments()`

- Parses command-line arguments to get the target IP address.
- Returns:
  - `argparse.Namespace`: An object containing the parsed arguments.

### `scan(ip_address)`

- Scans the given IP address or range for active devices.
- Parameters:
  - `ip_address` (str): The IP address or range to scan.
- Returns:
  - `list`: A list of dictionaries containing IP and MAC addresses of the discovered devices.

### `print_result(result_list)`

- Prints the scan results in a tabular format.
- Parameters:
  - `result_list` (list): A list of dictionaries containing IP and MAC addresses of the discovered devices.

## Example Usage

To run the script, use the following command:

```bash
python network_scanner.py -t 192.168.1.1/24
