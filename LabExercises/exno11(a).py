def bubble(n,arr):
 for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
    arr[j]=arr[j+1]
    arr[j+1]=temp
    print("Enter the size of the array")
    size=int(input())
    pos=-1
    array=[0 for x in range(size)]
    print("Enter the array elements")
    for i in range(size):
        array[i]=int(input())
    bubble(size,array)
    print("The sorted array is")
    for i in range(size):
     print(array[i])