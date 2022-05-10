from board import Board

def main():
    #assume the user types in a number
    user_rows = int(input('Quantas linhas? '))
    user_columns = int(input('Quantas colunas? '))

    # create a board:
    game_of_life_board = Board(user_rows,user_columns)

    #run the first iteration of the board:
    game_of_life_board.draw_board([-1, -1])
    #game_of_life_board.update_board()

    user_action = ''
    while user_action != 'q':
        user_action = input('Pressione ENTER para avançar uma geração ou Q para sair')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board([-1, -1])


main()