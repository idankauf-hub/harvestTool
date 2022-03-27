import os
import json

if __name__ == '__main__':

    path = input("Please enter the path to the folder of theHarvester:\n")
    command = 'cd {path} && theHarvester.py -d bing.com -b bing -f "data"'.format(path=path)
    pathToFolder = r'%s' % command
    pathToJson = r'%s' % path+"\data.json"
    os.system(pathToFolder)
    with open(pathToJson, "r") as f:
        data = json.load(f)

    output = []

    for element in data["hosts"]:
        if ":" in element:
            line = element.split(":")
            output.append({"asset": line[0], "ip": line[1]})
        else:
            output.append({"asset": element, "ip": "No ip"})
    print("JSON File: \n", output)

    with open(pathToJson, 'w') as json_file:
        json.dump(output, json_file)
