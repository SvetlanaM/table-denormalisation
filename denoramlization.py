import csv
import ast
import os, glob

#final table rows
rows = []

# mapping variant values
variants = []

#csv header
headers = ["document_id", "variant_id"]

with open("./data/in/tables/*.csv") as infile, open("./data/in/tables/*.-out.csv") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    writer.writerow(headers)
    for index_row, data_in_row in enumerate(reader):
        for index_col, data_in_cell in enumerate(data_in_row):
            if index_row > 0:
                rows.append(data_in_row[index_col])
                if index_col == 7:
                    try:
                        variants = ast.literal_eval(data_in_row[7])
                    except:
                        pass

        #remove duplicates
        variants = dict.fromkeys(variants).keys()
        for variant in variants:
            writer.writerow([data_in_row[1], variant])


    print ("========= Creating the asociated table is done ========")
    infile.close()
    outfile.close()
