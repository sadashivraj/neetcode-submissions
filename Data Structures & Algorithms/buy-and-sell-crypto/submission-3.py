class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        B, S, profit = 0, 1, 0

        while S < len(prices):
            if prices[B] < prices[S]:
                profit = max(profit, prices[S]-prices[B])
            else:
                B=S
            S += 1
        return profit

                
            
            
            

        
        
        return profit


            

            

        