def parse_step(step):
    direction = step[0]
    distance = int(step[1:])
    return direction, distance


def move_distance(curr, direction, distance):
    if direction == 'U':
        return (curr[0], curr[1] + distance)
    elif direction == 'R':
        return (curr[0] + distance, curr[1])
    elif direction == 'D':
        return (curr[0], curr[1] - distance)
    elif direction == 'L':
        return (curr[0] - distance, curr[1])


# using current position and the step update teh grid
def update_grid(step, curr, grid, total_steps):
    direction, distance = parse_step(step)

    # get points by moving distance
    for i in range(distance):
        new_point = move_distance(curr, direction, i + 1)
        # only add in if not already there
        if new_point not in grid:
            grid[new_point] = total_steps + i + 1

    return move_distance(curr, direction, distance), total_steps + distance


def run_map(arr):
    total_steps = 0
    curr = (0, 0)
    # position tuple and then the number of steps
    grid = {(0, 0): 0}
    for step in arr:
        curr, total_steps = update_grid(step, curr, grid, total_steps)
    return grid


def run_maps(arr1, arr2):
    grid1 = run_map(arr1)
    grid2 = run_map(arr2)

    intersections = grid1.keys() & grid2.keys()
    intersections.remove((0, 0))

    manhattans = []
    total_wire_distances = []
    for point in intersections:
        manhattans.append(abs(point[0]) + abs(point[1]))
        total_wire_distances.append(grid1[point] + grid2[point])
    print(min(total_wire_distances))


def main():
    with open('input3.txt') as f:
        arr1 = f.readline().strip().split(',')
        arr2 = f.readline().strip().split(',')
        return run_maps(arr1, arr2)


if __name__ == "__main__":
    main()
