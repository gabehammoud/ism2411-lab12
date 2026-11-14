# lab 12

# reflection
# 1.
# Python makes it easier to automate repetitive data cleaning and reporting
# tasks, especially with large datasets. Excel is better for quickly viewing
# data and making changes manually.

# 2.
# A restaurant could use an append-mode log to record daily sales totals.
# Append mode would be useful because it keeps previous records while
# adding new ones without overwriting them.

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

# exercise 4

print("\nExercise 4:")
total_revenue = 0
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total Revenue: ${total_revenue:.2f}")

# exercise 5 

print("\nExercise 5:")
original_count = 0
cleaned_count = 0
with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)
    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])
        for row in reader:
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity
            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                cleaned_count += 1
print("Original rows:", original_count)
print("Cleaned rows:", cleaned_count)

# exercise 6

print("\nExercise 6:")
# csv.reader is useful for simple files where column positions are known.
# DictReader is better when accessing columns by name instead of index.
dict_total_revenue = 0
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total Revenue: ${dict_total_revenue:.2f}")

# exercise 7 

print("\nExercise 7:")
product_summary = {}
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        product_summary[product] = product_summary.get(product, 0) + total
for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")

# exercise 8 

print("\nExercise 8:")
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as file:
    file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")
print("Sales revenue logged successfully.")