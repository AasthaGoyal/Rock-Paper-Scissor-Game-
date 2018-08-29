import os
import sys

def sort_list (mylist1, mylist2):
  
    for i in mylist2:
        for j in mylist2:
            if(i>j):
                temp = i
                i=j
                j=temp
                print(mylist2[i])
                for x in mylist1:
                    for y in mylist1:
                        temp=x
                        x=y
                        y=temp
                        print(mylist1)
        

    for item in mylist1:
        print(str(item))

mylist1 = []
mylist2 = []
#mylist3 = [] # sorted list of stars
#mylist4 = [] # final list of hotel names
string1 = input("Enter a list of Hotel Names:")
string2 = input("Enter a list of corresponding number of stars:")
phrase1 = string1.split(",")
phrase2 = string2.split(",")
mylist1.append(phrase1)
#mylist2.append(phrase2)
for item in phrase2:
     mylist2.append(int(item))
sort_list (mylist1,mylist2)
    



                        
