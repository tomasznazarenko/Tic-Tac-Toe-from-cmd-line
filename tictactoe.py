empty_field = "_________"
cells = [cell for cell in empty_field]
columns_count = 3
cells_count = 9
field = [cells[i:i+columns_count] for i in range(0, cells_count, columns_count)]


def print_field(field):
    print("---------")
    print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
    print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
    print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
    print("---------")


def has_won(field, sign):
    for i in range(3):
        if field[i] == [sign, sign, sign]:
            return True
        if [cell[i][0] for cell in field] == [sign, sign, sign]:
            return True

    if [field[0][0], field[1][1], field[2][2]] == [sign, sign, sign]:
        return True
    if [field[2][0], field[1][1], field[0][2]] == [sign, sign, sign]:
        return True

    return False


def has_empty_cells(field):
    return "_" in [cell for cells in field for cell in cells ]


def is_game_finished(field):
    return has_won(field, "X") or has_won(field, "O") or has_empty_cells(field) == False


def is_draw(field):
    return has_won(field, "X") == False and has_won(field, "O") == False and has_empty_cells(field) == False


def count_sign(sign, field):
    return len([cell for cells in field for cell in cells if cell == sign])


def is_impossible(field):
    if has_won(field, "X") and has_won(field, "O"):
        return True

    sign_count_difference = count_sign("X", field) - count_sign("O", field)
    if sign_count_difference >= 2 or sign_count_difference <= -2:
        return True

    return False


def is_cell_empty(coordinates, field):
    x, y = coordinates
    return "_" in field[y][x]


def put_sign(sign, coordinates, field):
    x, y = coordinates
    field[y][x] = sign
    

def translate_to_field_coordinates(coordinates):
    x, y = coordinates
    translated_x = x - 1
    translated_y = 0
    if y == 1:
        translated_y = 2
    elif y == 2:
        translated_y = 1
    if y == 3:
        translated_y = 0
    return translated_x, translated_y


def is_input_valid(inp):
    valid_values = ["1", "2", "3"]
    return inp[0] in valid_values and inp[1] in valid_values


def ask_for_coordinates():
    coordinates = 4, 4
    valid = False

    inp = input("Enter the coordinates: ").split()

    if is_input_valid(inp):
        entry = tuple(int(n) for n in inp)
        valid = True
        coordinates = translate_to_field_coordinates(entry)

    while not valid:
        if not inp[0].isdigit() or not inp[0].isdigit():
            print("You should enter numbers!")
        else:
            print("Coordinates should be from 1 to 3!")
        inp = input("Enter the coordinates: ").split()
        if is_input_valid(inp):
            entry = tuple(int(n) for n in inp)
            valid = True
            coordinates = translate_to_field_coordinates(entry)

    return coordinates


def can_put_sign_at(coordinates, field):
    if is_cell_empty(coordinates, field):
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False


def next_sign_to_put(current_sign):
    return "O" if current_sign == "X" else "X"


current_sign = "X"

print_field(field)

while not is_game_finished(field):
    coordinates = ask_for_coordinates()
    if can_put_sign_at(coordinates, field):
        put_sign(current_sign, coordinates, field)
        current_sign = next_sign_to_put(current_sign)
        print_field(field)

if is_draw(field):
    print("Draw")
elif has_won(field, "X"):
    print("X wins")
elif has_won(field, "O"):
    print("O wins")
