
def solve(s):
    q=[]
    q.append(s)
    visited=[False for i in range(n)]
    visited[s]=True
    prev=[None for i in range(n)]
    while len(q)>0:
        node=q.pop(0)
        neighbours=adj.get(node)
        for next in neighbours:
            if not visited[next]:
                q.append(next)
                visited[next]=True
                prev[next]=node
    return prev
def reconstructedPath(s,e,prev):
    path=[]
    at=e
    if at!=None:
        path.append(at)
        for i in range(len(prev)):
            if at!=None:
                at=prev[at]
                path.append(at)
    path=path[::-1]
    if path[1]==s:
        path.pop(0)
        return path
    return []

n=13
adj={0:[9,7,11],9:[10,8,0],7:[3,6,11,0],11:[7,0],10:[1,9],8:[1,12,9],3:[2,4,7],6:[5,7],1:[8,10],12:[8,2],2:[12,3],4:[3],5:[6]}
s=0
e=4
prev=solve(s)
print(prev)

print(reconstructedPath(s,e,prev))
