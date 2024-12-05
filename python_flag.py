python = "Python"
x = 0
for i in python:
    x += 1
    print(python[0:x])

for i in python:
    x -= 1
    print(python[0:x])

python = "Python"
x = 0
for i in python:
    x += 1
    print(python[0:x])

for i in python:
    x -= 1
    print(python[0:x])

z = input("enter a number : ")
z = int(z)

for item in range(z,0,-1):
    print(item * " * ")
for item in range(0,z):
    print(item * " * ")