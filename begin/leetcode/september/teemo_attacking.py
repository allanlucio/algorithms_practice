class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if(len(timeSeries)==0): return 0
        total=duration
        last_time=timeSeries[0]
        for time in timeSeries:
            total += min(time-last_time,duration)
            
            
            last_time=time
        
        return total
