def two_sum(m, n, a):
    tb = {}
    for idx, val in enumerate(a):
        #print idx,val
        if m - val in tb:
            print("{0} {1}".format(tb[m - val] + 1, idx + 1))
            #pass
        else:
            tb[val] = idx
            #print tb[val]
            #print tb

t = int(raw_input().strip())
for _ in range(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = list(map(int, raw_input().strip().split(' ')))
    two_sum(m, n, a)
    #print a 
