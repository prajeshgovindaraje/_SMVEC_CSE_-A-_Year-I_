n = int(input("Enter a number"))

for x in range(0,n):

    sum = 0
    
    for i in range(1, x):
        if x%i == 0:
            sum += i

    if x == sum:
        print(f"{x} is a Perfect number")
    else:
        print(f"{x} is not a Perfect number")