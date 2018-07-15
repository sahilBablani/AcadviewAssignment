import pymysql as pm

con= pm.connect(host='localhost', database='sahil', user='root',password='India@123',port=3304)
cur_obj=con.cursor()
cur_obj.execute("CREATE TABLE IF NOT EXISTS "
                    "book (id integer PRIMARY KEY, "
                            "title text, "
                            "author text, "
                            "year integer, "
                            "isbn integer)")
                             
con.commit()
con.close()

def insert(title, author, year, isbn):
    con= pm.connect(host='localhost', database='sahil', user='root',password='India@123',port=3304)
    cur_obj = con.cursor()
    cur_obj.execute("INSERT INTO book "
                    "VALUES (NULL, {}, {}, {}, {})".format(title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con= pm.connect(host='localhost', database='sahil', user='root',password='India@123',port=3304)
    cur_obj = con.cursor()
    cur_obj.execute("SELECT * FROM book")
    rows = cur_obj.fetchall()
    con.close()
    return rows

def update(id, title, author, year, isbn):
    con= pm.connect(host='localhost', database='sahil', user='root',password='India@123',port=3304)
    cur_obj = con.cursor()
    cur_obj.execute("UPDATE book "
                    "SET title = {}, "
                    "author = {}, "
                    "year = {}, "
                    "isbn = {} "
                    "WHERE id = {}".format(title, author, year, isbn, id)) 
                    
    con.commit()
    con.close()

def delete(id):
    con= pm.connect(host='localhost', database='sahil', user='root',password='India@123',port=3304)
    cur_obj = con.cursor()
    cur_obj.execute("DELETE FROM book "
                    "WHERE id = {}".format(id))
    con.commit()
    con.close()

def search(title = "", author = "", year = "", isbn = ""):
    con= pm.connect(host='localhost', database='sahil', user='root',password='India@123',port=3304)
    cur_obj = con.cursor()
    cur_obj.execute("SELECT * "
                    "FROM book "
                    "WHERE title = {} OR author = {} OR year = {} OR isbn = {}".format(title, author, year, isbn)) 
                    
    rows = cur_obj.fetchall()
    con.close()
    return rows





