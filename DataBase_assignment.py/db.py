import sqlite3

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test1.db')

#tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#loop through each tuple to find files with file extension '.txt'
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one file out of the tuple
        # therefore (x, ) will denote a one-elemnt tuple for files
        # ending in '.txt'
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (x, ))
conn.close()
