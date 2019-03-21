import csv
import psycopg2
import psycopg2.extras


crimeFile = open('crimeData.csv')
employmentFile = open('employmentData.csv')

crimeReader = csv.reader(crimeFile)
employmentReader = csv.reader(employmentFile)

for row in crimeReader:
    print(row)

for row in employmentReader:
    print(row)







crimeFile.close()
employmentFile.close()






