#!/usr/bin/python
import csv
import json

with open("node_exporter.csv", "rb") as nodeexfile:
    reader = csv.reader(nodeexfile)
    next(reader, None)
    for row in reader:
        print(row[1])