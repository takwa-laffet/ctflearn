#!/usr/bin/python3
#Level 2: Control Flow & Loops 
#1
x = input("Enter password: ")

if x == "s3cr3t":
    print("Access granted")
else:
    print("Access denied")
#2
for i in range(1, 101):
    if i % 4 == 0:
        continue
    print(i)
#3
for i in range(10000):
    print(f"{i:04d}")
#4
anee = int(input("Enter a year: "))

if (anee % 4 == 0 and anee % 100 != 0) or (anee % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
#5
for number in range(2, 101):
    prim = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prim = False
            break

    if prim:
        print(number)
#6
check = "admin123"
temps = 3

while temps > 0:
    pwd = input("Enter password: ")

    if pwd == check:
        print("Login successful!")
        break

    temps -= 1
    print(f"Incorrect! temps left: {temps}")

if temps == 0:
    print("Account locked!")
#7
import random
secret = random.randint(1, 20)
while True:
    guess = int(input("Guess a number (1-20): "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
#8
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#9
while True:
    password = input("Enter password: ")
    if password == "s3cr3t":
        print("Access granted!")
        break

#10
x = input("Enter a string: ")

checkx = True
for i in range(len(s)):
    if x[i] != x[-i-1]:
        checkx = False
        break

if checkx:
    print("Palindrome")
else:
    print("Not a palindrome")
