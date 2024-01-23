def solution(nums, k):
    answer = 0
    Sl=len(nums)-k
    Minn=100
    p1=0
    p2=p1+Sl
    while p2!=len(nums)+1:
        if sum(nums[p1:p2])<Minn:
            Minn=sum(nums[p1:p2])
            print(p1,p2)
        p1+=1
        p2+=1

    answer=sum(nums)-Minn
    

    return answer
        
                                         
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
