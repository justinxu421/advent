from collections import defaultdict

def get_orbits(i1, graph):
	total = 0

	if i1 not in graph:
		return 0

	for i2 in graph[i1]:
		total += get_orbits(i2, graph) + 1

	return total

def part_1(graph):
	total = 0
	for i1 in graph:
		total += get_orbits(i1, graph)
	print(total)

def get_dist(a, b, graph):
	q = [(a,0)]

	visited = set()
	visited.add(a)

	while q:
		curr, dist = q.pop(0)
		for n in graph[curr]:
			if n not in visited:
				visited.add(n) 
				if n == b:
					print(dist+1)
					return dist + 1
				q.append((n, dist+1))		 

def part_2(i_graph):
	get_dist(i_graph['YOU'][0], i_graph['SAN'][0], i_graph)

with open('input6.txt') as f:
	g = defaultdict(list)
	ig = defaultdict(list)

	for line in f:
		# b orbits a 
		a,b = line.strip().split(')')
		g[a].append(b)

		# bi directional graph
		ig[b].append(a)
		ig[a].append(b)

	part_1(g)
	part_2(ig)


			

