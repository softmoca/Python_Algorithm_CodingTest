def solution(moves):
    x = y = 0
    for k in moves:
        if k=='U':
            x=x-1
        elif k=='R':
            y=y+1
        elif k=='D':
            x=x+1
        elif k=='L':
            y=y-1


    
    return [x, y]
                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
