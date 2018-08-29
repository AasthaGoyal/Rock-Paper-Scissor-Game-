import os
import sys
import re

#mylist = []
count =0
try_count = 1
mylist= input("Enter the password:")
count = len(mylist)

if (try_count<=7):
    if(count>=5 and count<=10):
        pass
    else:
        print("The password should have minimum 5 characters and maximum 10 characters")

    #phrase = string.split(" ")
    #mylist.append(phrase)
    if re.search("[a-z]", mylist):
        pass
    else:
        print("The password should have atleast one lowercase letter")

    if re.search("[A-Z]", mylist):
        pass
    else:
        print("The password should have atleast one uppercase letter")

    if re.search ("[@,$,#,&,*]", mylist):
        pass
    else:
        print("The password should have atleast one of the character from the set [@,$,#,&,*]")

    if re.search ("[1-9]", mylist):
        pass
    else:
        print("The password should have both characters and digits")

    string = input("Enter the password:")
    count = len(string)
    try_count = try_count +1

else:
    print("You have all you 7 tries")


          
    


                      
