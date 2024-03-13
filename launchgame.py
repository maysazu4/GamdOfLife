import collections


NEIGHBORS = ((-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1))

'''
Returns a dictionary in which for each cell the num of live neighbors cells
'''
def get_neighbors_num_dict(live_cells):
    # For every cell(dead or live) calculate the number of live cells it neighbors.
    
    neighbors_num = collections.defaultdict(int)
    for cell_row,cell_col in live_cells:
        if (cell_row,cell_col) not in neighbors_num.keys():
            neighbors_num[(cell_row,cell_col)] = 0
        for row, col in NEIGHBORS:
            neighbor_cell = (cell_row + row, cell_col + col)
            neighbors_num[neighbor_cell] += 1
    return neighbors_num


'''
Update live cells and dead cells
'''
def update_live_cells(live_cells):
    neighbors_num = get_neighbors_num_dict(live_cells)
    for cell, num in neighbors_num.items():
        # remove cells that dead as a result of underpopulation or overpopulation
        if cell in live_cells:
            if num < 2 or num > 3:
                live_cells.remove(cell)
        # add the cells that becomes a live cell.
        else:
            if num == 3:
                live_cells.add(cell)
    return live_cells



'''
Launch game, each round calls the "update_live_cells" function
'''
def launch_game(board, rounds_num):
    board.print_board()
    print('\n')
    for i in range(rounds_num):
        print('Round ', i + 1)
        board.live_cells = update_live_cells(board.live_cells)
        board.print_board()
        print('\n\n')





