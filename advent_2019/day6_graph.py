import networkx as nx

def part_1(g):
	print(sum(nx.shortest_path_length(g, x, "COM") for x in g.nodes))

def part_2(ig):
	print(nx.shortest_path_length(ig, 'YOU', 'SAN') - 2)

with open("input6.txt") as f:
	edge_list = (x.strip().split(')') for x in f)
	g = nx.from_edgelist(edge_list)

part_1(g)
part_2(g)
