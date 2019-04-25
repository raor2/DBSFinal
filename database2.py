import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Connect to database
connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()

# Option for displaying available areas
option1 = input("Would you like to see a list of available areas?\n\t1. Yes\n\t2. No\n")
print()
if int(option1) == 1:
    print("List of Eligible Areas:")
    cursor.execute("SELECT DISTINCT area FROM arealookup ORDER BY area ASC;")
    data = cursor.fetchall()
    for row in data:
        print(row[0])
    print()

# Specify area
area = input("Enter Area:\n")
print()

# Option for displaying available industries
option2 = input("Would you like to see a list of available industries?\n\t1. Yes\n\t2. No\n")
print()
if int(option2) == 1:
    print("List of Eligible Industries:")
    cursor.execute("SELECT DISTINCT naics, naicstitle FROM naicslookup ORDER BY naics ASC;")
    data = cursor.fetchall()
    for row in data:
        print("{0:<5s}   {1}".format(row[0], row[1]))
    print()

# Specify area
naics = input("Enter NAICS:\n")

# Query data with specified area
cursor.execute("SELECT DISTINCT wages.area, wages.year, naicslookup.naicstitle, wages.numestablishments, wages.avgemployment \
                FROM wages, naicslookup \
                WHERE wages.area = %s AND naicslookup.naics = %s AND wages.naics = naicslookup.naics \
                ORDER BY wages.year ASC;", [area, naics])
records = cursor.fetchall()

# Parse query result
year, title, establishment, employment = [], records[0][2], [], []
for row in records:
    year.append(int(row[1]))
    establishment.append(int(row[3]))
    employment.append(int(row[4]))
employment_per_establishment = [e1/e2 for (e1, e2) in zip(employment, establishment)]

# Normalize data for drawing
max_establishment = max(establishment)# max(establishment)/avg(crime)
establishment = [e/max_establishment for e in establishment]
max_epe = max(employment_per_establishment) * len(establishment) / sum(establishment)
employment_per_establishment = [epe/max_epe for epe in employment_per_establishment]

# Draw graph
plt.plot(year, establishment, label='Establishment Number')
plt.plot(year, employment_per_establishment, label='Employment Per Establishment')
plt.title('Employment History of {} Industry in {} Area'.format(title, area))
plt.xlabel('Year')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylabel('Index')
plt.legend()
plt.show()
