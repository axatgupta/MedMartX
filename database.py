import sqlite3

conn=sqlite3.connect("creden.db")
conn.execute('CREATE table credentials(username varchar(30),passkey varchar(30), fname varchar(30),lname varchar(30) ,contact number(10),address varchar(50));')
conn.execute('insert into credentials values("akshatg@gmail.com","pass1","Akshat","Gupta",9008112345,"Block-9");')
conn.execute('insert into credentials values("yashm@gmail.com","pass2","Yash","Malkan",9008154321,"Block-14");')
conn.execute('insert into credentials values("vartikaj@gmail.com","pass3","Vartika","Jain",9008113241,"Block-13");')
conn.execute('insert into credentials values("amans@gmail.com","pass4","Aman","Sharma",9008112213,"Block-19");')
conn.execute('insert into credentials values("robbys@gmail.com","pass5","Robby","Singh",9008111221,"Block-15");')

conn.commit()

conn.close()
