n=int(input())

def SmallestFibGreater(n:int)->int:
    a=1
    b=1
    m=a+b
    #Going through the Fibonacci Sequence until m becomes greater than n, the first time we find
    #such number, that will be the smallest number from the Fibonacci Sequence greater than n
    while m <= n:
        a = b
        b = m
        m = a + b
    return m

print(SmallestFibGreater(n))