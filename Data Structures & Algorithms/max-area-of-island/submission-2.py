class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #find all islands bfs and compare their lengths after full island complete
        if not grid:
            return 0
        
        largest = 0
        visit = set()
        rowLen = len(grid)
        colLen = len(grid[0])

        def bfs(islandSize, r,c):
            q = collections.deque()
            visit.add((r,c))
            #while q has length, that means parts of the island exist
            q.append((r,c))
            while q:
                #queue is FIFO, so we remove the first element
                r, c = q.popleft()
                #north east south west
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    #if valid and is an island and we haven't visited yet, add to visited and queue
                    if row in range(rowLen) and col in range(colLen) and grid[row][col] == 1 and (row, col) not in visit:
                        
                        islandSize += 1
                        visit.add((row,col))
                        q.append((row,col))
            nonlocal largest
            largest = max(largest, islandSize)
            


        for r in range(rowLen):
            for c in range(colLen):
                #do bfs on the cell if island
                if grid[r][c] == 1 and (r,c) not in visit:
                    islandSize = 1
                    bfs(islandSize, r,c)
                    
                    

        return largest
