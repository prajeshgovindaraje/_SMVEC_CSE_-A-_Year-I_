import random
n=input("enter your choise: ")
ist1 = ['rock', 'paper', 'sissor']
x=random.choice(ist1)
print("computer's choise:",x)
chos=x
if n==chos and chos==n:
    print("draw")
elif n=='rock' and  chos=='sissor':
    print("you win")
elif n=='rock'and chos=='paper' :
    print("you lose")   
elif n=='paper' and chos=='sissor':
    print("you lose")
elif n=='paper' and chos=='rock':
    print("you win")
elif n=='sissor' and chos=='rock':
    print("you fail")
elif n=='sissor' and chos=='paper':
    print("you win")
else:
  print("enter valid input ")
    




