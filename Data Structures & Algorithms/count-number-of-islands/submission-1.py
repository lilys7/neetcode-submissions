class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        num = 0
        r, c = 0, 0
        rowLen = len(grid)
        colLen = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                r,c = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    #if we find a valid extension of the island, 
                    if row in range(rowLen) and col in range(colLen) and (row, col) not in visited and grid[row][col] == '1':
                        q.append((row,col))
                        visited.add((row,col))
            


        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    num += 1
                
        return num
