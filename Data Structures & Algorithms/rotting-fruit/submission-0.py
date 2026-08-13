class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs implementation with queue
        q = collections.deque()
        rLen = len(grid)
        cLen = len(grid[0])
        fresh, time = 0, 0
        for r in range(rLen):
            for c in range(cLen):
                if grid[r][c] == 1:
                    fresh += 1
                    
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = r+ dr
                    col = c+ dc
                    if row in range(rLen) and col in range(cLen) and grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append((row,col))
            time += 1
        return time if fresh == 0 else -1


