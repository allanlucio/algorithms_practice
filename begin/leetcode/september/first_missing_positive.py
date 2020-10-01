class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        candidate=1
        for num in nums:
            if(candidate==num):
                candidate+=1
        
        return candidate
            
