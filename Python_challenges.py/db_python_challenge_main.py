
import sqlite3

conn = sqlite3.connect('roster.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_roster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        FirstName TEXT, \
        Species TEXT, \
        IQ INT \
        )")
    conn.commit()

    
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_roster(FirstName, Species, IQ) VALUES (?,?,?)", \
                ('Jean-Baptiste Zorg', 'Human', '122'))
    cur.execute("INSERT INTO tbl_roster(FirstName, Species, IQ) VALUES (?,?,?)", \
                ('Korben Dallas', 'Meat Ppsicle', '100')), \
    cur.execute("INSERT INTO tbl_roster(FirstName, Species, IQ) VALUES (?,?,?)", \
                ('Ak\'not', 'Mangalore', '-5'))


    conn.commit()
conn.close()


conn = sqlite3.connect('roster.db')

    






    
    
    
