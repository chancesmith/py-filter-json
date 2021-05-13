#!/usr/bin/env python3
import csv
import json
import sys
from pathlib import Path

## get arg 1 (path of json) and 2 (path of destination)
# args (json file, destination path)
# python3 main.py path/to/json path/for/output
jsonFilePath = str(sys.argv[1])
print(jsonFilePath)
outputPath = str(sys.argv[2])
print(outputPath)

## fetch the json file
contents = Path(jsonFilePath).read_text()
print(contents)

## json.loads() contents of json file
jsonData = json.loads(contents)

## filter json down to newsletter true
filteredUsersList = []

for id, user in jsonData.items():
  if user["newsletter"] == True:
    ## trim fields on json to: name, email, newsletter
    newUser = dict(name=user["name"], email=user["email"],
                   newsletter=user["newsletter"])
    filteredUsersList.append(newUser)

## let user check data
print(filteredUsersList)

## create file at arg 2
with open(outputPath, 'w') as csvfile:
  writer = csv.DictWriter(
      csvfile, fieldnames=('name', 'email', 'newsletter'))
  writer.writeheader()
  writer.writerows(filteredUsersList)
