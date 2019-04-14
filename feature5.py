import psycopg2
import psycopg2.extras
#from decimal import Decimal


connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()
cursor.execute("SELECT w.avgEmployment as employment, c.totalCrimes as crime \
                FROM Wages w, Crime c, CountyLookup cl, AreaLookup al\
                WHERE c.Agency = cl.Agency \
                AND cl.County = al.County \
                AND al.Area = w.Area;")
records = cursor.fetchall()

crime_employment_data = []
for row in records[1:]:
    data = [float(x.strip()) for x in row.split(',')]
    ratio = data[0]/data[1]
    data.append(ratio)
    crime_employment_data.append(data)

print crime_employment_data

