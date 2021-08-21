def setup(m,memo,s,n):
    for i in range(n):
        if i==s:
            continue
        memo[i][1<<s|1<<i]=m[s][i]
def solve(m,memo,s,n):
    for r in range(3,n+1):
        for subset in combinations(r,n):
            if notin(s,subset):
                continue
            for next in range(n):
                if next==s or notin(next,subset):
                    continue
                state=subset^(1<<next)
                min_dist=float('inf')
                for e in range(n):
                    if e==s or e==next or notin(e,subset):
                        continue
                    new_dist=memo[e][state]+m[e][next]
                    if new_dist<min_dist:
                        min_dist=new_dist
                    memo[next][subset]=min_dist
def notin(i,subset):
    return ((1<<i)&subset)==0
def combinations(r,n):
    subsets=[]
    combination(0,0,r,n,subsets)
    return subsets
def combination(set,at,r,n,subsets):
    if r==0:
        subsets.append(set)
    else:
        for i in range(at,n):
            set=set|(1<<i)
            combination(set,i+1,r-1,n,subsets)
            set=set&~(1<<i)
def findmincost(m,memo,s,n):
    endstate=(1<<n)-1
    mintourcost=float('inf')
    for e in range(n):
        if e==s: continue
        tourcost=memo[e][endstate]+m[e][s]
        if tourcost<mintourcost:
            mintourcost=tourcost
    return mintourcost
def findtour(m,memo,s,n):
    lastindex=s
    state=(1<<n)-1
    tour=[None for i in range(n+1)]
    for i in range(n-1,0,-1):
        index=-1
        for j in range(n):
            if j==s or notin(j,state): continue
            if index==-1:
                index=j
            prevdist=memo[index][state]+m[index][lastindex]
            newdist=memo[j][state]+m[j][lastindex]
            if newdist<prevdist:
                index=j
        tour[i]=index
        state=state^(1<<index)
        lstindex=index
    tour[0]=tour[n]=s
    return tour

m=[[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
s=0
N=4
memo=[[None for i in range(2**N)]for j in range(N)]
setup(m,memo,s,N)
solve(m,memo,s,N)
min_cost=findmincost(m,memo,s,N)
tour=findtour(m,memo,s,N)
print(min_cost)
print(tour)
