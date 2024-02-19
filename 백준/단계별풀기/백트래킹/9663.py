def is_promising(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i): # 같은열에 있는지 같은 대각선에 있는지
            return False
    
    return True

def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다 가정하고 탐색
            col[x] = i
            if is_promising(x):
                dfs(x+1)

n = int(input())
ans = 0
col = [0] * n # col[k] : k번째 행(row)에서 퀸이 놓여있는 열(col)의 위치

dfs(0)
print(ans)


















