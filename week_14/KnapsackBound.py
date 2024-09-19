
'''
# item must be sorted in decreasing order of r

def getKey(x):
    return x.r

item.sort(key=getKey, reverse=True)

'''
	
def Bound(i, C):	# object i -> n-1, capacity = C
    global item, N
    
    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C-sw, item[j].w)
        f = float(wj)/item[j].w
        sw += f*item[j].w
        sv += f*item[j].v
        j += 1
    return sv


