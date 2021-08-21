def dfs(at,v,visitednode,adj):
    v[at]=True
    edges=adj.get(at)
    for edge in edges:
        if v[edge]==False:
            dfs(edge,v,visitednode,adj)
    visitednode.append(at)
adj={0:[9,7,11],9:[10,8,0],7:[3,6,11,0],11:[7,0],10:[1,9],8:[1,12,9],3:[2,4,7],6:[5,7],1:[8,10],12:[8,2],2:[12,3],4:[3],5:[6]}
N=13
v=[False for i in range(N)]
ordering=[0 for i in range(N)]
i=N-1
for at in range(0,N):
    if v[at]==False:
        visitednode=[]
        dfs(at,v,visitednode,adj)
        for id in visitednode:
            ordering[i]=id
            i-=1
print(ordering)
