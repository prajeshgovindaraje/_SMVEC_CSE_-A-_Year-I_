def linear(n,arr,num):

    for i in range(n):
        if arr[i]==num:
            return i 
print("enter the size of the array ")
size = int(input())
pos=-1
array=[0 for x in range(size)]
print("enter the array elements")
for i in range(size):
    array[i]=int(input())
search_ele=print('enter the search element ')
pos = linear(size, array,search_ele)
if pos!=-1:
    print("the element ", search_ele, "is present in position",pos+1)
else:
    print("element is not found")        

