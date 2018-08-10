# # -*- coding: utf8 -*-
import csv, json, codecs, io


def CSV2JSON():

    finalJSON = "{\"data\":["

    csvfile = "./Input.csv"

    with open(csvfile, mode='rb') as csvfile:

        fieldnames = ["column1","column2","column3", "column4", "column5","column6"] #columns in the CSV
        reader = csv.DictReader(csvfile, fieldnames=fieldnames) #set the reader of the csv

        for row in reader:
            finalJSON = finalJSON + json.dumps(row, ensure_ascii=False, encoding='utf-8', separators=(',', ':')) +"," 
        finalJSON = finalJSON[0:-1] + "]}" #append the rows as objects to the data array in the JSON String

        with io.open('./Output.json', 'w', encoding='utf8') as json_file: #create the file - Overwrite if exists
            json_file.write(finalJSON.decode('utf-8')) #write the JSON String in the file.
            json_file.close()


if __name__ == "__main__":
    CSV2JSON()