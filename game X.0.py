user_1 = input("Игрок 1 введите своё имя:")
user_2 = input("Игрок 2 введите своё имя:")

field_numbers = [i for i in range(1, 10)]
winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                        [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def draw_field():
    print('-' * 13)
    for i in range(3):
        print('|', field_numbers[0 + i * 3], '|', field_numbers[1 + i * 3], '|',
              field_numbers[2 + i * 3], '|')
        print('-' * 13)


moves_X = []
moves_O = []


def players_move_1():
    print(f'Ходит {user_1}.')
    while True:
        num_X = input('Куда ставить X? ')
        if num_X not in "123456789":
            print("Некорректный ввод. Введите число.")
            continue
        num_X = int(num_X)
        if num_X in moves_X or moves_O:
            print("Ячейка занята.")
            continue
        field_numbers[int(num_X) - 1] = "X"
        moves_X.append(int(num_X))
        break


def players_move_2():
    print(f'Ходит {user_2}.')
    while True:
        num_O = input('Куда ставить O? ')
        if num_O not in "123456789":
            print("Некорректный ввод. Введите число.")
            continue
        num_O = int(num_O)
        if num_O in moves_X or moves_O:
            print("Ячейка занята.")
            continue
        field_numbers[int(num_O) - 1] = "O"
        moves_X.append(int(num_O))
        break


def check_for_victory():
    for win_comb in winning_combinations:
        if field_numbers[win_comb[0]-1] == field_numbers[win_comb[1]-1] == \
                field_numbers[win_comb[2]-1] == "X":
            return f"Игрок {user_1} победил!"
        if field_numbers[win_comb[0]-1] == field_numbers[win_comb[1]-1] == \
                field_numbers[win_comb[2]-1] == "O":
            return f"Игрок {user_2} победил!"



def main():
    print("Привет")
    print(f"Игрок 1:\n {user_1}")
    print(f"Игрок 2:\n {user_2}")
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            players_move_1()
        else:
            players_move_2()
        if counter > 3:
            winner = check_for_victory()
            if winner:
                draw_field()
                print(winner)
                break
        counter += 1
        if counter > 8:
            draw_field()
            print("Ничья!")
            break


if __name__ == '__main__':
    main()