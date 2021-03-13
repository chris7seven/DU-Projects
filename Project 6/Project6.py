# Christopher Seven
# Project 6

import numpy as np
import csv
import pandas as pd

# Creating a 1000x10 matrix filled with random "scores" from 50 to 100. These will mimic exam scores for 1000 students over 10 exams.
exam_scores = np.random.randint(50, 100, (1000, 10))

# Opening a new csv file to write to.
with open("project6.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    # Establishing the headers as the exam numbers.
    headers = ['exam1', 'exam2', 'exam3', 'exam4', 'exam5', 'exam6', 'exam7', 'exam8', 'exam9', 'exam10']
    writer.writerow(headers)
    # Writing in the headers, and then writing in the values from the matrix.
    writer.writerows(list(row) for i, row in enumerate(exam_scores))

# Reading in the csv files into a dataframe in pandas.
data = pd.read_csv("project6.csv")
# Calculating the statistics required.
datamean = data.mean()
datamode = data.mode()
datamedian = data.median()
datasd = data.std()

# Opening up a new text file.
with open("project6results.txt", "w") as f:
    # Here we write in each of the statistics first.
    f.write("mean:\n" + str(datamean))
    f.write("\n")
    f.write("mode:\n" + str(datamode))
    f.write("\n")
    f.write("median:\n" + str(datamedian))
    f.write("\n")
    f.write("standard deviation:\n" + str(datasd))
    f.write("\n")
    # Writing in the column headers next.
    f.write("Column headers:\n")
    f.write(str(data.columns.values.tolist()))
    f.write("\n")
    # Pulling 3 rows from the matrix and writing them to the text file.
    f.write("Row 8 pulled:\n")
    f.write(str(data.iloc[8,:]))
    f.write("\n")
    f.write("Row 4 pulled:\n")
    f.write(str(data.iloc[4,:]))
    f.write("\n")
    f.write("Row 6 pulled:\n")
    f.write(str(data.iloc[6,:]))

