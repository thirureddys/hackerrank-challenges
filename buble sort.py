n=int(raw_input())
arr=list(map(int,raw_input().strip().split(" ")))
swaps = 0
flag = True
while flag:
    flag = False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swaps += 1
            #print arr
            flag = True

print "Array is sorted in", swaps ,"swaps."
print "First Element:",arr[0]
print "Last Element:",arr[-1]
