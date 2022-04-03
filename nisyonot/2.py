import math
import random
from random import randint

num=random.randint(1,99)
print(num)
st_num=str(num)
length=len(st_num)
print(length)
sum=0
while b!=0:
    a=(num%10)
    b=math.floor(num/10)
    sum=sum+a
    print(sum)
    
    # c=b%10
    # d=math.floor(b/10)
    # e=d%10
    # f=math.floor(e/10)
    # if f==0:
print(sum)


