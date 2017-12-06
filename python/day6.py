#!/usr/bin/python
import InputHelper as IH


def solve1(string):
	return compute(convert(string))[0]

def solve2(string):
	return compute(compute(convert(string))[1])[0]


def convert(string):
	return [ int(n) for n in string.split('\t') ]

def compute(array):
	counter = 0;
	configs = []
	while array not in configs:
		configs.append(list(array))
		left = max(array)
		index = array.index(left)

		array[index] = 0
		index = (index + 1) % len(array)

		while left > 0:
			array[index] += 1
			left -= 1
			index = (index + 1) % len(array)

		counter += 1

	return counter, array


# Read from stdin or else from input file
data = IH.InputHelper(6).read().strip()
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))