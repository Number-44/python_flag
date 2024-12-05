import time

python = "Python"

for _ in range(2):
    x = 0
    for _ in python:
        x += 1
        print(python[0:x])

    for _ in python:
        x -= 1
        print(python[0:x])
while True:
    z = input("enter a number \" recommonded from 3 to 10 \" and press \" enter \" : ")
    if z.isdigit() and 3 <= int(z) <= 10 :
        z = int(z)
        break

    print(f"{z} is not valid : Please enter a number in the given range !")
for item in range(z,0,-1):
    print(item * " * ")
for item in range(0,z+1):
    print(item * " * ")



print(f"the process time is :{time.process_time()} seconds " )
