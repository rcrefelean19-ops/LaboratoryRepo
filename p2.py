n=int(input())

def SmallestFibGreater(n:int)->int:
    a=1
    b=1
    m=a+b
    while m <= n:
        a = b
        b = m
        m = a + b
    return m

print(SmallestFibGreater(n))

