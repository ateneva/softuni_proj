
'''
Create a function called get_magic_triangle which will receive a single parameter
 (integer n) and it should create a magic triangle which follows those rules:
    - start with this simple triangle [[1], [1, 1]]
    - generate the next rows until we reach n amount of rows
    - Each number in each row is equal to the sum of the two numbers right above it in the triangle
    - If the current number has no neighbor to the upper left/rigth, just take the existing neighbor

'''

def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row in range(2, n):
        new_row = []
        for col in range(0, row + 1):
            if col - 1 < 0:
                new_row.append(1)
            elif col >= len(triangle[row-1]):
                new_row.append(1)
            else:
                upper_left = triangle[row - 1][col - 1]
                upper_right = triangle[row - 1][col]
                new_box = upper_left + upper_right
                new_row.append(new_box)

        triangle.append(new_row)
    return triangle

print(get_magic_triangle(6))
