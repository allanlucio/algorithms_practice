class Solution:
    n=0
    dic = []
    s="";
    dp=[]
    
    def solve(self, idx):
        if(idx == self.n): return True
        if(self.dp[idx] != -1): return self.dp[idx]
        res = False
        index=0
        
        for word in self.dic:
            k = len(word)
            
            if(word == self.s[idx:idx+k]):
                res = res or self.solve(idx+k)
                
            index+=1
        
        self.dp[idx]=res
        return self.dp[idx]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.n=len(s)
        self.s = s
        self.dic=wordDict
        self.dp=[-1 for a in range(0,self.n)]
        
        
        return self.solve(0)
