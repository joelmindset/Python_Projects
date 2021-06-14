import sqlite3

conn = sqlite3.connect('db_sub.db')
#create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Files TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('db_sub.db')
#insert our text files into col_Files and print them
filelist = ('information.docx', 'Hello.txt', 'myImage.png', \
        'myMove.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
for x in filelist:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_filelist(col_Files) VALUES (?)", (x,))
            print(x)
   
    conn.commit()
conn.close()

conn = sqlite3.connect ('db_sub.db')
#select txt files
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_Files FROM tbl_fileList WHERE col_Files LIKE '%.txt'")
    varText = cur.fetchall()
    print(varText)
    conn.commit()
conn.close()