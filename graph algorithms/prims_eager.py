from queue import PriorityQueue
adj={0:{(4,1),(1,2)},1:{(1,3)},2:{(2,1),(5,3)},3:{(3,4)},4:{(0,0)}}
n=5 
ipq=PriorityQueue() 
vis=[False for i in range(n)]
s=0 
m=n-1 
edge_count,mst_cost=0,0, 
mst_edges=[None for i in range(n)] 
relax(s)
while not ipq.empty() and edge_count!=m: 
    destind,edge=ipq.get() 
    edge_count+=1 
    mst_edges[edge_count]=edge 
    mst_cost+=edge 
    