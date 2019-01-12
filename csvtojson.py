#!/usr/bin/python
import csv
import json

targets = dict()

with open("node_exporter.csv", "rb") as nodeexfile:
    reader = csv.reader(nodeexfile)
    next(reader, None)
    new_env = 1
    for row in reader:
        for idx, element in enumerate(targets):
            if element["env"] == row[1]:
                print(idx, element)
                new_env = 0

