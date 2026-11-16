import json
import TableClass
import sys

"""
This module expects a very specific kind of JSON files, it expects a list of objects/
and array of dictionaries containing key-value pairs. The keys maybe jagged across the
objects, meaning some objects may have entirely missing fields. It gracefully fills
those fields with 'N/A' meaning not available or not applicable. This module can tabulate
multiple files at once, they must be passed as arguments while invoking the python executable


execution: python advanced.py file1.json file2.json file3.json ...

note: please keep the files and this module at the same level of whatever directory it is in.
Make sure to *download my TableClass module, as that is a dependency*.
"""

FULL_LIST=sys.argv
fileNames=FULL_LIST[1:]
loadedJSONs=[]
for file in fileNames:
    FILE=open(file)
    loadedJSON=json.load(FILE)
    loadedJSONs.append(loadedJSON)
    FILE.close()

header=[]

for loadedJSON,fileName in zip(loadedJSONs,fileNames):
    if isinstance(loadedJSON,list):
        # contains many objects
        for infoBlock in loadedJSON:
            for category in infoBlock:
                if category not in header:
                    header.append(category)
        header.clear()

        table=[header,*([infoBlock[category] if category in infoBlock else "N/A" for category in header] for infoBlock in loadedJSON)]
        TABLE_OBJ=TableClass.Table(table, padding=5, title=fileName.rsplit(".",1)[0], style="curved")
        print(TABLE_OBJ)
            
    else:
        # invalid
        raise TypeError("Must be a list of key-value pair objects.")
