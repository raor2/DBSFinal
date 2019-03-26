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

crimeReader = csv.reader(crimeFile)
employmentReader = csv.reader(employmentFile)

crimeArray = []

countyLookupAdded = []
areaLookupAdded = []
areaTypeLookupAdded = []
NAICSLookupAdded = []
wagesAdded = []
crimeAdded = []
<<<<<<< Updated upstream

=======





connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor)
setupDatabase()


for row in employmentReader:
    with conn.cursor() as cursor:
        if(row[1] != 'Area' and not (row[1],row[0]) in areaTypeLookupAdded): 
            q1 = "INSERT INTO areatypelookup VALUES('" + row[1] + "' , '" + row[0] + "');"   # WHERE " + row[1] + " NOT IN areatypelookup;"
            print(q1)
           # print(areaTypeLookupAdded)
            cursor.execute(q1)
            conn.commit()
        
            areaTypeLookupAdded.append((row[1],row[0]))

for row in crimeReader:
    with conn.cursor() as cursor:
        query = "INSERT INTO countylookup VALUES(" + "'" + row[0] + "' , '" + row[1] + "');"
        cursor.execute(query)
        conn.commit()


#print(crimeArray[1][1])
>>>>>>> Stashed changes

#for row in employmentReader:
    #print(row)



connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor)
setupDatabase()


for row in employmentReader:
    with conn.cursor() as cursor:
        if(row[1] != 'Area' and not (row[1],row[0]) in areaTypeLookupAdded): 
            q1 = "INSERT INTO areatypelookup VALUES('" + row[1] + "' , '" + row[0] + "');"   # WHERE " + row[1] + " NOT IN areatypelookup;"
            print(q1)
           # print(areaTypeLookupAdded)
            cursor.execute(q1)
            conn.commit()
        
            areaTypeLookupAdded.append((row[1],row[0]))

for row in crimeReader:
    with conn.cursor() as cursor:
        query = "INSERT INTO countylookup VALUES(" + "'" + row[0] + "' , '" + row[1] + "');"
        cursor.execute(query)
        conn.commit()


#print(crimeArray[1][1])

#for row in employmentReader:
    #print(row)


crimeFile.close()
employmentFile.close()






