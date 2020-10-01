class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        agregator=1
        
        product=0
        left=0
        index=0
        for num in nums:
            if(index==0):
                product=num
            else:
                product*=num
            
            if(product>=k):
                while(left < index and product>=k):
                    agregator-=1
                    product/=nums[left]
                    left+=1
            if(agregator == 0):
                agregator=1
            if(product < k):
                count += agregator
                agregator+=1
                
            
            index+=1
        
        return count
        
            
            
