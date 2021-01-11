from cs50 import SQL
from sys import argv
import csv

if len(argv) != 2:
    print("Please read documents to follow the format of program")
    exit(0)

db = SQL("sqlite:///students.db")

with open(argv[1],"r") as students:

    reader = csv.DictReader(students)

    for row in reader:

        current_name = row["name"].split()

        house = row["house"]
        birth = row["birth"]

        if len(current_name) == 3:
            first, middle,last =current_name
        else:
            first,last =current_name
            middle =None

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?,?)", first, middle,last,house,birth)