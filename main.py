from apikey import api_key
import requests
import json


def gpu_data():
    req = requests.get(f"https://api.hashrate.no/v1/gpuEstimates?apiKey={api_key}&powerCost=0.17")
    return req.json()

def write(gpu_json):
    with open(file='hashrate', mode="w") as j:
        gpu_json = json.dumps(gpu_json)
        j.write(gpu_json)
def read():
    with open(file='hashrate', mode='r') as r:
        return json.load(r)


def main():
    try:
        gpu_json_data = read()
    except FileNotFoundError:
        gpu_data_json = gpu_data()
        write(gpu_data_json)

    for i in gpu_json_data:
        print(i['device'])





if __name__ == "__main__":
    main()