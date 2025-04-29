class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(board,row,col):
            for i in range(row):
                if board[i] == col or abs(board[i]-col) == row-i:
                    return False
            return True
        
        def solve(row,board):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_safe(board,row,col):
                    board[row] = col
                    count += solve(row+1,board)
            return count
        return solve(0,[-1]*n)