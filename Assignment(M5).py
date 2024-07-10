import sqlite3
library=sqlite3.connect('bookstore.db')
bookcursor=library.cursor()

#creating a table
bookcursor.execute('''CREATE TABLE books (BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (20) NOT NULL,
    author TEXT,
    price FLOAT);''')

#inserting record to database
bookcursor.execute("INSERT INTO books (BookID, name, author, price) VALUES (2,'Think Python','Allen B. Drowney',475.0);")
library.commit()

#retrieving record from database
title=input("Book Title: ")
sql="SELECT * from books WHERE name='"+title+"';"
bookcursor.execute(sql)
record1=bookcursor.fetchone()
print(record1)

price="SELECT price from books WHERE name='"+title+"';"
bookcursor.execute(price)
record2=bookcursor.fetchone()

qty=int(input("No. of copies: "))

anything_else=input("Add more books? (Y/N)")
if (anything_else=="Y" or anything_else=="y"):
    library.rollback()
else:
    total_cost = qty*record2[0]
    print(total_cost)
    
