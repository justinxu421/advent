from collections import defaultdict, Counter
import numpy as np
import math
import parse

class Moon():
	def __init__(self, pos):
		self.v = np.array([0,0,0])
		self.pos = pos

	def get_potential(self):
		return sum(np.abs(self.pos))

	def get_kinetic(self):
		return sum(np.abs(self.v))

	def get_total_energy(self):
		return self.get_potential() * self.get_kinetic()

'''
<x=16, y=-11, z=2>
<x=0, y=-4, z=7>
<x=6, y=4, z=-10>
<x=-3, y=-2, z=-4>
'''
def parse_input(file):
	moon_locations = []
	with open(file) as f:
		for line in f:
			vrs = parse.parse('<x={}, y={}, z={}>', line.strip())
			moon_locations.append(list(map(int,vrs)))
	return moon_locations

def init_moons(file):
	moon_locations = parse_input(file)
	return [Moon(np.array(moon)) for moon in moon_locations]

def get_pull(p1, p2):
	if p1 == p2:
		return (0,0)
	if p1 < p2:
		return (1,-1)
	if p1 > p2:
		return (-1,1)

def apply_gravity(moons, axis):
	# loop through pairs of moons
	for i in range(len(moons)):
		for j in range(i+1, len(moons)):
			m1 = moons[i]
			m2 = moons[j]
			pull1, pull2 = get_pull(m1.pos[axis], m2.pos[axis])
			m1.v[axis] += pull1
			m2.v[axis] += pull2

def apply_velocity(moons, axis):
	for moon in moons:
		moon.pos[axis] += moon.v[axis]

def get_total_energy(moons):
	energy = 0
	for moon in moons:
		energy += moon.get_total_energy()
	return energy

def part_1(ipt):
	moons = init_moons(ipt)
	for _ in range(1000):
		for axis in range(3):
			apply_gravity(moons, axis)
			apply_velocity(moons, axis)
	total_energy = get_total_energy(moons)
	print(total_energy)


def lcm(nums):
	lcm = nums[0]
	for num in nums[1:]:
		lcm = lcm*num//math.gcd(lcm, num)
	return lcm

def get_positions(moons, axis):
	return tuple([moon.pos[axis] for moon in moons])

def get_velocities(moons, axis):
	return tuple([moon.v[axis] for moon in moons])

def get_iter(ipt, axis):
	i = 0
	position_history = set()
	moons = init_moons(ipt)
	while True:
		p = get_positions(moons, axis)
		v = get_velocities(moons, axis)
		pos = (p,v)

		if pos in position_history:
			print(axis, i)
			return i

		position_history.add(pos)

		apply_gravity(moons, axis)
		apply_velocity(moons, axis)
		i += 1

def part_2(ipt):
	iters = [get_iter(ipt, axis) for axis in range(3)]
	print(lcm(iters))


part_1('input12.txt')
part_2('input12.txt')


