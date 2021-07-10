import sqlite3

class Database():
    def __init__(self):
        self.conn=sqlite3.connect("movies.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, name text, director text, year integer, rating integer)")
        self.conn.commit()
        

    def insert(self,name,director,year,rating):
        self.conn=sqlite3.connect("movies.db")
        self.cur=self.conn.cursor()
        self.cur.execute("INSERT INTO movie VALUES (NULL,?,?,?,?)",(name,director,year,rating))
        self.conn.commit()
        

    def view(self):
        self.conn=sqlite3.connect("movies.db")
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT * FROM movie")
        rows=self.cur.fetchall()
        return rows

    def search(self,name="",director="",year="",rating=""):
        self.conn=sqlite3.connect("movies.db")
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT * FROM movie WHERE name=? OR director=? OR year=? OR rating=?", (name,director,year,rating))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.conn=sqlite3.connect("movies.db")
        self.cur=self.conn.cursor()
        self.cur.execute("DELETE FROM movie WHERE id=?",(id,))
        self.conn.commit()
        

    def update(self,id,name,director,year,rating):
        self.conn=sqlite3.connect("movies.db")
        self.cur=self.conn.cursor()
        self.cur.execute("UPDATE movie SET name=?, director=?, year=?, rating=? WHERE id=?",(name,director,year,rating,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()    
       
