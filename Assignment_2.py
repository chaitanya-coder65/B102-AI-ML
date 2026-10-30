# 1. Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

def is_even(n):
    if n%2==0:
        print(f"{n} is Even Number.")
    else:
        print(f"{n} is Odd Number.")

is_even(4)
print("\n")


# 2. Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.

def largest(a,b):
    if a>b:
        return a
    else:
        return b

greatest = largest(4,3)
print(f"{greatest} Number is largest")
print("\n")


# 3. Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_number(n):
    for i in range(1,n+1):
        print(i)
        
print_number(5)
print("\n")


# 4. Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

    return sum

print(sum_n(4))
print("\n")


# 5. Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

table(5)
print("\n")

# 6. Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3

def count_even(lst):
    sum = 0
    for i in lst:
        if int(i)%2==0:
            sum = sum+1
    return sum

even =count_even(["1","4","6","7","9"])
print(f"List Contain total {even} Even Number")
print("\n")


# 7. Find Maximum
# Without using max(), write a function that returns the largest number in a list.

def max(lst):
    max_val = int(lst[0])
    for i in lst:
        if int(i) > max_val:
            max_val = int(i)

    return max_val

gre_val = max(["4","6","7","1","2"])
print(f"The Greatest Number in list is the {gre_val}")


# 8. FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()
print("\n")


# 9. Palindrome Checker
# Write a function that returns True if a string is a palindrome.

def palindrome(string):
    reverse_text = string[::-1]
    if string == reverse_text:
        print("String is palindrome")
    else:
        print("String is not Palindrome")

palindrome("mom")
print("\n")


# 10. Count Vowels
# Write a function that counts the vowels in a string.

def count_vowels(string):
    vowels = ["a","e","i","o","u"]
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1

    return count

vowels = count_vowels("Chaitanya")
print(f"String Contains {vowels} Vowels")
print("\n")
    

# 11. Second Largest Number
# Write a function that returns the second largest number in a list without using sort().

def sec_lar(lst):
    l = int(lst[0])
    sl = float('-inf')
    
    for item in lst:
        val = int(item)  
        
        if l < val:
            sl = l
            l = val 
        
        elif val > sl and val < l:
            sl = val

    return sl 

second_largest = sec_lar(["1", "4", "5", "2", "1"])
print(f"Second largest number in List is {second_largest}")
print("\n")


# 12. Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

import random

def play_guessing_game():
    
    target = random.randint(1, 100)
    
    print("Think a number between 1 and 100.")
    
   
    while True:
        guess = int(input("Take a guess: "))
        
        
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print("You win! You got it right.")
            break 


play_guessing_game()
print("\n")


# 13. Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

grade(76)
