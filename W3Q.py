#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 11:53:33 2025

@author: aakash-tiwari
"""

"""
lst = []
lst.append("Anya")
print(lst)

lst = ["Ravi", "Tina", "Aman"]
print(lst[0])
lst.remove("Tina")
print(lst)

students = ["Ravi", "Tina", "Aman"]
students[0] = "Rajendra"
print(students)

students = ["Ravi", "Tina", "Aman"]
students[0:1] = ["Ravindra"]
print(students)

students = ["Ravi", "Tina", "Aman"]

students[0:1] = "Rajendra"
print(students)

list1 = ["Ravi", "Anya"]
list2 = ["Tina"]

print(list1+list2)

print(["Aman"] * 3)

students = ["Ravi", "Anya", "Tina", "Aman", "Neha"]
print(students[1:4])

print(students[-2:])

print(students[::2])
"""

"""
submissions = ["Ravi", "Tina"]
backup = submissions # created a reference, not a real copy. # backup and submissions point to the same list in memory
submissions.append("Aman")
print(submissions)
print(backup)


submissions = ["Ravi", "Tina", "Aman"]
backup = submissions[:] # Slicing created a new list with separate memory.
submissions[0] = "Neha"
print(submissions)
print(backup)

submissions = [["Ravi", "PDF"], ["Tina", "DOC"]]
backup = submissions #Changing the submissions list also changes the backup. # The backup list changed because backup and submissions both point to the same list in memory.
submissions[0][1] = "zip"
print(submissions)
print(backup)

submissions = [["Ravi", "PDF"], ["Tina", "DOC"]]
backup = submissions[:] #  Slicing didn't protect inner lists from being shared. # Only the outer list was copied, not the inner lists. # The backup also shows "ZIP" instead of "DOC".
submissions[1][1] = "ZIP"
print(submissions)
print(backup)

submissions = ["Ravi", "Tina"]
backup=submissions[:]
backup.append(("Neha"))
print(submissions)
print(backup)


inner = ["Ravi"]
submissions = [inner, inner]
submissions[0].append("PDF")
print(submissions)

submissions = ["Ravi"]
backup = submissions
backup[0] = "Neha"
print(submissions)
print(backup)

submissions = ["Ravi", "Tina", "Aman"]
backup=submissions[2:1]
print(submissions)
print(backup)

submissions = ["Ravi", "Tina"]
backup = submissions
backup = ["Aman"]
print(submissions)
print(backup)

group1 = [["Ravi"], ["Tina"]]
group2 = group1[:]
group1.append("Submitted")
print(group2[0])
"""

"""

# Smart Canteen 2.0 — Built with Python iterator functions

# ----------------------------
# 1. Nishanur: The Pairing Expert (zip)
# ----------------------------
names = ["Ravi", "Anya", "Kabir", "Meera", "Arjun"]
meals = ["Idli", "Chicken Curry", "Burger", "Fish fry", "Paneer Tikka"]

paired_orders = list(zip(names, meals))

for name, meal in paired_orders:
    print(f"{name} ordered {meal}")
print()
    
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
print()
    
prices = [50, 40, 120, 80, 150]

final_price = list(map(lambda price: price*1.18, prices))    
for meal, price in zip(meals, final_price):
    print(f"{meal}: ${price}")
print()
    
all_meals = ["Idli", "Poha", "Burger", "Salad", "Paneer Tikka", "Chicken Curry", "Fish Fry"]
veg_items = ["Idli", "Poha", "Salad", "Paneer Tikka"]

veg_meals = list(filter(lambda meal: meal in veg_items, all_meals))

for meal in veg_meals:
    print(f"{meal}")
print()
"""

"""
names = ["Ravi", "Anya", "Sita"]
meals = ["Idli", "Poha", "Dosa"]
pairs = zip(names, meals)
names[0] = "Amit"
print(list(pairs))
"""

"""
data = ["Idli", "Dosa", "Poha"]
for i, item in enumerate(data):
    data[i] = item.upper()
print(data)
"""

"""
prices = [100, 200]
updated_prices = list(map(lambda price: price*1.18, prices))
prices[1] = 300
print(updated_prices)
"""

"""
meals = ["Idli", "Poha", "Chicken"]
veg_items = ["Idli", "Poha", "Paneer"]
result = filter(lambda x: x not in veg_items, meals)
print(result) 
print(list(result))
print(len(list(result)))
"""       

"""
meal_prices = [100, 150, 200]
gst_func = lambda x: x*1.18
new_prices = list(map(gst_func, meal_prices[:2]))
meal_prices[1] = 300
print(new_prices)
"""

"""
data = [10, 20, 30]
for i, val in enumerate(data):
    val = val + 5
print(data)
"""

"""
items = ["a", "b", "c"]
result = list(map(lambda x: x+'1', items))
print("".join(result))
"""