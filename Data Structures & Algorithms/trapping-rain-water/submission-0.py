class Solution:
    def trap(self, height: List[int]) -> int:
        #keep a left and right min array and then if the min(L,R) - height is >0, add to sum
        total = 0
        n = len(height)
        l_wall = 0
        r_wall = 0
        leftMax, rightMax = [0] * n, [0] * n
        #this is how we iterate through a list forwards and backwards
        for i in range(n):
            j = -i - 1 #e.g. when i is 0 we are at -1, 1, -2, etc.
            leftMax[i] = l_wall
            rightMax[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            
        #now that we've gotten all values for leftmax and rightmax, iterate again
        for i in range(n):
            potential = min(leftMax[i], rightMax[i]) - height[i]
            if potential > 0:
                total += potential

        return total
            
