# HGT_lineparse
import csv
import sys

hgttxt = sys.argv[1]

print ("input file: ", hgttxt)

with open(hgttxt, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print (row[0], row[1], row[2])
