from collections import defaultdict
def solution(nums):
    answer = -1
    MM=0
    dic=defaultdict()
    for x in nums:
        if x in dic:
            dic[x]=2
        else:
            dic[x]=1
    for key in dic:
        if dic[key]==1:
            if MM< key:
                MM=key


       
    return -1 if MM==0 else MM
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
