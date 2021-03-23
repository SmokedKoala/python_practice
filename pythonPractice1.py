import math

def f11 (x, y):
    return math.sqrt(x**4-math.e**y)-(27*y**7+math.sin(y))+(51*y**2-math.tan(y))/(y**8+27*y**3-5)

def f12(x):
    if x<100:
        return x**4 - math.fabs(x)
    if 100<=x and x<187:
        return 27*(math.e**x-88*x**2)**7+x**4
    if 187<=x and x<264:
        return x**8+27*x**3-5
    if x>=264:
        return math.e**(x**(3)/75+x**4+89) - math.tan(x**6+16*x**4)

def f13(n,m):
    sum1 =0
    sum2 = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            sum1+=(i**4-math.e**j)
    for i in range (1,n+1):
        sum2+=(math.e**i+69*i**2)
    return 40*sum1+51*sum2

def f14(x):
    if x==0:
        return 4
    if x==1:
        return 6
    return 1/31*(f14(x-1))**2+1/79*f14(x-2)**3


# if __name__ == '__main__':
    # print("First task:")
    # print(task11(81,-11))
    # print(task11(-62,-61))
    # print("Second task:")
    # print(task12(207))
    # print(task12(54))
    # print("Third task:")
    # print(task13(19,100))
    # print(task13(33,51))
    # print("Forth task:")
    # print(task14(12))
    # print(task14(4))