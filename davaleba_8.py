# მაგალითი_1

import sqlite3

conn = sqlite3.connect("books_db.sqlite")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE book
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(30),
author VARCHAR(30),
release_year INT,
price INT);
""")
cursor.execute("""INSERT INTO book(title, author, release_year, price) VALUES ("დათა თუთაშხია", "ჭაბუა ამირეჯიბი", 1975, 25);""")
book_list = [
    ("დიდოსტატის კონსტანტინეს მარჯვენა", "კონსტანტინე გამსახურდია", 1939, 30),
    ("რკინის თეატრი", "ოთარ ჭილაძე", 1981, 20),
    ("Nineeteen Eighty-Four", "George Orwell", 1984, 40),
    ("The Headless Horseman", "Thomas Mayne Reid", 1865, 35)
]
cursor.executemany("INSERT INTO book(title, author, release_year, price) VALUES (?,?,?,?)", book_list)
conn.commit()
conn.close()

# მაგალითი_2

import sqlite3

conn = sqlite3.connect("titanic.sqlite")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE passenger
(id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHARE(30),
age INT,
sex VARCHAR(10),
ticket VARCHAR(30),
cabin INT);
""")
passengername = input("შეიყვანეთ მგზავრის სახელი: ")
passemgerage = int(input("შეიყვანეთ მგზავრის ასაკი: "))
passengersex = input("შეიყვანეთ მგზავრის სქესი: ")
passengerticket = input("შეიყვანეთ მგზავრის ბილეთის მარშუტი: ")
passengercabin = int(input("შეიყვანეთ მგზავრის კაბინის ნომერი: "))
cursor.execute("""INSERT INTO passenger(passenger_name, age, sex, ticket, cabin)
 VALUES (?,?,?,?,?)""", (passengername, passemgerage, passengersex, passengerticket, passengercabin))
# conn.commit()
travel = []
for i in range(1, 4):
    passengername1 = input("შეიყვანეთ მგზავრის სახელი: ")
    passemgerage2 = int(input("შეიყვანეთ მგზავრის ასაკი: "))
    passengersex3 = input("შეიყვანეთ მგზავრის სქესი: ")
    passengerticket4 = input("შეიყვანეთ მგზავრის ბილეთის მარშუტი: ")
    passengercabin5 = int(input("შეიყვანეთ მგზავრის კაბინის ნომერი: "))
    holyday = (passengername1, passemgerage2, passengersex3, passengerticket4, passengercabin5)
    travel.append(holyday)
cursor.executemany("INSERT INTO passenger(passenger_name, age, sex, ticket, cabin) VALUES (?,?,?,?,?)", travel)
conn.commit()
conn.close()

# მაგალითი_3

import sqlite3


class Movie:

    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"ფილმის სახელია: {self.title}, ჟანრი: {self.genre}, გამოშვების წელი: {self.year}, შეფასება: {self.imdb} "

    def convert(self):
        return tuple([self.title, self.genre, self.year, self.imdb])

conn = sqlite3.connect('movies.sqlite3')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE movie
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),
genre VARCHAR(50),
yearr INTEGER,
imdb  FLOAT);
''')
movie_list = []
for i in range(1, 5):
    title1 = input("შეიყვანეთ ფილმის სახელი: ")
    genre1 = input("შეიყვანეთ ფილმის ჟანრი: ")
    year1 = int(input("შეიყვანეთ ფილმის გადაღების წელი: "))
    imdb1 = float(input("შეაფასეთ ფილმი 10 ბალიანი სისტემით: "))
    obj = Movie(title1, genre1, year1, imdb1)
    movie_list.append(obj.convert())
    print(obj)
cursor.executemany("INSERT INTO movie (title, genre, yearr, imdb) VALUES (?, ?, ?, ?)", movie_list)
conn.commit()
conn.close()
