import numpy as np
def print_points(grid, transpose = False):
    if transpose:
        grid = {(y,x): '#' for (x,y) in grid}
    else:
        grid = {(x,y): '#' for (x,y) in grid}

    rows = [x[0] for x in grid]
    cols = [x[1] for x in grid]
    min_col, max_col = min(cols), max(cols)
    min_row, max_row = min(rows), max(rows)

    for row in range(min(rows), max(rows)+1):
        r_str = [' ']*(max_col-min_col+1)
        for point in grid:
            if point[0] == row:
                r_str[point[1] - min_col] = str(grid[point])
        print(''.join(r_str))

def print_grid(points, transpose = False):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    arr = np.full((max_x+1, max_y+1), ' ', dtype='str')
    for p in points:
        arr[p] = '#'

    if transpose:
        arr = arr.T

    for row in arr.T:
        print(''.join(row))