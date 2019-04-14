import psycopg2
import psycopg2.extras


connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string)
crimes = ['murdercrimes', 'rapecrimes', 'robberycrimes', 'aggravatedassaultcrimes', 'burgalarycrimes', 'larcenycrimes']



def crimeDataLookup():
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    locationChoice = input("Enter a selection:\n\t1. Search By Area\n\t2. Search By County\n")
    
    yearChoice = input("Get data for a specific year?\n\t1. Yes\n\t2. No\n")
    year = ''
    if(int(yearChoice) == 1):
        year = input("Enter desired year:\n")


    if(int(locationChoice) == 1):
        area = input("Enter Area:\n")
        crime = crimes[int(input("Select type of crime:\n\t1. Murder\n\t2. Rape\n\t3. Robbery\n\t4. Aggravated Assault\n\t5. Burgalary\n\t6. Larceny\n")) - 1]
        print("You've selected " + crime)
        


    elif(int(locationChoice) == 2):
        county = input("Enter County:\n")
        crime = crimes[int(input("Select type of crime:\n\t1. Murder\n\t2. Rape\n\t3. Robbery\n\t4. Aggravated Assault\n\t5. Burgalary\n\t6. Larceny\n")) - 1]

    else:
        print("Invalid option\n")





crimeDataLookup()
