from apikey import api_key
import requests
import json
import argparse
import sys
from time import sleep
def hash_data(power, compute):
    while True:
        req = requests.get(f"https://api.hashrate.no/v1/{compute}Estimates?apiKey={api_key}&powerCost={power}")

        if req.ok:
            write(req.json())
            return req.json()
        else:
            print('Api request failed.  Trying again in 5 seconds.  Ctrl-c to quit')
            sleep(5)

def write(hash_json):
    with open(file='hashrate', mode="w") as j:
        hash_json = json.dumps(hash_json)
        j.write(hash_json)
def read():
    with open(file='hashrate', mode='r') as r:
        return json.load(r)

def check_for_file():

    try:
        return read()

    except FileNotFoundError:
        return False

def display_results(json_data, devices):

    for i in json_data:
        if i in devices:
            print(f'{i} {json_data[i]["profit"]["coin"]} profit: {json_data[i]["profit"]["profitUSD"]}, revenue: {json_data[i]["profit"]["revenueUSD"]}')
            print(f'{i} {json_data[i]["revenue"]["coin"]} revenue: {json_data[i]["revenue"]["revenueUSD"]} profit: {json_data[i]["revenue"]["profitUSD"]}')


def list_compute_devices(json_data):
    for i in json_data:
        print(i)

def main():
    if args.reload:
        hashrateno_json_data = hash_data(args.power, args.compute)
    else:
        hashrateno_json_data = read()

    if args.list_devices:
        list_compute_devices(read())
        sys.exit()

    display_results(hashrateno_json_data, args.devices)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HashRate.no\'s api tools.. get coins that are most profitable and highest revenue for your devices')
    parser.add_argument('--reload', help='reload data from api', action="store_true")
    parser.add_argument('--compute', help='compute type gpu or cpu default is gpu', type=str, default="gpu")
    parser.add_argument('--power', help='cost of power in kWh default is 0.18 USD', type=str, default="0.18")
    parser.add_argument('--list_devices', help='list devices, when combines with --type available from api', action="store_true")
    parser.add_argument('--devices', help='return data for these devices',  nargs='+', type=str, default=["5700g","3060", "1660s", "2060s"])
    args = parser.parse_args()
    main()