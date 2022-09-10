T = int(input())
result=[]
while(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    freq = sorted(numbers,key=numbers.count,reverse=True)   # sort based on frequency
    arr=[]
    # then to sort lower value to higher value in case of same frequency
    for v in freq:
        if len(arr)==0:
            arr.append(v)
        elif v<=arr[0] and freq.count(v)==freq.count(arr[0]):
            arr.insert(0,v)
        else:
            arr.append(v)
    result.append(arr)
    T=T-1
for i in range(len(result)):
    print(str(result[i]))