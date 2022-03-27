import os
import json

if __name__ == '__main__':

    path = input("Please enter your path to the file of theHarvester?\n")
    stuff_in_string = 'cd {path} && theHarvester.py -d bing.com -b bing -f "data"'.format(path=path)
    path1 = r'%s' % stuff_in_string
    path2 = r'%s' % path+"\data.json"
    os.system(path1)
    with open(path2, "r") as f:
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

    with open(path2, 'w') as json_file:
        json.dump(output, json_file)
