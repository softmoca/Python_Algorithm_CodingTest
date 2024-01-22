def solution(n, moves): 
    x = y = 0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    dir=['U','R','D','L']

    for z in moves:
        for k in range(4):
            if z==dir[k]:
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    x=nx
                    y=ny
 
    return [x, y]    
                
                      
print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))

