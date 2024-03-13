'''
Gets and returns the user parameters: the alive cells,board size and number of rounds
'''
def get_user_input():
    print('\n')
    print('Welcome to "Game Of Life"...')
    row_size = int(input('Please enter the board row size: '))
    print('Please choose the cells you want to populate, enter the number of row then number of col')
    live_cells = set()
    while(True):
        row = int(input('Enter number of row from 0 to {}:'.format(row_size -1)))
        col = int(input('Enter number of column from 0 to {}:'.format(row_size-1)))
        if row not in range(0,8) or col not in range(0,8):
            print("Number not in range, please try again!\n")
            continue
        live_cells.add((row,col))
        x = input('When you finish press (q) ')
        if x == 'q':
            break
    rounds = int(input('Please enter number of rounds:'))
    return live_cells,rounds,row_size