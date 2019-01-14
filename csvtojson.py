#!/usr/bin/python
import csv
import json

targetarray = []


with open("node_exporter.csv", "rb") as nodeexfile:
    reader = csv.reader(nodeexfile)
    next(reader, None)
    for row in reader:
        new_target = 0
        idx = 0
        new_element = dict()
        element = dict()
        for idx, element in enumerate(targetarray):
            if element['labels']['env'] == row[1]:
                new_target = 1
                if element['labels']['job'] == row[2]:
                    if element['labels']['service'] == row[3]:
                        new_target = 1
                        if row[0] not in element['targets']:
                            print(row[0])
                            element["labels"] = {'env': row[1], 'job': row[2], 'service': row[3]}
                            element['targets'].append(row[0])


                    else:
                        new_target = 0
                else:
                    new_target = 0

        if new_target == 0:
            new_element["labels"] = {'env': row[1], 'job': row[2], 'service': row[3]}
            if 'targets' not in new_element['labels']:
                new_element['targets'] = []
            new_element['targets'].append(row[0])

            targetarray.append(new_element)

for dictrow in targetarray:
    print(json.dumps(dictrow))

with open('new_targets.json', 'wb') as outfile:
    json.dump(targetarray, outfile)