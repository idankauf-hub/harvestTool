import os
import json

if __name__ == '__main__':
    os.system(r'cd C:\Projects\theHarvester && theHarvester.py -d bing.com -b bing -f "data"')
    with open(r"C:\Projects\theHarvester\data.json") as f:
        data = json.load(f)

    output = []

    for element in data["hosts"]:
        print(element)
        if ":" in element:
            line = element.split(":")
            output.append({"asset": line[0], "ip": line[1]})
        else:
            output.append({"asset": element, "ip": "No ip"})
    print("JSON File: \n", output)

    with open(r"C:\Projects\theHarvester\data.json", 'w') as json_file:
        json.dump(output, json_file)
