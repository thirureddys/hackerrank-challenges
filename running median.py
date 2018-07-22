import sys
import bisect

arr = []
n = int(raw_input().strip())
for i in range(n):
    x = int(raw_input().strip())
    bisect.insort(arr, x)
    if i % 2 == 0:
        print(arr[i // 2] / 1.0)
    else:
        print((arr[i // 2] + arr[i // 2 + 1]) / 2.0)
