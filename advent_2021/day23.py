from collections import Counter, defaultdict
from functools import cache
import numpy as np
import copy

# make a constant for the spaces that are able to be moved to
SPACES = [
    (1, 1),
    (1, 2),
    (1, 4),
    (1, 6),
    (1, 8),
    (1, 10),
    (1, 11),
]

# all paths are L shaped, so we just traverse from space to room
# space is always on a row higher than the room, so we can make that assumption
def get_path(positions, space, room):
    x1, y1 = space
    x2, y2 = room

    # horizontal
    for y in range(min(y1, y2) + 1, max(y1, y2)):
        if positions.get((x1, y), ".") != ".":
            return False

    # vertical
    for x in range(x1 + 1, x2):
        if positions.get((x, y2), ".") != ".":
            return False

    return abs(y2 - y1) + abs(x2 - x1)


# check if all positions are filled
def check_done(positions, room_mapping):
    for label, rooms in room_mapping.items():
        for room in rooms:
            if positions[room] != label:
                return False

    return True


# find all unfilled rooms that are movable
def get_unfilled(pos, room_mapping):
    def get_first(rooms):
        for start in rooms:
            if pos[start] != ".":
                return start

    valid = set()
    for label, rooms in room_mapping.items():
        for room in reversed(rooms):
            if pos[room] != label:
                first = get_first(rooms)
                if first:
                    assert first not in valid
                    valid.add(first)
                    break

    return valid


# get all the valid moves that go from space to room
def move_space_to_room(p_, scores, room_mapping):
    # see if any space can go into any room
    new_ps = []
    for space in SPACES:
        # check pods
        pod = p_[space]
        if pod != ".":
            rooms = room_mapping[pod]
            for r in reversed(rooms):
                # already filled
                if p_[r] == pod:
                    continue
                # try to move there
                if p_[r] == ".":
                    path_len = get_path(p_, space, r)
                    if path_len:
                        p_copy = copy.deepcopy(p_)
                        # move the pod to the space
                        p_copy[space] = "."
                        p_copy[r] = pod

                        new_ps.append((p_copy, scores[pod] * path_len))
                        break
                else:
                    break

    return new_ps


# get all the valid moves that go from room to unfilled space
def move_room_to_unfilled(p_, scores, room_mapping):
    new_ps = []
    # check all valid pods
    for r in get_unfilled(p_, room_mapping):
        pod = p_[r]
        assert pod != "."
        # check all valid spaces
        for space in SPACES:
            if p_[space] == ".":
                path_len = get_path(p_, space, r)
                if path_len:
                    pass
                    p_copy = copy.deepcopy(p_)
                    # move the pod to the space
                    p_copy[space] = pod
                    p_copy[r] = "."

                    new_ps.append((p_copy, scores[pod] * path_len))

    return new_ps


def get_smallest_path(positions, room_mapping):
    scores = {"A": 1, "B": 10, "C": 100, "D": 1000}
    min_total = float("inf")

    seen = {}
    seen[str(positions)] = 0

    stack = [(positions, 0)]

    while stack:
        p_, total_ = stack.pop()

        if check_done(p_, room_mapping):
            if total_ < min_total:
                min_total = total_
                print(f"new min total is {min_total}")

        # if we can move do into room do it
        room_ps = move_space_to_room(p_, scores, room_mapping)
        unfilled_ps = move_room_to_unfilled(p_, scores, room_mapping)

        if room_ps:
            new_ps = room_ps
        else:
            new_ps = unfilled_ps

        for p_copy, move_val in new_ps:
            new_total = total_ + move_val
            if str(p_copy) not in seen or new_total < seen[str(p_copy)]:
                seen[str(p_copy)] = new_total
                stack.append((p_copy, new_total))

    return min_total


def init_positions(a, rows=2):
    positions = {}
    for coord in SPACES:
        positions[coord] = "."

    room_1 = [(x, 3) for x in range(2, 2 + rows)]
    room_2 = [(x, 5) for x in range(2, 2 + rows)]
    room_3 = [(x, 7) for x in range(2, 2 + rows)]
    room_4 = [(x, 9) for x in range(2, 2 + rows)]

    for coord in room_1 + room_2 + room_3 + room_4:
        positions[coord] = a[coord]

    room_mapping = {
        "A": room_1,
        "B": room_2,
        "C": room_3,
        "D": room_4,
    }

    return positions, room_mapping


def p1(a):
    positions, room_mapping = init_positions(a, 2)
    return get_smallest_path(positions, room_mapping)


def p2(a):
    row1 = "  #D#C#B#A#  "
    row2 = "  #D#B#A#C#  "
    rows = np.array([list(row1), list(row2)])
    b = np.insert(a, 3, rows, 0)
    print(b)

    positions, room_mapping = init_positions(b, 4)
    return get_smallest_path(positions, room_mapping)


def run(file):
    with open(file) as f:
        a = [list(x) for x in f.read().splitlines()]
        a = np.array(a)

        print(f"Part 1: {p1(a)}")
        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input23.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
