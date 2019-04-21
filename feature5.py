import psycopg2
import psycopg2.extras

def TopCounties():
    # Check the most recent crime, employment ratio to decide the bset county to live in
    connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT a.county, b.avgcrimes, a.avgemployment, a.year \
    FROM  \
    (SELECT DISTINCT county, SUM(CAST(avgemployment as INT)) as avgEmployment, year \
    FROM arealookup LEFT JOIN wages ON arealookup.area = wages.area \
    WHERE year = '2017' \
    GROUP BY (county,year) \
    ) a , \
    (SELECT DISTINCT county, SUM(CAST(totalCrimes as INT)) as avgCrimes,year \
     FROM CountyLookup LEFT JOIN crime \
     ON CountyLookup.Agency = crime.Agency \
    WHERE year = '2017' \
    GROUP BY (county,year) \
    ) b \
    WHERE a.county = b.county \
    ORDER BY county ASC;")
    
    records = cursor.fetchall()
    
    # crime_employment_data in format: 'county' : (avg,crimes,avgemployment)
    crime_employment_data = {}
    for row in records:
        crime_employment_data[row[0]] = (float(row[1]),float(row[2]))
    
    print("BEST NY COUNTIES TO PLACE YOUR RESIDENCY IN")
    mult1 = raw_input("I. On a scale of 1-10, How much do you care about your future county's employment rate: \n")
    while not mult1.isdigit():
        mult1 = raw_input("Input must be an integer from 1 to 10, please re-enter: \n")
    
    while not ((int(mult1) > 0) and (int(mult1) < 11)):
        mult1 = raw_input("Input must be an integer from 1 to 10, please re-enter: \n")
            
    mult2 = raw_input("II. On a scale of 1-10, How much do you care about your future county's safety: \n")
    while not mult2.isdigit():
        mult2 = raw_input("Input must be an integer from 1 to 10, please re-enter: \n")
    
    while not ((int(mult2) > 0) and (int(mult2) < 11)):
        mult2 = raw_input("Input must be an integer from 1 to 10, please re-enter: \n")
    
    
    best_county = []
    for county in crime_employment_data:
        ratio = float(mult1)*crime_employment_data[county][1]/10 + (1-float(mult2))*crime_employment_data[county][1]/10
        best_county.append((county, 2*ratio/(crime_employment_data[county][1] + crime_employment_data[county][0])))
    
    best_county = sorted(best_county, key = lambda x: x[1], reverse = True)
    
    print("")
    print("=============================================")
    print("TOP 10 NY COUNTIES TO PLACE YOUR RESIDENCY IN")
    print("=============================================")
    i = 1
    for i in range(1,10):
        print(i, best_county[i-1][0])
        i += 1




    