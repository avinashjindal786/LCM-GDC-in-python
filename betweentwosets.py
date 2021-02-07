
import math

def getTotalX(a, b):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])


    def find(x, y):
        while (y):
            x, y = y, x % y

        return x
    if len(b) > 1:
        num1 = b[0]
        num2 = b[1]

        gcd = find(num1, num2)
        for i in range(2, len(b)):
            gcd = find(gcd, b[i])
    else :
        gcd = b[0]

    lst =[]
    for i in range(lcm,gcd+1):
        if gcd % i ==0 :
            lst.append(i)
    print(len(lst))








first_multiple_input = input().rstrip().split()

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)

