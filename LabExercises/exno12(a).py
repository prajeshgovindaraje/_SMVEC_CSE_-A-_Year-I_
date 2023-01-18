print('Enter the sentence')
sentence=input()
d={}
l=sentence.split(" ")
temp=[]
for i in range(len(l)):
     if l[i] in temp:
        d[l[i]]+=1
     else:
        temp.append(l[i])
        d[l[i]]=1
index=0
word=''
for key,value in d.items():
         if value>index:
             index=value
             word=key
print("The word '",word,"' is the most repeated with count",index)