from collections import defaultdict

# get the digit and param modes
def parse_num(num):
	digit = num % 100
	m1 = (num // 100) % 10
	m2 = (num // 1000) % 10
	m3 = (num // 10000) % 10
	return digit, m1, m2, m3

def expand_arr(arr, idx):
	while idx >= len(arr):
		arr.append(0)

class IntcodeRunner:
	def __init__(self, arr, inputs = []):
		self.idx = 0
		self.count = 0
		self.arr = arr
		self.inputs = inputs
		self.outputs = []
		# parameters to tell if we've run out of inputs	
		# self.await_input = False
		self.input_op = False
		# true if intcode is done running
		self.done = False
		self.base = 0

	def set_inputs(self, inputs):
		self.inputs = inputs

	def get_param(self, mode, num):
		if mode == 0:
			return self.arr[num]
		if mode == 1:
			return num
		if mode == 2:
			return self.arr[num+self.base]

	def get_idx(self, mode, num):
		if mode == 0:
			return num
		if mode == 2:
			return num+self.base

	def add_inputs(self, ipts):
		self.inputs.extend(ipts)

	def add_input(self, ipt):
		self.inputs.append(ipt)
		# if self.await_input:
		# 	self.arr[self.input_op] = self.inputs[self.count]
		# 	self.count += 1
		# 	self.idx += 2
		# 	self.await_input = False
		# 	self.input_op = None


	def run(self):
		# run through the array
		while self.idx < len(self.arr):
			digit, m1, m2, m3 = parse_num(self.arr[self.idx])

			# end condition
			if digit == 99:
				self.done = True 
				return

			try:
				num1 = self.arr[self.idx + 1]
				i1 = self.get_idx(m1, num1)
				arg1 = self.get_param(m1, num1)
			except:
				pass

			try:
				num2 = self.arr[self.idx + 2]
				i2 = self.get_idx(m2, num2)
				arg2 = self.get_param(m2, num2)
			except:
				pass

			try:
				num3 = self.arr[self.idx + 3]
				i3 = self.get_idx(m3, num3)
			except:
				pass


			# addition
			if digit == 1:
				expand_arr(self.arr, i3)
				self.arr[i3] = arg1 + arg2 
				self.idx += 4

			# multiplication
			elif digit == 2:
				expand_arr(self.arr, i3)
				self.arr[i3] = arg1 * arg2
				self.idx += 4

			# write
			elif digit == 3:
				expand_arr(self.arr, i1)
				if self.count < len(self.inputs):
					self.arr[i1] = self.inputs[self.count] 
					self.count += 1
					self.idx += 2
				else:
					self.input_op = i1
					# self.await_input = True
					# print('out of inputs')
					return 

			# output
			elif digit == 4:
				self.outputs.append(arg1)
				self.idx += 2

			# jump if true
			elif digit == 5:
				if arg1 != 0:
					self.idx = arg2
				else:
					self.idx += 3

			# jump if false
			elif digit == 6:
				if arg1 == 0:
					self.idx = arg2 
				else:
					self.idx += 3

			# less than
			elif digit == 7:
				expand_arr(self.arr, i3)
				if arg1 < arg2:
					self.arr[i3] = 1
				else:
					self.arr[i3] = 0
				self.idx += 4

			# equals
			elif digit == 8:
				expand_arr(self.arr, i3)
				if arg1 == arg2:
					self.arr[i3] = 1
				else:
					self.arr[i3] = 0
				self.idx += 4

			# update relative base
			elif digit == 9:
				self.base += arg1
				self.idx += 2

			else:
				assert False

		# if out of while loop , then we done
		self.done = True
