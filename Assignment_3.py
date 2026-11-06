# 1. Data Types


# 1]Find the data type of every value in a mixed list.

lst = [
    "Chaitanya",
    11,
    11.5,
    True
]

for item in lst:
    print(type(item))

print("\n")


# 2]Convert a nested list into a tuple of tuples.

l = [[1, 2, 2], [3, 4, 5], ["hello", True, 12.4]]

result = tuple(tuple(item) for item in l)

print(type(result))

print("\n")

# 3]Remove all duplicate values from a mixed list while preserving the original order.

lst = [
    "Chaitanya",
    11,
    11,
    11.5,
    True,
    True
]

result = []

for item in lst:
    if item not in result:
        result.append(item)

print(result)


# 2. Operators
# 4]Check whether a number is a power of 2 using operators.


n = int(input("Enter a number: "))

if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")


# 5] Swap two numbers using bitwise XOR.

a = 10
b = 20

print("Before swapping:", a, b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:", a, b)


# 6]Find whether a number is divisible by both 4 and 6 using logical operators.

number = int(input("Enter the Number:"))

if number%4==0 and number%6==0:
    print(f"{number} is divisible by 4 and 6")

else:
    print(f"{number} is not divisible by 4 and 6")


# 7]Calculate the total electricity bill using different unit rates.

units = int(input("Enter number of units used:"))

if units<= 100:
    bill = units * 3

elif units<= 200:
    bill = (100 * 3) + (units - 100)*5

elif units<=300:
    bill = (100 * 3) + (100 * 5) + (units - 200)*7

else:
    bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300)*9

print(f"Total amount is {bill} for {units}")




# 3] Conditional Statements

# 8]Check whether three sides can form a triangle.
side_1 = int(input("Enter value for side 1"))
side_2 = int(input("Enter value for side 2"))
side_3 = int(input("Enter value for side 3"))

if (side_1 + side_2 + side_3 == 180 and
    side_1 + side_2 > side_3 and 
    side_2 + side_3 > side_1 and 
    side_3 + side_1 > side_2 ):
    print("Triangle is created successfully......")

else:
    print("Triangle is not created......")


# 9]Determine the type of triangle (Equilateral, Isosceles, Scalene).

side_1 = int(input("Enter value for side 1"))
side_2 = int(input("Enter value for side 2"))
side_3 = int(input("Enter value for side 3"))

if (side_1 + side_2 + side_3 == 180 and
    side_1 + side_2 > side_3 and 
    side_2 + side_3 > side_1 and 
    side_3 + side_1 > side_2 ):
    print("Valid Triangle")

    if side_1==side_2==side_3:
        print("Equilateral Triangle")

    elif side_1==side_2 or side_2==side_3 or side_3==side_1:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("invalid Triangle")


#10]Create a simple ATM menu (Withdraw, Deposit, Balance)

balance = 5000

while True:

    print("\n----- ATM MENU -----")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to withdraw: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal successful!")

        else:
            print("Insufficient balance or invalid amount")

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")

        else:
            print("Enter a valid amount")

    elif choice == 3:
        print("Your available balance is:", balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Please try again.")


# 11]Calculate income tax based on different tax slabs.

income = int(input("Enter your annual income: "))

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.10

else:
    tax = (250000 * 0.05) + (500000 * 0.10) + (income - 1000000) * 0.20

print("Your income tax is:", tax)


# 12] Create a menu-driven calculator using if-elif.

print("----- CALCULATOR MENU -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition:", a + b)

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Subtraction:", a - b)

elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Multiplication:", a * b)

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b != 0:
        print("Modulus:", a % b)
    else:
        print("Cannot divide by zero")

elif choice == 6:
    print("Exit..")

else:
    print("Invalid choice!")




# 4]Loops

#13] Print all prime numbers between 1 and n.

n = int(input("Enter the value of n: "))

for num in range(2, n + 1):

    count = 0

    for i in range(1, num + 1):

        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)


# 14]Find the factorial of a number using a loop
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial is:", fact)


# 15]Print the Fibonacci series up to n terms.
 
n = int(input("Enter the term require:"))

a=0
b=1

for i in range(n):
    print(a,end="")

    c = a+b
    a=b
    b=c


# 15]Check whether a number is an Armstrong number.

n= int(input("Enter the Number:"))

org_num = n
temp = n

len = len(str(n))
total = 0

while temp>0:

    digit = temp % 10

    total = total + digit ** len 

    temp = temp // 10

if total == org_num:
    print("Armstrong Number")

else:
    print("not Armstrong number")


# 17] Reverse a number and check if it is a palindrome.

n = int(input("Enter the Number:"))

