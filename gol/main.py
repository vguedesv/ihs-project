from board import Board
from utils import readButtons, setDisplay

def main():
    #assume the user types in a number
    print('Seja bem-vindo')
    user_rows = int(input('Quantas linhas? '))
    user_columns = int(input('Quantas colunas? '))

    strNumber = str(user_rows) + str(user_columns)
    setDisplay('left', strNumber)

    # create a board:
    game_of_life_board = Board(user_rows,user_columns)

    #run the first iteration of the board:
    game_of_life_board.draw_board([-1, -1])
    #game_of_life_board.update_board()

    userAction = ''
   
    while userAction != 'esc':
        print('Empurre a alavanca 2 para avançar de geração')
        print('Pressione os botões de esquerda e direita simultaneamente para sair')
        userAction = readButtons()

        if userAction == '':
            game_of_life_board.update_board()
            livingCells = game_of_life_board.count_live_cells()
            print(livingCells)
            setDisplay('right', livingCells.zfill(4))
            game_of_life_board.draw_board([-1, -1])


main()