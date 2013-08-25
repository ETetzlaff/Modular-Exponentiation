#!/usr/bin/python
import math

def baseexp(n,b):
	q = n
	k = 0
	a = []
	while q != 0:
		a.append(q % b)
		q = q // b
		k += 1
	return a
	
	
a1 = baseexp(644, 2)
print a1

def modularexp(b, a, m):
	x = 1
	power = b % m
	for i in range(0, len(a)):
		if a[i] == 1:
			x = (x*power) % m
		power = (power*power) % m
	return x

x = modularexp(7, a1, 645)
print x
y = modularexp(11, a1, 645)
print y

a2 = baseexp(2003, 2)
print a2
z = modularexp(3, a2, 99)
print z

a3 = baseexp(1001, 2)
print a3
n = modularexp(123, a3, 101)
print n

a4 = baseexp(5, 2)
z1 = modularexp(2, a4, 3)
print z1
