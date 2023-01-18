# file name ---package.py
def prime(a,b):
 for i in range(a,b+1,1):
    flag=0
 for j in range(2,(i//2)+1,1):
    if i%j==0:
        flag=1
    break
 if flag==0 and i!=1:
    print(i)

# in second file import this
usepack.py
from package import prime
print("Enter the starting range")
a=int(input())
print("Enter the ending range")
b=int(input())
prime(a,b)