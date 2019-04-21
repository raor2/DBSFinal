import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string)
crimes = ['murdercrimes', 'rapecrimes', 'robberycrimes', 'aggravatedassaultcrimes', 'burgalarycrimes', 'larcenycrimes']


def crimeDataLookup():
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    locationChoice = input("Enter a selection:\n\t1. Search By Area\n\t2. Search By County\n")

    if(int(locationChoice) == 1):
        inp = input("Would you like to see a list of available areas?\n\t1. Yes\n\t2. No\n")
        if(int(inp) == 1):
            print("List of Eligible Areas:\n")
            dict_cur.execute("SELECT DISTINCT area from arealookup;")
            data = dict_cur.fetchall()
            for row in data:
                print(row[0])

        area = input("Enter Area:\n")
        crime = crimes[int(input("Select type of crime:\n\t1. Murder\n\t2. Rape\n\t3. Robbery\n\t4. Aggravated Assault\n\t5. Burgalary\n\t6. Larceny\n")) - 1]
        #print("You've selected " + crime)
        q = "SELECT DISTINCT foo.area ,year, sum(CAST("+ crime + " AS INT)) as "+crime+" FROM (SELECT DISTINCT area, agency FROM arealookup LEFT JOIN countylookup on arealookup.county = countylookup.county WHERE area = '"+area+"' AND area <> ' ' ORDER BY agency) as foo  RIGHT JOIN crime ON crime.agency = foo.agency WHERE crime.agency <> 'County Total' AND "+crime+" <> '' AND area <> ''GROUP BY (foo.area, year) ORDER BY year ASC;"
        dict_cur.execute(q)
        data = dict_cur.fetchall()
        print("\nData for "+area+":\n\nYear\tAmount\n")
        for row in data:
            print(str(row[1]) + "\t" + str(row[2]))
        c = input("Would you like to graph this data?\n\t1. Yes\n\t2. No\n")
        if(int(c) == 1):
            xvals = []
            yvals = []
            for row in data:
                #print("Appending Data...")
                xvals.append(row[1])
                yvals.append(row[2])

            #print("Generating Plot...")
            plt.plot(xvals, yvals, label='Crime Data Bsed on Area')
            #plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])



    elif(int(locationChoice) == 2):
        inp = input("Would you like to see a list of available counties?\n\t1. Yes\n\t2. No\n")
        if(int(inp) == 1):
            print("List of Eligible Counties:\n")
            dict_cur.execute("SELECT DISTINCT county from countylookup;")
            data = dict_cur.fetchall()
            for row in data:
                print(row[0])
        county = input("Enter County:\n")
        crime = crimes[int(input("Select type of crime:\n\t1. Murder\n\t2. Rape\n\t3. Robbery\n\t4. Aggravated Assault\n\t5. Burgalary\n\t6. Larceny\n")) - 1]
        q = "SELECT DISTINCT county, year, sum(CAST("+crime+" AS INT)) as "+crime+" FROM countylookup RIGHT JOIN crime ON crime.agency = countylookup.agency WHERE countylookup.county = '"+county+"' AND crime.agency <> 'County Total' AND larcenycrimes <> '' GROUP BY (county,year) ORDER BY year ASC;"
        dict_cur.execute(q)
        data = dict_cur.fetchall()
        print("Data for "+county+" County:\n\nYear\tAmount\n")
        for row in data:
            print(str(row[1]) + "\t" + str(row[2]))


        c = input("Would you like to graph this data?\n\t1. Yes\n\t2. No\n")
        if(int(c) == 1):
            xvals = []
            yvals = []
            for row in data:
                #print("Appending Data...")
                xvals.append(row[1])
                yvals.append(row[2])

            #print("Generating Plot...")
            plt.plot(xvals, yvals, label='Crime Data Based on County')
    else:
        print("Invalid option\n")





crimeDataLookup()
