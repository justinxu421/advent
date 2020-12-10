from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

def part_1(layers):
	digits = [Counter(layer.flatten().tolist()) for layer in layers]
	min_0 = min([x[0] for x in digits])

	for layer in digits:
		if layer[0] == min_0:
			print(layer[1]*layer[2])
				
def part_2(layers):
	n_,h,w = layers.shape
	final_image = np.empty((h,w))
	for i in range(h):
		for j in range(w):
			for d in range(n_):
				if layers[d,i,j] != 2:
					final_image[i,j] = 1-layers[d,i,j]
					break

	plt.imshow(final_image)
	plt.savefig('image.png')

def parse_image(image, w, h):
	size= w*h
	n_= int(len(image) / size)
	layers = np.empty((n_,h,w)) 

	for layer in range(n_):
		begin = size*layer
		for i in range(h):
			for j in range(w):
				idx = begin + w*i + j
				layers[layer, i, j] = image[idx]

	part_1(layers)
	part_2(layers)


with open('input8.txt') as f:
	image = list(map(int, list(f.readline().strip())))
	w,h = 25,6

	parse_image(image, w, h)
