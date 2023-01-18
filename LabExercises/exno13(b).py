file=open("demo.txt",'r')
file2=open("demo2.txt",'w')

num=file.readline()
num=int(num)
print(num)
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


file2.write(str(fact))
