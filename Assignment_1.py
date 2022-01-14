#Q1.Program  to find average of three numbers entered by user
print("_________Program 1_________\n")
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))

#formula for finding average
avg = (num1+num2+num3)/3 

print("The avg of",num1,",",num2,"and",num3,"is",avg) 


#Q2.Program to compute person's Income Tax
print("_________Program 2_________\n")

Gross_Inc  = int(input("Enter your Gross Income : "))
Depndt = int(input("Enter No. of Dependents : "))

'''Standard deduction is $10,000
Dependent deduction per head is $3000'''

Taxable_Inc = (Gross_Inc - 10000)-(30000*Depndt) #Formula for calculating taxable income

if Taxable_Inc>0:
    print("Your Taxable income is : ",Taxable_Inc)
    Tax = (Taxable_Inc*20)/100
    print("And payable tax is : " ,Tax)

else:
    print("You don't have to pay income tax. \n Thank You")

#Q3.Program to store different data type vales into a list.
print("_________Program 3_________\n")

student_lst=[]

n=int(input('Enter the number of students in class: '))

for i in range(n):
    sid=int(input('\nStudent ID: '))
    name=input("Student's Name: ")
    gender=input("Student's Gender\n[Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).]: ")
    course=input("Student's course: ")
    cgpa=float(input("Student's CGPA: "))

    student=[sid,name,gender,course,cgpa]

    student_lst=student_lst+[student]
print('\n\nStudent List:-\n',student_lst)

#Q4. Program to enter marks of 5 student and display it in sorted manner
print("_________Program 4_________\n")
lst=[]

for i in range(5):
    marks=input("Student marks: ")
    lst.append(marks)
lst.sort()
print("\nSorted List Of Student marks:-",lst,sep='\n')

#5a. Write a Python program to print a specified list after removing 4th element.
print("_________Program 5_________\n")
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("a.\n",color)

#5b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.Do that in one line code.
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print("\nb.\n",color)

