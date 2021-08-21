adj=[[0,4,1],[0,-1,2],[1,-1,3],[2,2,1],[2,5,3],[3,-3,4],[4,0,0]]
e=6
v=5
s=0
d=[float('inf') for i in range(v)]
d[s]=0
for i in range(v-1):
    for u,w,v in adj:
        if d[u]+w<d[v]:
            d[v]=d[u]+w
for i in range(v-1):
    for u,w,v in adj:
        if d[u]+w<d[v]:
            d[v]=float('-inf')
print(d)
