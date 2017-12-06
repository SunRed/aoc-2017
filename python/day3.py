#!/usr/bin/python
import InputHelper as IH


def solve1(pinput):
	direction = 1;

	north = 0;
	east = 0;

	stepsToChangeDir = 1
	stepCounter = 0

	index = 1
	while index < pinput:
		if stepCounter == stepsToChangeDir:
			direction = (direction + 3) % 4

		if stepCounter == (stepsToChangeDir * 2):
			stepCounter = 0
			stepsToChangeDir += 1

			direction = (direction + 3) % 4

		stepCounter += 1
		index += 1

		if direction == 0:
			north += 1
		elif direction == 1:
			east += 1
		elif direction == 2:
			north -= 1
		elif direction == 3:
			east -= 1

	return abs(north) + abs(east)

def solve2(pinput):
	return "not implemented yet"


# Read from stdin or else from input file
data = int(IH.InputHelper(3).read())
print("Part 1: " + str(solve1(data)))
print("Part 2: " + str(solve2(data)))