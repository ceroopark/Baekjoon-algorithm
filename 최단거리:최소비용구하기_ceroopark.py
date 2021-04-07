import sys
 
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
INF=sys.maxsize

a=[[INF for _ in range(n+1)] for _ in range(n+1)]
 
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    a[a][b]=min(c,a[a][b])
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                a[i][j]=0
            else:
                a[i][j]=min(a[i][j],a[i][k]+a[k][j])
 
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]==INF:
           print(0,end=" ")
        else:
           print(a[i][j],end=" ")
    print()
