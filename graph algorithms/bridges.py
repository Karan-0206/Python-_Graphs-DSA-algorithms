# the commented statements are for articulation points

from collections import defaultdict
class Graph:

    def __init__(self,vertices):
        self.v= vertices
        self.adj = defaultdict(list)
        self.id=0
        #self.outedgecount=0

    
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self,at,parent,bridges,vis,low,ids):
        vis[at]=True
        self.id+=1
        low[at]=ids[at]=self.id
        for i in self.adj[at]:
            if i==parent: continue
            if not vis[i]:
                self.dfs(i,at,bridges,vis,low,ids)
                low[at]=min(low[at],low[i])
                if ids[at]<low[i]:
                    bridges.append(at)
                    bridges.append(i)
            else:
                low[at]=min(low[at],ids[i])
    def bridge(self):
        id=0
        #isart=[false for i inn range(self.v)]
        ids=[float('inf') for i in range(self.v)]
        low=[float('inf')for i in range(self.v)]
        vis=[False for i in range(self.v)]
        bridges=[]
        for i in range(self.v):
            if  not vis[i]:
                #self.outedgecount=0
                #self.dfs(i,i,-1,vis,low,ids)
                #self.isart[i]=(outedgecount>1)
                self.dfs(i,-1,bridges,vis,low,ids)
        return bridges
        #return isart

aj = Graph(5)
aj.addEdge(1, 0)
aj.addEdge(0, 2)
aj.addEdge(2, 1)
aj.addEdge(0, 3)
aj.addEdge(3, 4)
print(aj.bridge())
