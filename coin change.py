n,m=map(int,raw_input().split(" "))
#print n,m
coins=sorted(list(map(int,raw_input().strip().split(" "))),reverse=True)
#print coins
tb={}
def dp(coins,n):
    l=len(coins)
    if coins == [] or n < 0:
        return 0
    elif n == 0:
        return 1
    elif not(l,n) in tb:
        res = 0
        for idx,coin in enumerate(coins):
            if n-coin >= 0:
                res =res +  dp(coins[idx:],n-coin)
        tb[(l,n)]=res
    return tb[(l,n)]

print dp(coins,n)
