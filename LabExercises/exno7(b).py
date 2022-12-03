#fibbionaci series using recursion
n= int(input("range : "))



def fibonacci(n):
    count=0
    a=0
    b=1
    if n<=0:
         print('invalid number')
    elif n==1 :
         print(a) 
    
    else:
        while(count<n):
            print(a)
            c=a+b
            a=b
            b=c
            count+=1
fibonacci(n)           
            




     


    






  
  