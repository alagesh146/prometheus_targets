#!/usr/bin/python
import csv
import json

targets = []


with open("node_exporter.csv", "rb") as nodeexfile:
    reader = csv.reader(nodeexfile)
    next(reader, None)
    for row in reader:
        new_env = 0
        idx = 0
        element = dict()
        for idx, element in enumerate(targets):
            if element["labels"]["env"] == row[1]:
                new_env = 1
                new_service = 0
#                if element["labels"]["service"] == row[3]:
#                    print(row[3])
#                else:
#                    element["labels"]["service"] = row[3]
#                    print(element["service"])

        if new_env == 0:
            element["labels"]["env"] = row[1]
            targets.append(element["labels"]["env"])
            print(element["labels"]["env"])
            targets[idx] = element

        print(targets)
