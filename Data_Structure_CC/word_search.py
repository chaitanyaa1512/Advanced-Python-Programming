# Python program to search a word in a 2D word puzzle (5x5 matrix):
class WordSearch:
   
    def __init__(self):
        self.Row = None
        self.Col = None
        self.dir = [[-1, 0], [1, 0], [1, 1],[1, -1],
                    [-1, -1], [-1, 1],[0, 1], [0, -1]]
                   
    def search2D(self, grid, row, col, word):
       
        if grid[row][col] != word[0]:
            return False
           
        for x, y in self.dir:

            rd, cd = row + x, col + y
            flag = True
           
       
            for k in range(1, len(word)):
               
               
                if (0 <= rd <self.Row and
                    0 <= cd < self.Col and
                    word[k] == grid[rd][cd]):
                   
           
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
           
           
            if flag:
                return True
        return False
       

    def patternSearch(self, grid, word):
       
        self.Row = len(grid)
        self.Col = len(grid[0])
       
        for row in range(self.Row):
            for col in range(self.Col):
                if self.search2D(grid, row, col, word):
                    print("pattern found at " +
                        str(row +1) + ', ' + str(col+1))
                   
if __name__=='__main__':
    grid = ["AWPFE",
            "XIILZ",
            "NCRAF",
            "CEGGU",
            "MQSTN"]
    w_search = WordSearch()
    w_search .patternSearch(grid, 'FLAG')
    print('')
    w_search .patternSearch(grid, 'EGG')
