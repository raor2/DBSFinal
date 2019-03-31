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
countyFile = open('Area_remap.csv')

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
            print(q1)
           # print(areaTypeLookupAdded)
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
            print(q2)
            cursor.execute(q2)
            conn.commit()
            NAICSLookupAdded.append((row[2],row[3]))

###############TABLE 5#######################
employmentFile.close()
employmentFile = open('employmentData.csv')
employmentReader = csv.reader(employmentFile)




#print("Adding from Crimes File")
#for row in crimeReader:
#    with conn.cursor() as cursor:
#        query = "INSERT INTO countylookup VALUES(" + "'" + row[0] + "' , '" + row[1] + "');"
#        cursor.execute(query)
#        conn.commit()


#print(crimeArray[1][1])

#for row in employmentReader:
    #print(row)


crimeFile.close()
employmentFile.close()






