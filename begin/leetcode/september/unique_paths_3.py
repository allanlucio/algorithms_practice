class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols = len(grid[0])
        
        free_squares = 0
        begin_row, begin_col = 0,0
        for row in range(0,rows):
            for col in range(0,cols):
                cell = grid[row][col]
                if(cell >= 0): free_squares+=1
                if(cell == 1):
                    begin_row,begin_col = row,col
        
        paths_count = 0
        
        def backtracking(row, col, remain):
            nonlocal paths_count
            
            if(remain == 1 and grid[row][col]==2):
                paths_count+=1
                return
            
            tempCell = grid[row][col]
            grid[row][col]=-10
            remain-=1
            
            for trow, tcol in [(0,1),(1,0),(0,-1),(-1,0)]:
                nrow, ncol = row+trow,col+tcol
                
                if(not (0<=nrow<rows and 0 <= ncol < cols) or grid[nrow][ncol] < 0):
                    continue
                
                backtracking(nrow,ncol,remain)
            grid[row][col]= tempCell
        
        backtracking(begin_row,begin_col,free_squares)
        
        return paths_count
