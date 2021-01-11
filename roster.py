from cs50 import SQL
from sys import argv
import csv

if len(argv) != 2:
    print("Please read documents to follow the format of program")
    exit(0)

db = SQL("sqlite:///students.db")

rows = db.execute("SELECT * FROM students WHERE house = ? GROUP BY last,first", argv[-1])

for row in rows:

    print(row["first"]+ " ", end="")

    if row["middle"] != None:

        print(row["middle"] + " ", end="")

    print(row["last"] + ", born "+str(row["birth"]))




