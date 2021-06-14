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
#insert our text files into col_Files
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO  tbl_fileList(col_Files) VALUES(?)" , \
            ('information.docx',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES(?)", \
            ('Hello.txt',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES(?)", \
            ('myImage.png',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES(?)", \
            ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES(?)", \
            ('World.txt',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES(?)", \
            ('data.pdf',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES(?)", \
        ('myPhoto.jpg',))
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