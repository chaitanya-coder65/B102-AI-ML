# 1] Write a Python program to check whether a number is even or odd.

def check_num(num):
    if num%2==0:
        print("Number is Even")

    else:
        print("Number is odd")

check_num(13)

# 2] Write a program to find the largest of three numbers.

def greatest(num1,num2,num3):
    if num1 > num2 and num1>num3:
        print(f"{num1} is Greatest Number")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is Greatest Number")
    else:
        print(f"{num3} is Greatest Number")

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
num3 = int(input("Enter Number 3:"))

greatest(num1,num2,num3)


 # 3] Write a program to check whether a given number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 4] Write a program to print the Fibonacci series up to n terms.

def fibonacci(n):
    a=0
    b=1

    for i in range(n):
        print(a,end="")

    c = a+b
    a=b
    b=c

fibonacci(3)

# 5] Write a program to find the factorial of a number using a loop.

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# 6] Write a program to reverse a string without using [::-1].

s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

print("Reverse:", rev)


# 7] Write a program to check whether a string is a palindrome.


s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 8] Write a program to count the number of vowels and consonants in a string.


s = input("Enter a string: ")

vowels = 0
consonants = 0

for i in s:
    if i.lower() in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# 9] Write a program to find the sum of all elements in a list.

l = [10, 20, 30, 40, 50]

total = 0

for i in l:
    total = total + i

print("Sum:", total)


# 10] Write a program to find the largest and smallest element in a list without using max() or min().

l = [10, 5, 30, 2, 50, 15]

largest = l[0]
smallest = l[0]

for i in l:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)


# 11] Write a program to remove duplicate elements from a list.


l = [10, 20, 10, 30, 20, 40]

new_list = []

for i in l:
    if i not in new_list:
        new_list.append(i)

print(new_list)


# 12] Write a program to count how many times each element appears in a list using a dictionary.


l = [10, 20, 10, 30, 20, 10]

d = {}

for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)


# 13] Write a program to find the second-largest number in a list.


l = [10, 50, 30, 40, 20]

largest = l[0]
second = None

for i in l:
    if i > largest:
        second = largest
        largest = i
    elif i != largest:
        if second == None or i > second:
            second = i

print("Second Largest:", second)


# 14] Write a program to sort a list without using sort() or sorted().


for i in range(len(l)):
    for j in range(0, len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)


# 15] Write a function that accepts a list of numbers and returns a list containing only the even numbers.

def even_numbers(l):
    result = []

    for i in l:
        if i % 2 == 0:
            result.append(i)

    return result

l = [1, 2, 3, 4, 5, 6, 7, 8]

print(even_numbers(l))


# 16] Write a program to find the frequency of each character in a string.


s = "hello"

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)


# 17] Write a program to check whether two strings are anagrams of each other.


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")


# 18] Write a program to find all duplicate values in a list.


l = [10, 20, 30, 10, 40, 20, 50]

duplicates = []

for i in l:
    if l.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)


# 19] Write a program that takes a sentence and finds the longest word.


s = input("Enter a sentence: ")

words = s.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)


# 20] Create a simple student marks program that:
# accepts marks for 5 subjects,
# calculates the total and percentage,
# assigns a grade,and displays whether the student passed or failed.


marks = []

for i in range(5):
    m = int(input("Enter subject marks: "))
    marks.append(m)

total = sum(marks)

percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if any(m < 35 for m in marks):
    print("Result: Fail")
else:
    print("Result: Pass")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 35:
        print("Grade: D")
