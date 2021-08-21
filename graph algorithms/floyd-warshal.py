def setup(m,dp,next,n):
    for i in range(n):
        for j in range(n):
            dp[i][j]=m[i][j]
            if m[i][j]!=float('inf'):   #here +infinity means that the node has no edge from i to j.
                next[i][j]=j 


m=[[0,4,1,9],[3,0,6,11],[4,1,0,2],[6,5,-4,0]]
a=4 
dp=[[None for i in range(a)]for j in range(a)]
next=[[None for i in range(a)]for j in range(a)]
setup(m,dp,next,a)
for k in range(a):
    for i in range(a):
        for j in range(a):
            if (dp[i][k]+dp[k][j])<dp[i][j]:
                dp[i][j]=dp[i][k]+dp[k][j]
                next[i][j]=next[i][k] 

for k in range(a):
    for i in range(a):
        for j in range(a):
            if dp[i][k]!=float('inf') and dp[k][j]!=float('inf') and dp[k][k]<0: 
                dp[i][j]=float('-inf')
                next[i][j]=-1 
print(dp)
