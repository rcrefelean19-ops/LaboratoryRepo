import math

n=int(input())

#Special Check to see if we want to determine the first element
if n==1:
    not_one=False
else:
    not_one=True

#Function to check if a number is a prime number
def prim(n:int)->bool:
    if n<=1:
        return False
    if n%2==0 and n!=2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True

element=2
current_output=2
n-=1

while n>0:
    #If an element is a prime number then we only count it as one element in the sequence
    if prim(element):
        n-=1
        current_output=element
        element+=1
    else:
        #We decompose each element and then subtract from n, if n becomes less than zero
        #then it's definitely in the area determined by the last divisor used
        copy_element=element
        divisor=2
        while copy_element>1:
            current_output=divisor
            if copy_element%divisor==0:
                n-=divisor
            while copy_element % divisor == 0:
                copy_element //= divisor
            if n<=0:
                break
            divisor+=1
        element+=1

if not_one:
    print(current_output)
else:
    print(1)