arr = [0,0,0,0]
rounds=int(input("enter no of rounds : "))
i=1
while i<=rounds:
    for elements in range(len(arr)):
        x=int(input("enter the score of the player%d in round%d :" %((elements+1),(i))))
        arr[elements]+=x
    i+=1
    maxScore = max(arr)
    for i in arr:
        if i == maxScore:
            print("The winner is player ",(arr.index(i)+1))
            break    