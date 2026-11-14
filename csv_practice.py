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