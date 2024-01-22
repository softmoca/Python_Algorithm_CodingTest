from collections import Counter
def solution(s):
    answer = 0
    CC=Counter(s)
    cnt=0
    for x in CC:
        if CC[x]%2==1:
            cnt+=1
    if cnt >1:
        answer=len(s)-(cnt-1)
    else:
        answer=len(s)


    return answer
    
                
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
