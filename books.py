
import sqlite3
db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()        #create cursor


if ('''EXISTS(SELECT books)'''):
    pass
else:
    cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)    
''')                    #create table 'books'
    db.commit()

id1 = 3001
title1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

id2=3002
title2="Harry Potter and the Philosophers Stone"
author2="J.K. Rowling"
qty2=40

id3=3003
title3="The Lion, the Witch, and the Wardrobe"
author3="C.S. Lewis"
qty3=25

id4=3004
title4="The Lord of the Rings"
author4="J.R.R. Tolkien"
qty4=37

id5=3005
title5="Alice in Wonderland"
author5="Lewis Carroll"
qty5=12


books_ = [(id1, title1, author1, qty1), (id2, title2, author2, qty2), (id3, title3, author3, qty3),
         (id4, title4, author4, qty4), (id5, title5, author5, qty5)]


if ('''EXISTS(SELECT books)'''):
    pass
else:
    cursor.executemany('''INSERT INTO books (id, title, author, qty)   
    VALUES(?,?,?,?)''', books_)                                     #populating the table with book data
    db.commit()



#user input to start program
start = ""
try: 
    while start != "Exit":                                      #condition to keep program running until 'exit' is entered
        start = input("What would you like to do (Enter, Update, Delete, Search, Exit)?")
        if start == "Enter":                                                #if user wants to enter, get data of new book
            id = int(input("What is the book id?"))
            title = input("What is the title?")
            author = input("Who is the author?")
            qty = int(input("What is the quanitity?"))
            
            cursor.execute('''INSERT INTO books (id, title, author, qty)
                VALUES(?,?,?,?)''', (id, title, author, qty))                   #enter new book data entered by the user
            print("The new books data was entered!")
            db.commit()
            
        elif start == "Update":                                                     #user wants to update
            id = int(input("What is the book id?"))
            info_update = input("Would you like to update title, author, or qty?")
                
            if info_update == "title":
                title_new = input("Enter the new title:")
                cursor.execute('''UPDATE books SET title = ? WHERE id = ?''', (id, title_new))           #update title 
                print("Book info successfully updated!")
                   
            elif info_update == "author":
                author_new = input("Enter the author:")
                cursor.execute('''UPDATE books SET author = ? WHERE id = ?''', (id, author_new))         #update author  
                print("Book info successfully updated!")

            else:
                qty_new = int(input("Enter the new quantity:"))
                cursor.execute('''UPDATE books SET qty = ? WHERE id = ?''', (id, qty_new))                 #update quantity
                print("Book info successfully updated!")
                
        elif start == "Delete":
            id = int(input("What is the book id?"))
            cursor.execute('''DELETE FROM books WHERE id = ?''', (id,))                                     #delete book
            print("Book successfully deleted!")

        elif start == "Search":
            id = int(input("What is the book id?"))
            cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))                                     #search for books
            bookFind = cursor.fetchone()
            print("The book you were looking for is: " + str(bookFind))

    if start == "Exit":                                                   #exit program
        print("Have a nice day!")  
            
except:
    print("Oops! An error occured!")
    
        





 


