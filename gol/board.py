
from cell import Cell
from random import randint
# import keyboard
from utils import readButtons

class Board:
    def __init__(self , rows , columns):
        '''
        constructor holds input from user and populates the grid with cells. 
        '''
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._generate_board()

    def draw_board(self, underlineCoord):
        '''
        method that draws the actual board in the terminal
        '''
        print('\n'*5)
        # print('Novo campo')
        for indexR, row in enumerate(self._grid):
            for indexC, column in enumerate(row):
                actualCoord = [indexR, indexC]
                print (column.get_print_character(actualCoord, underlineCoord),end='')
                # print (indexR, indexC)
            print () # to create a new line pr. row.

    def count_live_cells(self):
        count = 0
        for row in self._grid:
            for column in row:
                if column.is_alive:
                    count += 1
        return count

    def _generate_board(self):
        '''
        method that sets the random state of all cells.
        '''
        userInput = ''
        underlineCoord = [0, 0]
        while(userInput != 'enter'):
            # print(userInput)
            if userInput =='right':
                underlineCoord[1] = (underlineCoord[1] + 1) % self._columns
            if userInput =='left':
                underlineCoord[1] = (underlineCoord[1] - 1) % self._columns
            if userInput =='up':
                underlineCoord[0] = (underlineCoord[0] - 1) % self._rows
            if userInput =='down':
                underlineCoord[0] = (underlineCoord[0] + 1) % self._rows  
            if userInput =='space':
                selectedCell = self._grid[underlineCoord[0]][underlineCoord[1]]
                if selectedCell.is_alive():
                    selectedCell.set_dead()
                else:
                    selectedCell.set_alive()
                # print(selectedCell.is_alive())
            # print(underlineCoord )
            self.draw_board(underlineCoord)
            userInput = readButtons()


        # for row in self._grid:
        #     for column in row:
        #         #there is a 33% chance the cells spawn alive.
        #         chance_number = randint(0,2)
        #         if chance_number == 1:
        #             column.set_alive()

    def update_board(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                #check neighbour pr. square:
                check_neighbour = self.check_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                #If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        #sett cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    
    
    def check_neighbour(self, check_row , check_column):
        '''
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update 
        method can set the new status
        '''        
        #how deep the search is:
        search_min = -1
        search_max = 2

        #empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column 
                
                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list