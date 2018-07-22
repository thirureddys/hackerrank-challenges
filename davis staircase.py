tb = {1:1,2:2,3:4}
out=[]
def patterns(n):
    
    if not n in tb.keys():
        tb[n] = patterns(n - 1) + patterns(n - 2) + patterns(n - 3)
        #print tb[n]
        #out.append(tb[n])
    return tb[n]

s = int(raw_input().strip())

for _ in range(s):
    n = int(raw_input().strip())
    #print patterns(n)
    out.append(patterns(n))

for i in out:
    print i
    
