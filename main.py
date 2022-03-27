# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    os.system(r'cd C:\Projects\theHarvester && theHarvester.py -d bing.com -b bing -f "data"')
    with open(r"C:\Projects\theHarvester\data.json") as f:
        data = json.load(f)

    output = []

    for element in data["hosts"]:
        if ":" in element:
            line = element.split(":")
            output.append({"asset": line[0], "ip": line[1]})
        else:
            output.append({"asset": element, "ip": "No ip"})
    print("JSON File: " + output)

    with open(r"C:\Projects\theHarvester\data.json", 'w') as json_file:
        json.dump(output, json_file)
