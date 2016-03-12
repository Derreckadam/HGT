#! /usr/bin/python
# HGT_lineparse by Derreck
import csv
import sys

hgttxt = sys.argv[1]

print ("input file: " + hgttxt)

with open(hgttxt, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	count = 0
	hits = open("HGTFILE.txt", "wb")
	for row in reader:
		count += 1
		print (row[0], float(row[1]), row[2])
		if float(row[1]) <= .0000000000000000001:
			print row[1]
			print count
			hits.write("Row number: " + str(count) + row[1] + "\n")
	hits.close()
