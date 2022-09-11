def count(coins,N,gsum):
    if gsum==0:
        return 1
    if gsum<0:
        return 0
    if N<=0:
        return 0
    return count(coins,N-1,gsum) + count(coins,N,gsum-coins[N-1])
gsum = int(input())
N = int(input())
coins = list(map(int,input().split()))
Ways = count(coins,N,gsum)
print(Ways)