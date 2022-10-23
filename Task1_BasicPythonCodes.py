
# IF STATEMENT CONDITION
midterm = float(input("Enter the midterm exam grade please : "))
final = float(input("Enter the final exam grade please "))

student_grade = midterm*0.4 + final*0.6

if(student_grade>=85 and student_grade<= 100):
    print(student_grade , "The grade annotation of the student is : AA")
elif(student_grade>=75 and student_grade<85):
    print(student_grade, "The grade annotation of the student is : AB")
elif(student_grade>=60 and student_grade<75):
    print(student_grade, "The grade annotation of the student is : BB")
elif (student_grade >= 50 and student_grade < 60):
    print(student_grade, "The grade annotation of the student is : CC")
else :
    print(student_grade , "Sorry ! The Student failed ")

# FOR STATEMENT

student_grades = [50,60,70,100,22,45,73,85]
student_numbers = len(student_grades)
sum = 0
for n in student_grades:
    sum+=n
    avg = sum/student_numbers
print("The average of class of {} people is : {}" .format(student_numbers,avg))


# # WHILE CONDITION
#
# #print all students' grade one by one by while loop

i=0
while(i!=len(student_grades)):
    print(student_grades[i])
    i+=1

def factorialOfNumber(num):
    f = 1
    for n in range(1,num+1):
       f = f * n
    return f

print("The factorial of the entered number is : ",factorialOfNumber(5))

# let's create an array and add numbers to and have the average of the entered numbers .

n = int(input("How many numbers do you like to enter :"))
my_numbers = []
for i in range(0,n):
    element = int(input("Enter the element of the array please : "))
    my_numbers.append(element)
avg = sum(my_numbers)/n
print("Hers is the average of all entered numbers : " ,avg)











