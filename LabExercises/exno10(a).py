def binary(n, arr, num):
    low=1
    high=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==num:
            return mid
        elif num<arr[mid]:
            low=1
            high=mid-1
        else:
            low=mid+1
            high=n
    print("Enter the size of the array")
    size=int(input())
    pos=-1
    array=[0 for x in range(size+1)]
    print("Enter the array elements")
    for i in range(1,size+1):
        array[i]=int(input())
    print("Enter the search element")
    search_ele=int(input())
    pos=binary(size,array,search_ele)
    if pos!=-1:
         print("The element",search_ele,"is present in position",pos)
    else:
         print("Element not found")