import sys

N=int(input())
K=int(input())

arr=[[0]*N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1]=1

L=int(input())

g=[[0, 0]]*10000

for i in range(L):
    x, c=input().split()
    game[i]=[int(x), c]

