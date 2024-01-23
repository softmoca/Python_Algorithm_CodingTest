dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y,board):
    global cnt
    cnt+=1
    board[x][y]=0
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<len(board) and 0<=ny<len(board) and board[nx][ny]==1:
            DFS(nx,ny,board)

cnt=0
def solution(board):
    answer = []
    global cnt

    for i in range(len(board)):
        for j in range(len(board)):
            cnt=0
            if board[i][j]==1:
                DFS(i,j,board)
                answer.append(cnt)
            
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

