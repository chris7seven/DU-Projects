# Christopher Seven

import numpy as np
import csv
import pandas as pd

exam_scores = np.random.randint(50, 100, (1000, 10))

with open("project6.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    headers = ['exam1', 'exam2', 'exam3', 'exam4', 'exam5', 'exam6', 'exam7', 'exam8', 'exam9', 'exam10']
    writer.writerow(headers)
    writer.writerows(list(row) for i, row in enumerate(exam_scores))

data = pd.read_csv("project6.csv")
datamean = data.mean()
datamode = data.mode()
datamedian = data.median()
datasd = data.std()


with open("project6results.txt", "w") as f:
    f.write("mean:\n" + str(datamean))
    f.write("\n")
    f.write("mode:\n" + str(datamode))
    f.write("\n")
    f.write("median:\n" + str(datamedian))
    f.write("\n")
    f.write("standard deviation:\n" + str(datasd))
    f.write("\n")
    f.write("Column headers:\n")
    f.write(str(data.columns.values.tolist()))
    f.write("\n")
    f.write("Row 8 pulled:\n")
    f.write(str(data.iloc[8,:]))
    f.write("\n")
    f.write("Row 4 pulled:\n")
    f.write(str(data.iloc[4,:]))
    f.write("\n")
    f.write("Row 6 pulled:\n")
    f.write(str(data.iloc[6,:]))

