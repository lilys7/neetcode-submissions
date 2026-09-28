class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                elt = board[r][c]
                if elt != ".":
                    if elt in row[r] or elt in col[c] or elt in box[(r//3, c//3)]:
                        return False
                    else:
                        row[r].add(elt)
                        col[c].add(elt)
                        box[(r//3,c//3)].add(elt)
        return True

