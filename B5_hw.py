rotated_list = []
# main_diagonal = []
# diagonal = []
winner = ''

def create_field(size):
    if size < 3:
        print('Минимальное поле 3х3')
        return
    else:
        return [['-' for _ in range(size)] for _ in range(size)]

def output_field(field):
    indexes = [' ']
    for i in range(len(field)):
        indexes.append(i)
    print(*indexes)
    indexes.pop(0)
    for x,y in zip(indexes,field):
        print(str(x),*y)

def check_step(step, field, rem_of_div):
    field_size = len(field)

    if len(step) != 2:
        print('Введите две координаты для хода')
    elif not (type(step[0]) is int and type(step[1]) is int):
        print('Координаты должны быть целыми числами')
    elif step[0] > field_size-1 or step[1] > field_size-1:
        print(f'Ход за границу поля. Размер поля {field_size}x{field_size}, нумерация с "0"')
    elif field[step[0]][step[1]] != '-':
        print('Позиция занята')
    else:
        if rem_of_div == 0:
            mark = 'o'
        else:
            mark = 'x'
        accept_the_step(step, field, mark)
        output_field(field)
        _winner(field, mark)
        return True

def _winner(field, mark):
    global rotated_list
    global diagonals
    global main_diagonal
    global winner

    def chek_out(f):
        for item in f:
            equals_cells = 0
            for item_item in item:
                if item_item == mark:
                    equals_cells += 1
                if equals_cells == len(field):
                    return True

    rotated_list = [*zip(*field)]
    # Не понял как корректно обработать диагонали матрицы без подключения модуля Numpy

    if chek_out(field) or chek_out(rotated_list):
        winner = mark


def accept_the_step(st, f, m):
    f[st[0]][st[1]] = m

# Основная программа:
f_size = int(input('Введите размер игрового поля:'))
game_field = create_field(f_size)
rotated_list = game_field.copy()
output_field(game_field)
step_counter = 1

while True:
    division2 = step_counter % 2
    current_step = list(map(int,input('Ваш ход:').split()))
    if check_step(current_step, game_field, division2):
        if winner != '':
            print(f'Выиграли  {winner}')
            break
        else:
            step_counter += 1
    else:
        continue