org_num = n
temp = n

while temp>0:

    digit = temp % 10

    rev = rev * 10 + digit

    temp = temp // 10

if rev == org_num:
    print("Number is palindrome")
else:
    print("Not a palindrome")


# 18]Find the Greatest Common Divisor (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):

    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD is:", gcd)




# 5] Function

# 19] Write a function to check if a string is a palindrome.

def palindrome(string):
    if string[::-1] == string:
        print("String is palindrome")

    else:
        print("String is not palindrome")

palindrome("mom")


# 20] Write a function to count vowels and consonants in a string.

def count(string):
    vowels_count = 0
    consonants_count = 0
    for i in string:
        if i.lower() in "aeiou":
            vowels_count += 1
        else:
            consonants_count += 1
    return vowels_count,consonants_count

print(count("Chaitanya"))

# 22] Write a function to return all factors of a number.

def factors(num):
    factor = []
    for i in range(1,num+1):
        if num%i==0:
            factor.append(i)

    return factor

print(factors(12))


# 23] Write a function to find the second-largest number in a list.

def second_largest(lst):
    unique = list(set(lst))
    unique.sort()

    if len(unique) < 2:
        return "Second largest does not exist"

    return unique[-2]

print(second_largest([10, 20, 30, 40, 50]))




# 6] List

# 24] Merge two lists without duplicates.

def merge_lists(l1, l2):
    result = []

    for i in l1 + l2:
        if i not in result:
            result.append(i)

    return result

print(merge_lists([1, 2, 3], [3, 4, 5]))

# 25] Find the second-largest and second-smallest elements.

def find_numbers(lst):
    unique = sorted(set(lst))

    if len(unique) < 2:
        return "Not enough unique elements"

    second_smallest = unique[1]
    second_largest = unique[-2]

    return second_smallest, second_largest

print(find_numbers([10, 20, 30, 40, 50]))



# 26] Rotate a list to the left by k positions.

def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate([1, 2, 3, 4, 5], 2))


# 27] Separate even and odd numbers into two lists.

def separate(lst):
    even = []
    odd = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd

print(separate([1, 2, 3, 4, 5, 6]))


# 28] Find the common elements between two lists.

def common(l1, l2):
    result = []

    for i in l1:
        if i in l2 and i not in result:
            result.append(i)

    return result

print(common([1, 2, 3, 4], [3, 4, 5, 6]))



# 7] Tuples & Sets

# 29] Count the frequency of each element in a tuple

def frequency(t):
    result = {}

    for i in t:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

print(frequency((1, 2, 2, 3, 3, 3)))

# 30] Find union, intersection and difference of two sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))

# 31] Check whether one set is a subset of another

def check_subset(a, b):
    return a.issubset(b)

print(check_subset({1, 2}, {1, 2, 3, 4}))




# 8] Dictionaries

# 32] Count the frequency of words in a sentence

def word_count(sentence):
    result = {}

    words = sentence.lower().split()

    for i in words:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

print(word_count("python is easy python is powerful"))

# 33] Create a dictionary from two lists (keys and values)

def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Chaitanya", 22, "Pune"]

print(create_dict(keys, values))

# 34] Sort a dictionary by its values

def sort_dict(d):
    result = {}

    values = sorted(d.values())

    for i in values:
        for key in d:
            if d[key] == i:
                result[key] = i

    return result


data = {"A": 50, "B": 20, "C": 40}

print(sort_dict(data))



# 9] File Handling

# 35] Read a text file and count lines, words and characters

def count_file(filename):
    with open(filename, "r") as f:
        data = f.read()

    lines = data.splitlines()
    words = data.split()
    characters = len(data)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

count_file("sample.txt")

# 36] Copy only even-numbered lines from one file to another

def copy_even_lines(source, destination):
    with open(source, "r") as f:
        lines = f.readlines()

    with open(destination, "w") as f:
        for i in range(1, len(lines) + 1):
            if i % 2 == 0:
                f.write(lines[i-1])

copy_even_lines("input.txt", "output.txt")





# 10] Exception Handling
# 37] Handle invalid integer input using try-except

try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Please enter a valid integer")

# 38] Handle file-not-found errors while reading a file

try:
    with open("data.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File does not exist")




# 11] Modules

# 39] Create a random password generator using random and string modules

import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print(password_generator(10))

# 40] Calculate the number of days between two dates

from datetime import date

def calculate_days(d1, d2):
    date1 = date(d1[0], d1[1], d1[2])
    date2 = date(d2[0], d2[1], d2[2])

    difference = date2 - date1

    return abs(difference.days)

print(calculate_days((2026, 1, 1), (2026, 1, 10)))
