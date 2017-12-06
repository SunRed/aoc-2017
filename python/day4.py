#!/usr/bin/python
import InputHelper as IH


def solve1(lines):
	return compute(lines, lambda w1, w2: w1 == w2)

def solve2(lines):
	return compute(lines, lambda w1, w2: is_anagram(w1, w2))


def compute(lines, cond):
	counter = 0

	for line in lines:
		contains = False
		for i, word1 in enumerate(line.strip().split(' ')):
			for j, word2 in enumerate(line.strip().split(' ')):
				if i != j and cond(word1, word2):
					contains = True

		if not contains:
			counter += 1

	return counter

def is_anagram(a, b):
	if len(a) != len(b):
		return False

	return ''.join(sorted(a)) == ''.join(sorted(b)); 

# Read from stdin or else from input file
data = IH.InputHelper(4).readlines()
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))