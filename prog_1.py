import os
import sys

list1 = []
list2 = []
list3 = []
string1 = input("Enter the first list:")
string2 = input("Enter the second list:")

list1 = string1.split(",")
list2 = string2.split(",")

for x in list1:
    for y in list2:
        if(x==y):
            if(x.isdigit() == True):
                list3.append(x)

for item in list3:
    print(item)


