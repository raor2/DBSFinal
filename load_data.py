import csv
import psycopg2
import psycopg2.extras



def setupDatabase():
    connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)

    with conn.cursor() as cursor:
        with open('makeTable.sql','r') as project_data:
            queries = project_data.read()
            cursor.execute(queries)

        conn.commit()



crimeFile = open('crimeData.csv')
employmentFile = open('employmentData.csv')
countyFile = open('areaTypeLookup.csv')

crimeReader = csv.reader(crimeFile)
employmentReader = csv.reader(employmentFile)
countyReader = csv.reader(countyFile)

crimeArray = []

countyLookupAdded = []
areaLookupAdded = []
areaTypeLookupAdded = []
NAICSLookupAdded = []
wagesAdded = []
crimeAdded = []

connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor)
setupDatabase()

##############TABLE 3######################
for row in employmentReader:
    with conn.cursor() as cursor:
        if(row[1] != 'Area' and not (row[1],row[0]) in areaTypeLookupAdded):
            q1 = "INSERT INTO areatypelookup VALUES('" + row[1] + "' , '" + row[0] + "');"
            #print(q1)
            #print(areaTypeLookupAdded)
            cursor.execute(q1)
            conn.commit()

            areaTypeLookupAdded.append((row[1],row[0]))


#############TABLE 4######################
employmentFile.close()
employmentFile = open('employmentData.csv')
employmentReader = csv.reader(employmentFile)

for row in employmentReader:
    #print(row)
    with conn.cursor() as cursor:
        row[3] = row[3].replace("'","")

        if(row[2] != 'NAICS' and not (row[2],row[3]) in NAICSLookupAdded):
            q2 = "INSERT INTO naicslookup VALUES('" + row[2] + "', '" + row[3] + "');"
            #print(q2)
            cursor.execute(q2)
            conn.commit()
            NAICSLookupAdded.append((row[2],row[3]))

###############TABLE 5#######################
employmentFile.close()
employmentFile = open('wages.csv')
employmentFile.readline()
#readline(employmentFile)
employmentReader = csv.reader(employmentFile)
cursor = conn.cursor()
cursor.copy_from(employmentFile, 'wages', sep=',')
conn.commit()


#############TABLE 6#######################
crimeFile.close()
crimeFile = open('crime.csv')
crimeFile.readline()
cursor = conn.cursor()
cursor.copy_from(crimeFile,'crime', sep = ',')
conn.commit()

################TABLE 2###################
f = open('areaTypeLookup.csv')
f.readline()
cursor = conn.cursor()
cursor.copy_from(f,'arealookup', sep = ',')
conn.commit()

################TABLE 1####################
f = open('countyLookup.csv')
f.readline()
#readline(f)
cursor = conn.cursor()
cursor.copy_from(f,'countylookup', sep = ',')
conn.commit()


crimeFile.close()
employmentFile.close()
