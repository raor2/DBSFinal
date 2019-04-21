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
if(int(inp) == 1):
    print("List of Eligible Areas:\n")
    cursor.execute("SELECT DISTINCT area FROM arealookup;")
    data = cursor.fetchall()
    for row in data:
        print(row[0])

# Specify area
area = input("Enter Area:\n")

# Query data with specified area

