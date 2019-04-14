import psycopg2
import psycopg2.extras


connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
conn = psycopg2.connect(connection_string)

def crimeDataLookup():
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    locationChoice = input("Enter a selection:\n\t1. Search By Area\n\t2. Search By County\n")
    
    yearChoice = input("Get data for a specific year?\n\t1. Yes\n\t2. No\n")






crimeDataLookup()
