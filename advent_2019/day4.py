min = 271973
max = 785961

total = 0
for i in range(1,10):
	for j in range(i,10):
		for k in range(j,10):
			for l in range(k,10):
				for m in range(l,10):
					for n in range(m,10):
						num = 100000*i + 10000*j + 1000*k + 100*l + 10*m + n
						if num > min and num < max:
							diffs = [j-i, k-j, l-k, m-l, n-m]
							for idx in range(len(diffs)):
								if diffs[idx] == 0:
									if idx == 0 or diffs[idx-1] != 0:
										if idx == 4 or diffs[idx+1] != 0:
											total += 1
											break

print(total)


