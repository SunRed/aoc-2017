#!/usr/bin/python
import InputHelper as IH


def solve1(string):
	return compute(string, lambda i,l: i+1)

def solve2(string):
	return compute(string, lambda i,l: i+l//2)


def compute(string, cond):
	digits = list(string)
	length = len(digits)
	total = 0

	for i, digit in enumerate(digits):
		next = cond(i, length) % length
		total += int(digit) if digit == digits[next] else 0

	return total

# Read from stdin or else input file
data = IH.InputHelper(1).read().strip()
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))