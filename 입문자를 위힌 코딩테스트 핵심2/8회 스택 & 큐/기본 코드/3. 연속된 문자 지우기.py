def solution(s):
    answer = ""
    stack=[]

    for x in s:
        
            if  stack and stack[-1]==x:
                stack.pop()
                continue
            else:
                 stack.append(x)
        
            
    return answer.join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
