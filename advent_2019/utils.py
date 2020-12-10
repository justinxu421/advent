def print_grid(grid):
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

def print_grid_levels(grid):
	levels = [x[2] for x in grid]
	rows = [x[0] for x in grid]
	cols = [x[1] for x in grid]
	min_col, max_col = min(cols), max(cols)
	min_row, max_row = min(rows), max(rows)

	for l in range(min(levels), max(levels)+1):
		print(l)
		for row in range(min(rows), max(rows)+1):
			r_str = [' ']*(max_col-min_col+1)
			for point in grid:
				if point[0] == row and point[2] == l:
					r_str[point[1] - min_col] = str(grid[point])
			print(''.join(r_str))
	print()