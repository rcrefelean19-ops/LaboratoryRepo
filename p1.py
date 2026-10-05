import math

n=int(input())

n-=1

def prim(n:int)->bool:
    if n<=1:
        return False
    if n!=2 and n%2==0:
        return False
    for d in range(3, int(math.sqrt(n))+1, 2):
        if n%d==0:
            return False
    return True

while not prim(n):
    n-=1
    if(n<=1):
        break

if n>1:
    print(n)
else:
    print("Nu exista!")