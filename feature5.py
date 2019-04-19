import psycopg2
import psycopg2.extras
#from decimal import Decimal


connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()
cursor.execute("SELECT w.avgEmployment, c.totalCrimes, cl.County \
               FROM Wages w, Crime c, CountyLookup cl,AreaLookup al \
               WHERE c.Agency = cl.Agency AND cl.County = al.County \
                   AND w.Year = c.Year AND w.Year = 2017 AND c.Year = 2017 AND c.totalCrimes <> '' \
               LIMIT 100;")

records = cursor.fetchall()


crime_employment_data = []
for row in records:
    #ratio = float(row[0])/float(row[1])
    #crime_employment_data.append((float(row[0]),float(row[1]),ratio))
    crime_employment_data.append((float(row[0]),float(row[1]),row[2]))

