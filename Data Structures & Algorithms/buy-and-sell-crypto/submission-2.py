class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        maxProf = 0
        while rp < len(prices):
            if prices[lp] < prices[rp]:
                diff = prices[rp] - prices[lp]
                if diff > maxProf:
                    maxProf = diff
                rp += 1
            else:
                lp = rp
                rp += 1
        return maxProf
         
            
