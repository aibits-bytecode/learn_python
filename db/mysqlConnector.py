import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootuser",
  database="movies"
)

myCursor = mydb.cursor()

# create database movies
# use movies;
# create table topmovies(name varchar(20), prize varchar(20));
# insert into topmovies values ("Movie1","320$"),("Movies2", "430$");

myCursor.execute("select * from topmovies")
for i in myCursor:
  print(i)

