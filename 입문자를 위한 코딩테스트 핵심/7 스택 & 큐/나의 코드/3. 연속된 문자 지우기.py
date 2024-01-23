def solution(s):
    answer = ""
    stack=[]
    stack.append(s[0])

    for i in range(1,len(s)):
        if stack and stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    return answer.join(map(str,stack))

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
