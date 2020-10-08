class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(nums, target, begin, end):
            
            chosed=(begin+end)//2
            
            if(chosed<begin or chosed>end): return -1
            if(nums[chosed]==target): return chosed
            
            if(target < nums[chosed]):
                return bs(nums,target,begin,chosed-1)
            else:
                return bs(nums,target,chosed+1,end)
        
        return bs(nums, target,0,len(nums)-1)
