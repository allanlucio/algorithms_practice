class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums)/3
        if(limit==0): limit=1
        storage = {}
        for num in nums:
            if(num in storage):
                storage[num]+=1
            else:
                storage[num]=1
        
        result = []
        
        for k,v in storage.items():
            if(v>limit):
                result.append(k)
            
        return result
        
