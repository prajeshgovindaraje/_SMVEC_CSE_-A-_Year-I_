#functions \
'''def factorialfinder(a):
    a=int(input('enter the number'))
    b=1
    for i in range (1,a+1):
        b=b*i
    print(b)


factorialfinder()
'''
#factorial of a given number using function
a=int(input('enter the number: '))
def factorialfinder(a):
    
    #a=int(input('enter the number'))
    b=1
    for i in range (1,a+1):
        b=b*i
    print("the factorial of the given number is : ",b)


factorialfinder(a)

