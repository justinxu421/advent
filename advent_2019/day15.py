from intcode_deprecated import IntcodeRunner
import utils

N,S,E,W = 1,2,3,4
actions = [N,S,E,W]	
r_actions = {N:S, S:N, E:W, W:E, None:None}

def move(state, action):
	if action == N:
		return (state[0]-1, state[1])
	if action == S:
		return (state[0]+1, state[1])
	if action == E:
		return (state[0], state[1]+1)
	if action == W:
		return (state[0], state[1]-1)

def run_step(ic, ipt):
	ic.run(ipt, ipt)
	return ic.output	

def update(history, ic, grid, visited, goals):
	last_state, _ = history[-1]

	for action in actions:
		# move
		new_state = move(last_state, action)

		# dont repeat states
		if new_state in visited: 
			continue 
		# if wall dont go
		elif new_state in grid and grid[new_state] == 0:
			continue
		# otherwise, see the status of this move
		else:
			status = run_step(ic, action)
			grid[new_state] = status
			visited.add(new_state)
			# hit wall, do another move
			if status == 0:
				continue
			# if valid, then do next move
			else:
				history.append((new_state, action))
				# if we hit goal, then save it
				if status == 2:
					goals.append(new_state)
					print(len(history)-1)
					utils.print_grid(grid)
				return True
	return False

def flood(grid, start):
	q = [(start, 0)]
	visited = set()
	max_dist = 0

	while q:
		state, dist = q.pop(0)
		max_dist = max(dist, max_dist)
		visited.add(state)
		for action in actions:
			new_state = move(state, action)
			if new_state not in visited and grid[new_state] != 0:
				q.append((new_state, dist+1))

	print(max_dist)

def solve(ic):
	grid = {}
	goals = []
	visited = set()

	start = (0,0)
	grid[start] = '*'
	history = [(start, None)]

	while history: 
		# backtrack if dead end
		if update(history, ic, grid, visited, goals) == False:
			_, action = history.pop()
			run_step(ic, r_actions[action])

	print(goals[0])
	flood(grid, goals[0])

with open('input15.txt') as f:
	arr = list(map(int, f.readline().strip().split(',')))
	ic = IntcodeRunner(arr)
	solve(ic)
