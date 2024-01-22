def solution(board):
    answer = 0
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
  
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                for k in range(8):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<len(board) and 0<=ny<len(board) and board[nx][ny]==0:
                        board[nx][ny]=2
                        answer+=1
    
    
    return answer
                       
print(solution([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0]]))
