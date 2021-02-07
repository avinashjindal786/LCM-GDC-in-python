# Gcd of two numbers
a= int(input("enter the first element"))
b= int(input("enter the second element"))

Min = min(a,b)

for i in range(1,Min+1):
    if a % i ==0 and b% i ==0:
        hcf = i
print(hcf)
print(Min)

# Gcd of three numbers
e= int(input("enter the first element"))
f= int(input("enter the second element"))
g= int(input("enter the second element"))
Min1 = min(f,g,e)

for i in range(1,Min1+1):
    if e % i ==0 and f% i ==0 and g% i ==0:
        hcf1 = i
print(hcf1)


# gcd more than two numbers
def find(x,y):
    while(y):
        x,y = y, x % y
        print(x,y)
    return x


l = [16, 32, 96]

num1=l[0]
num2=l[0]

gcd = find(num1,num2)
for i in range(2,len(l)):
    gcd = find(gcd,l[i])
print(gcd)