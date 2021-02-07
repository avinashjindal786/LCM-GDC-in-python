
# lcm of two numbers
a= int(input("enter the first element"))
b= int(input("enter the second element"))

Max = max(a,b)

while(True):
    if Max % a == 0 and Max % b ==0:
        y = Max
        break
    Max = Max + 1

print(y)

# lcm of three numbers
e= int(input("enter the first element"))
f= int(input("enter the second element"))
g= int(input("enter the second element"))

Maxs = max(e,f,g)

while(True):
    if Maxs % e == 0 and Maxs % f ==0 and Maxs % g ==0:
        ys = Maxs
        break
    Maxs = Maxs + 1

print(ys)

# lcm more than two numbers

import math

def lcm(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i] // math.gcd(lcm,a[i])
    return  lcm

arr = [3,4]
print(lcm(arr))