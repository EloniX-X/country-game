
import sqlite3


#stats
#-name
#-bal
#-cities
#-mats
#-power
#-population
#diplo
#-wars
#-allies



con = sqlite3.connect("mydb.db")
cur = con.cursor()


def takeval(cont, val, setval):
    "set countrys value to new value"

def gettxt(getwhat, cont):
    con = sqlite3.connect("mydb.db")
    query = f"SELECT {getwhat} FROM stats WHERE name = ?"
    cur.execute(query, (cont,))
    
    fetched = cur.fetchone()
    
    con.close()
    
    
def getstats(getwhat, cont):
    con = sqlite3.connect("mydb.db")
    query = f"SELECT {getwhat} FROM stats WHERE name = ?"
    cur.execute(query, (cont,))
    
    fetched = cur.fetchone()
    
    con.close()
    
    if fetched is not None:
        return int(fetched[0])
    else:
        return None




def makestats():
    cur.execute('drop table stats')
    cur.execute("CREATE TABLE stats(name PRIMARY KEY, bal, cities, mats, power, population, alive)")
    data = [
        ("Destan", 500, 1, 400, 100, 5000, 'yes'),  # Added a comma here
        ("Veristan", 300, 2, 400, 500, 1000, 'yes')  # Added a comma here
    ]

    # Insert the data
    cur.executemany("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?)", data)  # Fixed the number of placeholders

    # Commit changes
    con.commit()
    f = open("game/turn.txt", 'r+')
    f.truncate(0)
    f.write('0')


def getturn():
    f = open("game/turn.txt", 'r+')
    content = f.readlines()
    for line in content:
        
        for i in line:
            
            # Checking for the digit in
            # the string
            if i.isdigit() == True:
                
                curturn = int(i)
                next_turn = curturn + 1
                print("The previous turn was: ",curturn)
                print("The current turn is: ", next_turn)
                next = int(next_turn)
                f.truncate(0)
                f.write(str(next))



def updateint(whatcol, whatint, cont):

   # run = cur.execute("UPDATE stats set "+whatcol+" = "+whatint+" WHERE name = "+cont)
    query = f"UPDATE stats SET {whatcol} = ? WHERE name = ?"
    cur.execute(query, (whatint, cont))
   # run
    con.commit()

    print("gotten")



#Destan
#Veristan
    
#updateint('wars','Veristan','Destan')

#-----------PT 2-------------

