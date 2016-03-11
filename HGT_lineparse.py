#! /usr/bin/python
# HGT_lineparse by Derreck
import csv
import sys

hgttxt = sys.argv[1]

print ("input file: " + hgttxt)

with open(hgttxt, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print (row[0], float(row[1]), row[2])
		if float(row[1]) <= .0000000000000000001:
			print row[1]
