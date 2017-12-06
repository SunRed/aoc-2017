#!/usr/bin/python
import InputHelper as IH


# Day 2 Part 1
def solve1(lines):
	return sum([ max(line) - min(line) for line in convert(lines) ])

# Day 2 Part 2
def solve2(lines):
	return sum([ get_divisible(line) for line in convert(lines) ])


def convert(lines):
	return [[ int(n) for n in line.strip().split('\t') ] for line in lines ]

def get_divisible(line):
	return max([ int(i / j) for j in line for i in line if i % j == 0 ])
#	for i in range(len(line)):
#		for j in range(len(line)):
#			if i != j and line[i] % line[j] == 0:
#				return int(line[i] / line[j])

# Read from stdin or else input file
data = IH.InputHelper(2).readlines()
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))