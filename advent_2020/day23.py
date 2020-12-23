from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solve_LL(a, max_, iters):
    d = {}
    cur = None
    head = None

    # create linked list
    for x in a:
        node = Node(x)
        d[x] = node

        if cur:
            cur.next = node
        if not head:
            head = node
        cur = node
    cur.next = head
    
    start = d[a[0]]
    for it in range(iters):
        if it % 1000000 == 0:
            print(it)
        cur = start.data
        dest = cur - 1
        # wrap around to max
        if dest == 0:
            dest = max_
        
        next_3 = [start.next, start.next.next, start.next.next.next]
        next_3_dat = [start.next.data, start.next.next.data, start.next.next.next.data]
        start.next = start.next.next.next.next

        while dest in next_3_dat:
            dest -= 1
            if dest == 0:
                dest = max_
        
        # reroute
        spot = d[dest]
        next_3[-1].next = spot.next
        spot.next = next_3[0]
        start = start.next

    return d

def p1(a):
    d = solve_LL(a, 9, 100)
    
    spot = d[1].next
    res = []
    for i in range(8):
        res.append(str(spot.data))
        spot = spot.next
    return ''.join(res)

def p2(a):
    max_ = 1000000
    iters = 10000000
    a = a + list(range(10, max_+1))
    d = solve_LL(a, max_, iters)

    spot = d[1].next
    return spot.data * spot.next.data

def main():
    with open('input23.txt') as f:
        a = [int(x) for x in list(f.read().strip())]
        #a = [3, 8, 9, 1, 2, 5, 4, 6, 7]

        print(f'part one: {p1(a)}')
        print(f'part two: {p2(a)}')

if __name__ == "__main__":
    main()
