#!/usr/bin/python
import InputHelper as IH


def solve1(lines):
	return compute(convert(lines), lambda i: i + 1)

def solve2(lines):
	return compute(convert(lines), lambda i: i + 1 if i < 3 else i - 1)


def convert(lines):
	return [ int(line) for line in lines ]

def compute(lines, cond):
	counter = 0
	index = 0
	while index < len(lines):
		index = index if index > 0 else 0
		newindex = lines[index]
		lines[index] = cond(lines[index])
		index += newindex
		counter += 1

	return counter

# Read from stdin or else from input file
data = IH.InputHelper(5).readlines()
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))