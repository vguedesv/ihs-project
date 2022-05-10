'''
Game of Life
Cell class
Martin A. Aaberge
'''

class Cell:
    def __init__(self):
        '''
        Class holding init status of cell (dead).
        Ability to set- and fetch new statuses with functions
        '''
        self._status = 'Dead'

    def set_dead(self):
        '''
        method sets the cell status to DEAD
        '''
        self._status = 'Dead'

    def set_alive(self):
        '''
        method sets the cell status to ALIVE
        '''
        # print('ficando viva...')
        self._status = 'Alive'

    def is_alive(self):
        '''
        method checks if the cell is ALIVE
        returns True if it is alive, False if not.
        '''
        if self._status == 'Alive':
            return True
        return False

    def get_print_character(self, actualCoord, underlineCoord):
        '''
        method returning a status character of our choice to print on the board
        '''
        # print(actualCoord)
        # print(underlineCoord)
        # print("This is bold text looks like:",'\033[1m' + 'Python' + '\033[0m')
        if actualCoord[0] == underlineCoord[0] and actualCoord[1] == underlineCoord[1]: # trata-se da coordenada selecionada
            if self.is_alive():
                return "_"
            return "_"
        
        if self.is_alive():
            return '*'
        return '.'