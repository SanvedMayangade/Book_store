from asyncio.windows_events import NULL
import sqlite3


def Create():
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

    conn.commit()
    conn.close()

def Insert(title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))

    conn.commit()
    conn.close()

def View():
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM books")

    row=curr.fetchall()
    conn.close()
    return row
    
    
def Search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    row=curr.fetchall()
    conn.close()
    return row

def Delete(id):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def Update(id,title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))    
    conn.commit()
    conn.close()


Create()
#Insert("The Moon","Jhon Sun",2008,1234978786)

#Delete()
#Update(1,"The Last Tiger","Virat Kohli",2022,1212121234)
#print(View())
#print(Search(author="Sanved"))

