class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        index=0
        while index<k:
            removed=nums.pop()
            nums.insert(0,removed)
            
            index+=1
        
        return nums
