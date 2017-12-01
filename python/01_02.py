#!/usr/bin/python

string = input("Input: ")
digits = list(string)

length = len(digits)
total = 0

for i, digit in enumerate(digits):
	next = (i+length//2) % length
	total += int(digit) if digit == digits[next] else 0

print(total)