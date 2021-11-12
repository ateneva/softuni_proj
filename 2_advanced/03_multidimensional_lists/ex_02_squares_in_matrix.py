

def get_rectangle_matrix(nums):
    dimensions = [int(i) for i in nums.split()]
    rows = dimensions[0]
    matrix = []

    for _ in range(rows):
        matrix_row = [x for x in input().split()]
        matrix.append(matrix_row)
    return matrix


def in_range(pos, size):
    x = pos[0]
    y = pos[1]
    return 0 <= x < size and 0 <= y < size


def get_current_position(matrix):
    current_position = []
    for m in matrix:
        for position in m:
            current_position = [matrix.index(m), m.index(position)]
    return current_position


def one_item_right(current_position):
    row = current_position[0]
    column = current_position[1] + 1
    one_right = [row, column]
    return one_right


def one_item_down(current_position):
    row = current_position[0] + 1
    column = current_position[1]
    one_down = [row, column]
    return one_down


def one_item_across(current_position):
    row = current_position[0] + 1
    column = current_position[1] + 1
    one_across = [row, column]
    return one_across


matrix_size = input()
original_matrix = get_rectangle_matrix(matrix_size)
print(original_matrix)

rows_count = len(original_matrix)
columns_count = len(original_matrix[0])
equal_matrices = []

for row_item in original_matrix:
    value_right = ''
    value_down = ''
    value_across = ''

    print(row_item)
    for r in row_item:
        r_coordinates = get_current_position(original_matrix)
        right = one_item_right(r_coordinates)
        down = one_item_down(r_coordinates)
        across = one_item_across(r_coordinates)

        print(f'{r} --> {r_coordinates} --> {right},{down}{across}')

        '''

        value_right = original_matrix[right[0]][right[1]]
        value_down = original_matrix[down[0]][down[1]]
        value_across = original_matrix[across[0]][across[1]]

        print(f'{r} --> {r_coordinates} --> {value_right},{value_down}{value_across}')
        
        '''