#!/usr/bin/python3
#Level 3: Lists, Tuples, and Dictionaries
#1
tools = [
    "Nmap", "Metasploit", "Wireshark", "Burp Suite", "JohnTheRipper",
    "Aircrack-ng", "Hydra", "Nikto", "SQLmap", "Hashcat"
]
print(tools)
#2
print(tools[2])
#3
code_htpp= {
    200: "OK",
    301: "Moved Permanently",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}
print(code_htpp)
#4
text = input("Enter text: ")
count = {}
for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)
#5
numbers = [12, 4, 9, 1, 20, 15]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
#6
port = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    80: "HTTP",
    443: "HTTPS"
}
input_port = int(input("Enter port number: "))
if input_port in port:
    print("service:", port[input_port])
else:
    print("Unknown port")
#7
def remove(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
print(remove([1,2,2,3]))
#8
items = ["nmap", "sqlmap", "hydra"]
end = ",".join(items)
print(end)
#9
word=["cyber","security","blue","red","Metasploit","nmap"]
x=""
for i in word:
    if len(i)>len(x):
        x=i
print("longest ",x)
#10
pepole={
    "ali":"password123",
    "ahmed":"admin",
    "mohamed":"root",
    "sara":"saraadmin"
}
users=input("enter user:")
if users in pepole:
    print("password:",pepole[users])
else:
    print("user not found 404")