class GameBoard:

    '''
    Game board object, has two elements, set of the alive cells, and the board size
    if the size is nXn, size = n
    '''

    def __init__(self,live_cells,size):
        self.live_cells = live_cells
        self.size = size

    '''
    Auxilary functions to print the board
    '''
    def format_row(self,row):
        return '|' + '|'.join('{0:^3s}'.format(x) for x in row) + '|'

    
    def format_board(self,board):
        return '\n\n'.join(self.format_row(row) for row in board)
    
    '''
    Prints the game board
    '''
    def print_board(self):
        board = [['.' for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) in self.live_cells:
                    board[i][j] = '*'
        print(self.format_board(board))

        

   
    

    
