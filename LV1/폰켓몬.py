def solution(nums):
    #최대 len(nums)/2 의 종류만큼을 가짐, 즉 nums에 다른 원소의 종류가 len(nums)/2 이상이라면 len(nums)/2종류 만큼 가짐 아니면 다른원소의 종류만큼!
    if len(set(nums)) >= len(nums) // 2:
        return len(nums) // 2
    else :
        return len(set(nums))
    
