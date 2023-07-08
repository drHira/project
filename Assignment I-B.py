#Assignment no. 1-A

Student_name = input("Enter Student Name: ")
Roll_number =  int (input ("Enter Roll number: "))
Standard = int (input ("Enter Standard: "))   
English = int (input ("Enter English Marks: ")) 
Math = int (input ("Enter Math Marks: ")) 
Islamiat = int (input ("Enter Islamiat: ")) 
Marks_Obtained = English + Math + Islamiat
print (Marks_Obtained)
Total_Marks = 300
perc = (Marks_Obtained / Total_Marks)*100
print (perc)
if perc <=100 and perc >= 90:
    print("Grade: A+")
elif perc <=90 and perc >=80:
    print("Grade: A")
elif perc <=80 and perc >=70:
    print("Grade: B+")
elif perc <=70 and perc >=60:
    print("Grade: B")
elif perc <= 60 and perc >=50:
    print("Grade: C+")
elif perc <=50 and perc >=40:
    print("Grade:D (Fail)")
elif perc <100 or perc > 50:
    print ("Put the correct grade")
else:
    print ("Result: Fail")


#Assignment No. 1-B

# Write a python program to print the following string in a spexcific format.
print ("Twinkle, Twinkle, Little star\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, Twinkle, Little star\n\tHow I wonder what you are ")


#Write a python program to get the python version you are using.

import sys
print("System Version")
print (sys.version)
print ("version info")
print (sys.version_info)

#Write a python program to display the current date and time.

import datetime
current_datetime = datetime.datetime.now()
print (current_datetime)

#Write a python program which accept the radius of a circle from the user and compute the area.

rad = int(input("Enter radius of a circle: "))
print (rad)
Area = 3.14*rad*rad
print (Area)

rad = float(input("Enter radius of a circle: "))
print (rad)
Area = 3.14*rad*rad
print (Area)

#write a python program which accept the user's forst and last name and print them in reverse order with a space between them.

First_Name = input("Enter First_Name: ")
Last_Name = input("Enter Last_Name: ")
print (Last_Name +" "+ First_Name)

#Write a python program which tskes two inputs from user and print them addition

num_1 = int(input("Enter num_1: "))
num_2 = int(input("ENter num_2: "))
sum = num_1 + num_2
print ("the sum of two numbers is:" ,sum)


#Write a program ehich takes five input from user for different subject's makrs, total it and genrate marksheet using grades.

Student_name = input("Enter Student Name: ")
Roll_number =  int (input ("Enter Roll number: "))
Standard = int (input ("Enter Standard: "))   
English = int (input ("Enter English Marks: ")) 
Math = int (input ("Enter Math Marks: ")) 
Islamiat = int (input ("Enter Islamiat Mark: ")) 
Biology = int(input("Enter Biology Marks: "))
Chemistry = int(input("Enter Chemistry Marks: "))
Marks_Obtained = English + Math + Islamiat + Biology + Chemistry
print (Marks_Obtained)
Total_Marks = 500
perc = (Marks_Obtained / Total_Marks)*100
print (perc)
if perc <=100 and perc >= 90:
    print("Grade: A+")
elif perc <=90 and perc >=80:
    print("Grade: A")
elif perc <=80 and perc >=70:
    print("Grade: B+")
elif perc <=70 and perc >=60:
    print("Grade: B")
elif perc <= 60 and perc >=50:
    print("Grade: C+")
elif perc <=50 and perc >=40:
    print("Grade:D (Fail)")
elif perc <100 or perc > 50:
    print ("Put the correct grade")
else:
    print ("Result: Fail")

#Write a program which take input from user and identify that the given number is even or odd?
A = int(input("Enter the number: "))
if (A %1 ==1):
    print (A, "is even number")
else: print(A, "is odd number")
