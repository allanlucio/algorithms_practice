class RecentCounter:

    def __init__(self):
        self.pings=[]
        self.minIndex=0
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        minn=t-3000
        while True:
            ping=self.pings[self.minIndex]
            if(ping>=minn):
                break
                
            self.minIndex+=1
        
        if(self.pings == None):
            return self.pings
        
        return len(self.pings)-self.minIndex
