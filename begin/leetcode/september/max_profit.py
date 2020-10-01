class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 0): return 0
        m=prices[0]
        
        profit=0
        
        
        for price in prices:
            profit = max(profit,price-m)
            m = min(price,m) 
           
        
        return profit