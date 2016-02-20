# HGT_lineparse
import csv
import sys

filename = sys.argv[1]

print ("input file: ", filename)

with open(filename, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print (row[0], row[1], row[2])