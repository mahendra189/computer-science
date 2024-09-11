def find_change(coins,amount):
    change = []
    ream = amount
    cur = 0
    while ream > 0:
        if coins[cur] <= ream:
            ream = ream - coins[cur]
            change.append(coins[cur])
        else:
            cur = cur + 1
    return change

coins = [1000,500,200,100,50,20,10,5,2,1]
change = find_change(coins,45)
print(change)