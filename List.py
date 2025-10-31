#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 12:13:17 2025

@author: aakash-tiwari
"""

ages = [1,12,5,87,5,6,9,25,31,12,87,45,36,25,9,8,4,5,12]
print(ages)

print("the length of the list is:", len(ages))

ages.append(15)
print(ages)
print("the new length of the list is:", len(ages))

ages.insert(1, 18)
print(ages)
print("the new length of the list is:", len(ages))

print("the item at the 5th index is:", ages[5])
print("The items at the end of the list is:", ages[len(ages) - 1])

print("The number of times 12 appear in the list is:", ages.count(12))

ages.sort()
print("The sorted list: ")
print(ages)

print("The list is descending order: ")
ages.reverse()
print(ages)


print("------------------------------------------------------------")


students = ["Rajesh", "Kamal", "Yash", "Suresh"]
print(students)

for item in students:
    print(item)
    
print("-----------------------------")
for i in range(len(students)):
    print(students[i])
    
print("The Sorted Student List is: ")
students.sort()
print(students)

print("Slicing the students from 1 to 3")
print(students[1:4])

print("Printing the whole list through slicing:")
print(students[:])

print("The students from 2nd Index are: ")
print(students[2:])

print("The first 3 students are: ")
print(students[:3])


# The default start value is 0 and the default end value is len(list)

