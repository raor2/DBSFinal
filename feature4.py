import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Connect to database
connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()

# Option for display available areas
inp = input("Would you like to see a list of available areas?\n\t1. Yes\n\t2. No\n")
print()
if(int(inp) == 1):
    print("List of Eligible Areas:")
    cursor.execute("SELECT DISTINCT area FROM arealookup ORDER BY area ASC;")
    data = cursor.fetchall()
    for row in data:
        print(row[0])
    print()

# Specify area
area = input("Enter Area:\n")

'''
    Problem 2: Empty row of totalcrime means 0
'''
# Query data with specified area
cursor.execute("SELECT crimes.area, crimes.year, crimes.totalcrimes, wages.numestablishments, wages.avgemployment \
                FROM (SELECT DISTINCT lookup.area, crime.year, sum(crime.totalcrimes::INT) AS totalcrimes \
                      FROM (SELECT DISTINCT arealookup.area, countylookup.agency \
                            FROM arealookup, countylookup \
                            WHERE arealookup.area = %s AND arealookup.county = countylookup.county) AS lookup, crime \
                      WHERE lookup.agency = crime.agency AND crime.agency <> 'County Total' AND crime.totalcrimes <> '' AND lookup.area <> '' \
                      GROUP BY lookup.area, crime.year) AS crimes, wages \
                WHERE crimes.area = wages.area AND crimes.year = wages.year AND wages.naics = '0' \
                ORDER BY crimes.year ASC;", [area])
records = cursor.fetchall()

# Parse query result
year, crime, establishment, employment = [], [], [], []
for row in records:
    year.append(int(row[1]))
    crime.append(int(row[2]))
    establishment.append(int(row[3]))
    employment.append(int(row[4]))
employment_per_establishment = [e1/e2 for (e1, e2) in zip(employment, establishment)]

# Normalize data for drawing
max_crime = max(crime)
crime = [c/max_crime for c in crime]
max_establishment = max(establishment) * len(crime) / sum(crime) # max(establishment)/avg(crime)
establishment = [e/max_establishment for e in establishment]
max_epe = max(employment_per_establishment) * len(crime) / sum(crime)
employment_per_establishment = [epe/max_epe for epe in employment_per_establishment]

# Draw graph
plt.plot(year, crime, label='Crime Rate')
plt.plot(year, establishment, label='Establishment Number')
plt.plot(year, employment_per_establishment, label='Employment Per Establishment')
plt.title('Crime Rate vs. Employment Index')
plt.xlabel('Year')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylabel('Index')
plt.legend()
plt.show()
