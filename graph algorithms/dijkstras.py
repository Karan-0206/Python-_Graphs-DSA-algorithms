import sys
from queue import PriorityQueue
adj={0:{(4,1),(1,2)},1:{(1,3)},2:{(2,1),(5,3)},3:{(3,4)},4:{(0,0)}}
n=5
s=0
vis=[False for i in range(n)]
dist=[float('inf') for i in range(n)]
dist[0]=0
pq=PriorityQueue()
pq.put((0,s))
while not pq.empty():
    minval,index=pq.get()
    vis[index]=True
    if dist[index]<minval:
        continue
    for edge,val in adj[index]:
        if vis[val]:
            continue
        newdist=dist[index]+edge
        if newdist<dist[val]:
            dist[val]=newdist
            pq.put((newdist,val))
print(dist)
