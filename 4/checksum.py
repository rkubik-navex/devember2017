import csv
import math

def checkSumRow(row):
    max = -math.inf
    min = math.inf
    for numberString in row:
        number = int(numberString)
        if (number > max):
            max = number
        if (number < min):
            min = number
    return max - min


with open('data.tsv', 'r') as dataFile:
    reader = csv.reader(dataFile, delimiter='\t')
    sum = 0
    for row in reader:
        sum += checkSumRow(row)
    print(sum)
