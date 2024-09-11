def cheapFlight(n,flights,src,dst,k):
    prices = [float("inf")] * n
    prices[src] = 0
    for i in range(k+1):
        tmp = prices.copy()
        for s,d,p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmp[d]:
                tmp[d] = prices[s] + p
        prices = tmp.copy()
    return prices[dst]

src = 0
dst = 2
flights = [[0,1,1000],
           [0,2,2000],
           [1,2,300],
           [3,2,100],
           [2,0,11000],
           ]
k = 2
print(cheapFlight(4,flights,src,dst,k))