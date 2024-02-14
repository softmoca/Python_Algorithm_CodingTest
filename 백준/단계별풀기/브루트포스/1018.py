n,m=map(int,input().split())

arr=[list(map(str,input())) for _ in range(n)]
arr1=[[0]*m for _ in range(n)]
ch=[[0]*m for _ in range(n)]
ch1=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr1[i][j]=arr[i][j]

arr[0][0]='B'
for i in range(n):
    if i%2==0 and arr[i][0]=='W':
        ch[i][0]=1
        arr[i][0]='B'
    if i%2==1 and arr[i][0]=='B':
        ch[i][0]=1
        arr[i][0]='W'        
        

    for j in range(1,m):
        if arr[i][j-1]==arr[i][j]:
            ch[i][j]=1
            if arr[i][j]=='B':
                arr[i][j]='W'
            else:
                arr[i][j]='B'

Minn=100000
for i in range(n-8+1):
    for j in range(m-8+1):
        S=0
        for k in range(8):
            S=S+sum(ch[k+i][j:j+8])
        if S<Minn:
            Minn=S

arr1[0][0]='W'
for i in range(n):
    if i%2==0 and arr1[i][0]=='B':
        ch1[i][0]=1
        arr1[i][0]='W'
    if i%2==1 and arr1[i][0]=='W':
        ch1[i][0]=1
        arr1[i][0]='B'        
        
    for j in range(1,m):
        if arr1[i][j-1]==arr1[i][j]:
            ch1[i][j]=1
            if arr1[i][j]=='B':
                arr1[i][j]='W'
            else:
                arr1[i][j]='B'

for i in range(n-8+1):
    for j in range(m-8+1):
        S=0
        for k in range(8):
            S=S+sum(ch1[k+i][j:j+8])
        if S<Minn:
            Minn=S

print(Minn)



############


n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

def count_changes(board):
    min_changes = float('inf')
    for start_color in ['B', 'W']:
        changes = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] != start_color:
                    changes += 1
                start_color = 'W' if start_color == 'B' else 'B'
            start_color = 'W' if start_color == 'B' else 'B'
        min_changes = min(min_changes, changes)
    return min_changes

min_changes = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        sub_board = [row[j:j+8] for row in arr[i:i+8]]
        min_changes = min(min_changes, count_changes(sub_board))

print(min_changes)

