#!/usr/bin/python
import InputHelper as IH


# Day 1 Part 1
def solve1(string):
	digits = list(string)
	length = len(digits)
	total = 0

	for i, digit in enumerate(digits):
		next = (i+1) % length
		total += int(digit) if digit == digits[next] else 0

	return total

# Day 1 Part 2
def solve2(string):
	digits = list(string)
	length = len(digits)
	total = 0

	for i, digit in enumerate(digits):
		next = (i+length//2) % length
		total += int(digit) if digit == digits[next] else 0

	return total


# Read from stdin or else input file
data = IH.InputHelper(1).read().strip()
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))