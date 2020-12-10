fields = {
    'byr': lambda x: 2002 >= int(x) >= 1920,
    'iyr': lambda x: 2020 >= int(x) >= 2010,
    'eyr': lambda x: 2030 >= int(x) >= 2020,
    'hgt': lambda x: (x[-2:] == 'cm' and 193 >= int(x[:-2]) >= 150) or (x[-2:] == 'in' and 76 >= int(x[:-2]) >= 59),
    'hcl': lambda x: x[0] == '#' and all(x[i] in ['0','1','2','3','4','5','6','7','8','9', 'a','b','c','d','e','f'] for i in range(1, 7)),
    'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda x: len(x) == 9  and x.isdigit(),
}

def p1(a):
	valid = 0

	for i, passport in enumerate(a):
		if all(key in passport for key in fields):
			valid += 1
	return valid

def p2(a):
	valid = 0

	for i, passport in enumerate(a):
		if all(key in passport for key in fields) and all(fields[key](passport[key]) for key in fields):
			valid += 1

	return valid

### insert how to parse line
def parse_line(lines):
	d = {}
	for line in lines.split(' '):
		k, v = line.split(':')
		d[k] = v
	return d

import re
with open('input4.txt') as f:
	a = []
	passports = f.read().strip().split('\n\n')

	for passport in passports:
		parts = re.split('\s', passport)
		pass_dict = dict(part.split(':') for part in parts)
		a.append(pass_dict)

	print(p1(a))
	print(p2(a))

# def check_entry(entry):
# 	all_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
# 	remain = all_keys - set(entry.keys())

# 	return list(remain) == [] or list(remain) == ['cid']

# def check_range(entry, key, low, high):
# 	if key not in entry:
# 		return False
# 	return int(entry[key]) >= low and int(entry[key]) <= high

# def check_hgt(entry):
# 	if 'hgt' not in entry:
# 		return False

# 	height = entry['hgt']
# 	if 'cm' == height[-2:]:
# 		return int(height[:-2]) >= 150 and int(height[:-2]) <= 193
# 	elif 'in' == height[-2:]:
# 		return int(height[:-2]) >= 59 and int(height[:-2]) <= 76
# 	else:
# 		return False

# def check_hcl(entry):
# 	if 'hcl' not in entry:
# 		return False

# 	hcl = entry['hcl']
# 	if '#' != hcl[0] and len(hcl) != 7:
# 		return False

# 	valid_chars = ['0','1','2','3','4','5','6','7','8','9',
# 					'a','b','c','d','e','f']
# 	for i in range(1, 7):
# 		if hcl[i] not in valid_chars:
# 			return False
# 	return True

# def check_ecl(entry):
# 	if 'ecl' not in entry:
# 		return False
# 	valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
# 	return entry['ecl'] in valid_ecl

# def check_pid(entry):
# 	if 'pid' not in entry:
# 		return False
# 	pid = entry['pid']
# 	if len(pid) != 9:
# 		return False

# 	for i in range(9):
# 		if pid[i] not in ['0','1','2','3','4','5','6','7','8','9']:
# 			return False

# 	return True

# def check_entry_2(entry):
# 	a = check_range(entry, 'byr', 1920, 2002)
# 	b = check_range(entry, 'iyr', 2010, 2020)
# 	c = check_range(entry, 'eyr', 2020, 2030)
# 	d =	check_hgt(entry)
# 	e =	check_hcl(entry)
# 	f =	check_ecl(entry)
# 	g =	check_pid(entry)

# 	res =  a and b and c and d and e and f and g #and check_entry(entry)


# 	if res == True and (res and check_entry(entry) == False):
# 		print(entry)
# 		print(a, b, c, d ,e, f, g, check_entry(entry))
# 		print(res)
# 		print()

# 	return res