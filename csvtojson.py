#!/usr/bin/python

__author__ = "Nano-Naga"
__version__ = "1.1"

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

                if element['labels']['businessUnit'] == row[2]:

                    if element['labels']['service'] == row[3]:
                        
                        if element['labels']['os'] == row[4]:
                            
                             if element['labels']['action'] == row[5]:

                                  if element['labels']['businessImpact'] == row[6]:  
                                    
                                     new_target = 1

                                     if row[0] not in element['targets']:

                                      element["labels"] = {'env': row[1], 'businessUnit': row[2], 'service': row[3], 'os': row[4], 'action': row[5], 'businessImpact': row[6] }

                                      element['targets'].append(row[0])

                    else:

                        new_target = 0

                else:

                    new_target = 0



        if new_target == 0:

            new_element["labels"] = {'env': row[1], 'businessUnit': row[2], 'service': row[3], 'os': row[4], 'action': row[5], 'businessImpact': row[6]}

            if 'targets' not in new_element['labels']:

                new_element['targets'] = []

            new_element['targets'].append(row[0])

            targetarray.append(new_element)





with open('new_targets.json', 'wb') as outfile:

    json.dump(targetarray, outfile)



with open("targets.json") as exporterfile:

    exporterdata = json.load(exporterfile)



    print ('total items before running the script : ' + str(len(exporterdata)))

    for i in targetarray:

        print (i['targets'])

        chk_existing = filter(lambda tgt: tgt['targets'] == i['targets'], exporterdata)

        if chk_existing:

            print ("Node already Exist in target.json file")

        else:

            exporterdata.append(i)

            print('target '+ str(i) + 'added')

    



print ('total items before after the script : ' + str(len(exporterdata)))



with open('targets.json', 'wb') as newfile:

    json.dump(exporterdata,newfile,indent=4, sort_keys=True)
