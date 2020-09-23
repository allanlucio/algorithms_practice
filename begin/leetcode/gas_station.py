class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index=0
        size=len(gas)
        current=-1
        balance=0
        while True:
            balance+=gas[index%size]-cost[(index)%size]
            
            if(balance >=0 and current==-1):
                current = index%size
            elif(balance<0):
                current=-1
                balance=0
            
            index+=1
            if((index>size and current==-1)): 
                current=-1
                break
            elif(index%size == current): 
                break
        
        
        
        return current
