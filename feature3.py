import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Connect to database
connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()

# Option for choosing area or county
option1 = input("Enter a selection:\n\t1. Search By Area\n\t2. Search By County\n")
print()
if int(option1) == 1:
    # Option for displaying available areas
    option2 = input("Would you like to see a list of available areas?\n\t1. Yes\n\t2. No\n")
    print()
    if int(option2) == 1:
        print("List of Eligible Areas:")
        cursor.execute("SELECT DISTINCT area FROM arealookup ORDER BY area ASC;")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print()

    # Specify area
    area = input("Enter Area:\n")

    # Query data with specified area
    cursor.execute("SELECT DISTINCT lookup.area, crime.year, sum(crime.totalcrimes::INT) AS totalcrimes \
                    FROM (SELECT DISTINCT arealookup.area, countylookup.agency \
                          FROM arealookup, countylookup \
                          WHERE arealookup.area = %s AND arealookup.county = countylookup.county) AS lookup, crime \
                    WHERE lookup.agency = crime.agency AND crime.agency <> 'County Total' AND crime.totalcrimes <> '' AND lookup.area <> '' \
                    GROUP BY lookup.area, crime.year \
                    ORDER BY crime.year ASC;", [area])
    records = cursor.fetchall()

    # Parse query result
    year, crime = [], []
    for row in records:
        year.append(int(row[1]))
        crime.append(int(row[2]))

    # Draw graph
    plt.plot(year, crime)
    plt.title('Crime Rate History of {} Area'.format(area))
    plt.xlabel('Year')
    plt.ylabel('Total Number of Crimes Reported')
    plt.show()
elif int(option1) == 2:
    # Option for displaying available counties
    option2 = input("Would you like to see a list of available counties?\n\t1. Yes\n\t2. No\n")
    print()
    if int(option2) == 1:
        print("List of Eligible Counties:")
        cursor.execute("SELECT DISTINCT county from countylookup ORDER BY county ASC;")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print()

    # Specify county
    county = input("Enter County:\n")

    # Query data with specified county
    cursor.execute("SELECT DISTINCT countylookup.county, crime.year, sum(crime.totalcrimes::INT) AS totalcrimes \
                    FROM countylookup, crime \
                    WHERE countylookup.county = %s AND countylookup.agency = crime.agency AND crime.agency <> 'County Total' AND crime.totalcrimes <> '' \
                    GROUP BY countylookup.county, crime.year \
                    ORDER BY crime.year ASC;", [county])
    records = cursor.fetchall()

    # Parse query result
    year, crime = [], []
    for row in records:
        year.append(int(row[1]))
        crime.append(int(row[2]))
    
    # Draw graph
    plt.plot(year, crime)
    plt.title('Crime Rate History of {} County'.format(county))
    plt.xlabel('Year')
    plt.ylabel('Total Number of Crimes Reported')
    plt.show()
else:
    print("Invalid option\n")
