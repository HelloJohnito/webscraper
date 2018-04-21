import csv


def export_to_file(results, new_file_name):
    column_names = [["Date", "Title", "Price", "Link"]]

    with open(new_file_name, 'w') as new_file:
        writeCSV = csv.writer(new_file, delimiter=',')

        # Set the column names
        for names in column_names:
            writeCSV.writerow(names)

        # Set all rows
        for i in range(0, results["length"]):
            columns = []
            for col in column_names[0]:
                columns.append(results[i][col.lower()])

            writeCSV.writerow(columns)

    return




# def read_and_convert_to_list(file):
#     list = []
#     with open(file, 'r') as csvfile:
#         readCSV = csv.reader(csvfile)
#
#         for row in readCSV:
#             list.append(row)
#     return list
#
#
# def write_to_file(list, new_file_name):
#     with open(new_file_name, 'w') as new_file:
#         writeCSV = csv.writer(new_file, delimiter=',')
#
#         for row in list:
#             writeCSV.writerow(row)
#     return
