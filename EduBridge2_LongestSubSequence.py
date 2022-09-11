N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()   # sort in ascending order
#print(numbers)
count=1
for i in range(1,len(numbers)):
    if numbers[i]==numbers[i-1]+1:  #check for consecutive number in sequence
        count+=1
    else:
        break
print(count)