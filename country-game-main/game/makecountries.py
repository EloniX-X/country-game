
import sqlite3

con = sqlite3.connect("mydb.db")
cur = con.cursor()


def makestats():
    cur.execute('drop table stats')
    cur.execute("CREATE TABLE stats(name PRIMARY KEY, bal, cities, mats, power, population, alive)")
    data = [
    #    ("Destan", 500, 1, 400, 100, 5000, 'yes'),  # Added a comma here
    #    ("Veristan", 300, 2, 400, 500, 1000, 'yes')
        ("NorthMontoro", 1000, 3, 400, 800, 898, 'yes'),
        ("WestMontoro", 1500, 5, 650, 980, 10000, 'yes')  # Added a comma here
    ]

    # Insert the data
    cur.executemany("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?)", data)  
