# lab 12

import csv

# exercise 1

# sales.csv is stored in the data folder.

# exercise 2 

print("Exercise 2:")
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# exercise 3

print("\nExercise 3:")
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)