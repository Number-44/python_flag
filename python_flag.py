python = "Python"
x = 0
for _ in range(2):
    for _ in python:
        x += 1
        print(python[0:x])

    for _ in python:
        x -= 1
        print(python[0:x])

z = input("enter a number \" recommonded from 3 to 10 \" and press \" enter \" : ")
z = int(z)

for item in range(z,0,-1):
    print(item * " * ")
for item in range(0,z+1):
    print(item * " * ")
