# 1] Check if a number is positive, negative, or zero.


number = int(input("Enter the number:"))

if number==0:
    print("Number is Zero")

elif number>0:
    print("Number is Positive")

else :
    print("Number is Negative")



# 2] Check whether a number is even or odd.


number = int(input("Enter the number:"))

if number%2==0:
    print("Number is Even")

else :
    print("Number is Odd")



# 3] Find the greater of two numbers.


number1 = int(input("Enter the number1:"))
number2 = int(input("Enter the Number2:"))

if number1>number2:
    print("Number1 is Greatest")

elif number1<number2:
    print("Number2 is Greatest")

else :
    print("Number is Equal")   


# 4] Find the greatest of three numbers.


number1 = int(input("Enter the number1:"))
number2 = int(input("Enter the Number2:"))
number3 = int(input("Enter the Number3:"))

if number1>number2 and number1>number3:
    print("Number1 is Greatest")

elif number1<number2 and number2>number3:
    print("Number2 is Greatest")

elif number2<number3 and number1<number3:
    print("number3 is Greatest")

else :
    print("Number is Equal")
    


# 5] Check if a person is eligible to vote (age ≥ 18).
 

age = int(input("Enter the age: "))

if age<0:
    print(f'Enter the Valid Age Number {age}')

elif age<18:
    print('Not eligible for Voting')

else:
    print("You are eligible for Voting")
    


# 6] Check whether a year is a leap year.


year = int(input("Enter the year: "))

if year%4==0:
    print(f'{year} is leap year')

else:
    print(f'{year} is not leap year')


# 7] Check if a character is a vowel or consonant.


char = str(input("Enter the Character:"))

vowel = ['a','e','i','o','u','A','E','I','O','U']
flag = False
for chars in vowel:
    if chars == char:
        flag = True

if flag == True:
    print("Character is Vowel")

else:
    print("Character is Consonant")
    


# 8] Check whether a number is divisible by 5 and 11.


num = int(input('Enter the number:'))

if num%5==0 and num%11==0:
    print("Number is Divisible by 5 and 11")

else:
    print("Number is not Divisible by 5 and 11")
    


# 9] Check if a number is a multiple of both 3 and 7.


num = int(input('Enter the number:'))

if num>7:
    if num%3==0 and num%7==0:
        print("Number is multiple of both 3 and 7")

    else:
        print("Number is not multiple of 3 and 7")

else:
    print("Number is not multiple of both 3 and 7")
    


# 10] Assign grades based on marks:
'''         90 - 100: A
            80 - 89: B
            70 - 79: C
            60 - 69: D
            Below 60: F
'''


mark = int(input('Enter the Marks:'))

if mark >= 90 and mark <= 100:
    print("Grade: A")

elif mark >= 80 and mark <=89:
    print("Grade: B")

elif mark >= 70 and mark <= 79:
    print("Grade: C")

elif mark >= 60 and mark <= 69:
    print("Grade: D") 

elif mark < 60:
    print("Fail...")

else:
    print("Enter valid marks less then 100")


# 11] Check if a character is uppercase or lowercase.


ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")
    


# 12] Find whether the entered alphabet is a vowel using if-elif.


ch = input("Enter an alphabet: ").lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")
    


# 13] Check if three sides can form a triangle.


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle is possible")
else:
    print("Triangle is not possible")


# 14] Determine the type of triangle (Equilateral, Isosceles, Scalene).


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# 15] Find the largest among four numbers.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest:", a)
elif b >= a and b >= c and b >= d:
    print("Largest:", b)
elif c >= a and c >= b and c >= d:
    print("Largest:", c)
else:
    print("Largest:", d)
    


# 16] Check whether a number is a three-digit number.


num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 17] Calculate electricity bill using slab rates.


units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Bill:", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Bill:", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Bill:", bill)  


# 18] Calculate income tax based on income slabs.


income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 300000:
    tax = 0
elif income <= 700000:
    tax = (income - 300000) * 0.05
elif income <= 1000000:
    tax = 400000 * 0.05 + (income - 700000) * 0.10
else:
    tax = 400000 * 0.05 + 300000 * 0.10 + (income - 1000000) * 0.20

if income >= 0:
    print("Income tax:", tax)


# 19] Check if a student passes (minimum 35 marks in each subject).

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Pass")
else:
    print("Fail")

# 20] Find whether a number is within a given range.

num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is within range")
else:
    print("Number is outside range")

# 21] Build a simple calculator using if-elif-else (+, -, *, /).

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 22] Check if a year is a century leap year.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not a leap year")
else:
    print("Not a century year")


# 23] Determine the season based on the month number.

month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month")
elif month in (3, 4, 5):
    print("Summer")
elif month in (6, 7, 8, 9):
    print("Monsoon")
elif month in (10, 11):
    print("Autumn")
else:
    print("Winter")

# 24] Find the number of days in a month.

month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid month")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month in (4, 6, 9, 11):
    print("30 days")
else:
    print("31 days")

# 25] Check whether a password meets minimum conditions (length, digits, etc.).

password = input("Enter password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Password is valid")
else:
    print("Password must have 8 characters and one digit")

# 26] Determine ticket price based on age category.

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Free")
elif age <= 17:
    print("Ticket price: ₹100")
elif age < 60:
    print("Ticket price: ₹200")
else:
    print("Ticket price: ₹150")

# 27] Calculate discount based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
    print("Discount:", discount)
    print("Final amount:", amount - discount)
elif amount >= 2000:
    discount = amount * 0.10
    print("Discount:", discount)
    print("Final amount:", amount - discount)
else:
    print("No discount")
    print("Final amount:", amount)

# 28] Check if a person is eligible for a driving license (age and eyesight condition).

age = int(input("Enter age: "))
eyesight = input("Is eyesight acceptable? (yes/no): ").lower()

if age < 0:
    print("Invalid age")
elif age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible")

# 29] Create a login system with username and password validation.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

# 30]  Create a menu-driven program using if-elif-else with options like:
'''                 Addition
                    Subtraction
                    Multiplication
                    Division
                    Exit
'''

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)

elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    print("Exiting program")

else:
    print("Invalid choice")
