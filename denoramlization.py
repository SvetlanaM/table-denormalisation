import csv

file_name = input("Add name of the csv: ")


with open(file_name + '.csv', 'r') as infile, open(file_name + '-out.csv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for index_row, data_in_row in enumerate(reader):
        for index_col, data_in_cell in enumerate(data_in_row):
            if index_row > 0:
                if index_col == 7:
                    for item in data_in_row[7]:
                        writer.writerow(data_in_row)

        if index_row > 15:
            break

    print (" First conversion is done ")
    infile.close()
    outfile.close()
