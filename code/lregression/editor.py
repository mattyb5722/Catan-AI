import csv
import os
import shutil
from tempfile import NamedTemporaryFile
def get_length(file_path):
    with open("catanstatsrev2.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def edit_data(headername):
    filename = "catanstatsrev22.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "r") as csvfile, open('tempfile.csv', "w", newline="") as temp_file:
        reader = csv.DictReader(csvfile)        #reads from the original
        fieldnames = ['gameNum', 'player', 'points', 's1v1', 's1r1', 's1v2', 's1r2', 's1v3', 's1r3', 's1tot', 's2v1', 's2r1', 's2v2', 's2r2', 's2v3', 's2r3', 'set2tot']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)  #writes on the temp file
        writer.writeheader()
        for row in reader:
            print(temp_file)
            print(row)
            if float(row[headername]) == 2 or float(row[headername]) == 12:
                row[headername] = 2.78
                writer.writerow(row)
            if float(row[headername]) == 3 or float(row[headername]) == 11:
                row[headername] = 5.56
                writer.writerow(row)
            if float(row[headername]) == 4 or float(row[headername]) == 10:
                row[headername] = 8.33
                writer.writerow(row)
            if float(row[headername]) == 5 or float(row[headername]) == 9:
                row[headername] = 11.11
                writer.writerow(row)
            if float(row[headername]) == 6 or float(row[headername]) == 8:
                row[headername] = 13.89
                writer.writerow(row)
            if float(row[headername]) == 0:     #Must account for desert tiles which have no value
                row[headername] = 0
                writer.writerow(row)
        # shutil.move(temp_file.name, filename)
        return True
    return False


edit_data('s1v3')

#PermissionError: [WinError 32] process cannot access the file because being used by another process: 'C:\\Users\\DanielK\\AppData\\Local\\Temp\\tmprll4vz85'