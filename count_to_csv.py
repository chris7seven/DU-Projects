import count
import sys
import csv

def count_to_csv():
    #This function writes the dictionary created from flags() in count.py into a csv file.
    vals = []
    for val in sys.argv:
        vals.append(val)

    d = {}
    d = count.flags(vals)
    for i in vals:
        if i.endswith(".csv"):
            with open(str(i), 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in d.items():
                    writer.writerow([key, value])

count_to_csv()
