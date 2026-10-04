import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #binary search from 1 to the max of the piles
        #the moment we get above the hour mark, return the value + 1
        #minimum is gonna be the sum / h
        total = sum(piles)
        lp=1
        
        rp = max(piles) #maximum rate
        res = rp
        while lp <= rp:
            c = (lp + rp) // 2
            hours = 0
            for b in piles:
                hours += (b+c-1)//c
            if hours <= h:
                res = min(res, c)
                rp = c - 1
            else:
                lp = c + 1
        return res
        #62 // 4 = 15 minimum
