from collections import Counter, defaultdict
from functools import cache
import numpy as np
import copy


def get_path(positions, space, room):
    x1, y1 = space
    x2, y2 = room

    for y in range(min(y1, y2) + 1, max(y1, y2)):
        if positions.get((x1, y), ".") != ".":
            return False

    for x in range(x1 + 1, x2):
        if positions.get((x, y2), ".") != ".":
            return False

    return abs(y2 - y1) + abs(x2 - x1)


SPACES = [
    (1, 1),
    (1, 2),
    (1, 4),
    (1, 6),
    (1, 8),
    (1, 10),
    (1, 11),
]


def check_done(positions, room_mapping):
    for label, rooms in room_mapping.items():
        for room in rooms:
            if positions[room] != label:
                return False

    return True


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


def check_spaces(p_, scores, room_mapping):
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
        new_ps = check_spaces(p_, scores, room_mapping)
        if new_ps:
            for p_copy, move_val in new_ps:
                # print("moving", p_copy)
                new_total = total_ + move_val
                if str(p_copy) not in seen or new_total < seen[str(p_copy)]:
                    seen[str(p_copy)] = new_total
                    stack.append((p_copy, new_total))

        else:
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

                            new_total = total_ + scores[pod] * path_len

                            # already seen a path that gets there in less steps
                            if str(p_copy) not in seen or new_total < seen[str(p_copy)]:
                                seen[str(p_copy)] = new_total
                                stack.append((p_copy, total_ + scores[pod] * path_len))

    return min_total


def p1(a, room_1, room_2, room_3, room_4):
    positions = {}
    for coord in SPACES:
        positions[coord] = a[coord]

    for coord in room_1 + room_2 + room_3 + room_4:
        positions[coord] = a[coord]
    print(positions, "\n")

    room_mapping = {
        "A": room_1,
        "B": room_2,
        "C": room_3,
        "D": room_4,
    }

    return get_smallest_path(positions, room_mapping)


def p2(a):
    row1 = "  #D#C#B#A#  "
    row2 = "  #D#B#A#C#  "
    rows = np.array([list(row1), list(row2)])

    b = np.insert(a, 3, rows, 0)
    print(b)

    room_1 = [(2, 3), (3, 3), (4, 3), (5, 3)]
    room_2 = [(2, 5), (3, 5), (4, 5), (5, 5)]
    room_3 = [(2, 7), (3, 7), (4, 7), (5, 7)]
    room_4 = [(2, 9), (3, 9), (4, 9), (5, 9)]

    return p1(b, room_1, room_2, room_3, room_4)


def run(file):
    with open(file) as f:
        a = [list(x) for x in f.read().splitlines()]
        a = np.array(a)

        room_1 = [(2, 3), (3, 3)]
        room_2 = [(2, 5), (3, 5)]
        room_3 = [(2, 7), (3, 7)]
        room_4 = [(2, 9), (3, 9)]

        print(f"Part 1: {p1(a, room_1, room_2, room_3, room_4)}")

        print(f"Part 2: {p2(a)}")


test_files = [
    "test.txt",
    "input23.txt",
]
for file in test_files:
    print(f"Run cases for {file}")
    run(file)
    print()
