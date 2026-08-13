class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        #use two pointers
        lp = 0
        rp = 1
        while lp < rp and rp < len(prices):
            if prices[lp] < prices[rp]:
                maxPrice = max(maxPrice, prices[rp] - prices[lp])
                rp += 1
            else:
                lp = rp
                rp += 1
        return maxPrice