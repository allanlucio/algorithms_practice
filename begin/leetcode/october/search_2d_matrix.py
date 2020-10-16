class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flat_list=[]
        for row in matrix:
            for col in row:
                flat_list.append(col)
                
        def bs(nums, target, begin, end):
            
            chosed=(begin+end)//2
            
            if(chosed<begin or chosed>end): return -1
            if(nums[chosed]==target): return chosed
            
            if(target < nums[chosed]):
                return bs(nums,target,begin,chosed-1)
            else:
                return bs(nums,target,chosed+1,end)
            
        if(bs(flat_list, target,0,len(flat_list)-1)==-1):
            return False
        else:
            return True
