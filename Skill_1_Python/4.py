#!/usr/bin/python3
#Level 4: Functions & Modules
#1
def reverse(char):
    return char[::-1]
#2
def strong_password(password):
    number = any(ch.isdigit() for ch in password)
    special = any(not ch.isalnum() for ch in password)
    if len(password) >= 8 and number and special:
        return True
    return False
print(strong_password("H@ck3r123"))
#3
import random
import string

def generate():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(12))

print(generate())
#4
import hashlib

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

print(md5("hacker"))
#5
def valid(ip):
    test = ip.split(".")
    if len(test) != 4:
        return False
    for part in test:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True
print(valid("8.8.8.8"))
#6
import random
def random_mac():
    x=[]
    for i in range(6):
        x.append(f"{random.randint(0,255):02x}")
    return ":".join(x)
print(random_mac())
#7
def encrypt(text,key):
    xor=""
    for k in text:
        xor+=chr(ord(k)^key)
    return xor
print(encrypt("hi hacker",11))
#8
import uuid

def device():
    return str(uuid.uuid4())

print(device())
#9
import socket
def resolve(host):
    return socket.gethostbyname(host)
print(resolve("google.com"))
#10
def vowels(s):
    v="aeiouAEIOU"
    return "".join(ch for ch in s if ch in v)
print(vowels("new hacker in the world"))
