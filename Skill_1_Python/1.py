#!/usr/bin/python3
# Level 1: Python Basics & Data Types
#1
print("Hello, Hacker!")
#2
name = input("Enter Your Name : ")
print(f"Welcome, {name}")
#3
x = int("1337")
result = x + 10
print(result)
#4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)
#5
s = "rekcah_repus"
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

print(reversed_s)
#6
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#7
test = True
print(test)
#8
binary = "100101"
decimal = int(binary, 2)
print(decimal)
#9
text = "H4ck3r"
result = ""

for i, ch in enumerate(text):
    if ch.isalpha():               
        if i % 2 == 0:
            result += ch.upper()
        else:
            result += ch.lower()
    else:
        result += ch               

print(result)
#10
password = "P@ssw0rd"
test = "aeiouAEIOU"
end = ""

for ch in password:
    if ch in test:
        end += "*"
    else:
        end += ch

print(end)
