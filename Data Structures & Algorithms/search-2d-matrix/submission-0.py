class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search all the first and last elements of the rows, and once we find correct row binary search the elts in that row
        rowLen = len(matrix)
        colLen = len(matrix[0])
        #we want to find the middle row first.
        
        lp = 0
        rp = rowLen - 1
        #use <= to ensure when they are equal that row is still being checked
        while lp <= rp:
            #use the midpoint method
            mRow = (rp + lp) // 2
            #check if this is the elt
            if matrix[mRow][0] == target or matrix[mRow][colLen - 1] == target:
                return True
            elif matrix[mRow][0] > target:
                rp = mRow - 1
            elif matrix[mRow][colLen - 1] < target:
                lp = mRow + 1
            else:
                #the target should be between this range
                l = 0
                r = colLen - 1
                while l <= r:
                    #binary search on this array
                    c = (r+l)//2
                    if matrix[mRow][c] == target:
                        return True
                    elif matrix[mRow][c] < target:
                        l = c+1
                    else:
                        r = c - 1
                return False
        return False



        
        #check the first and last elt of this mRow, if target is smaller than first or larger than last, move accordingly
