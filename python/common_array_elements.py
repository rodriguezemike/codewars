#https://www.codewars.com/kata/5a6225e5d8e145b540000127/python

from collections import Counter

def common(a,b,c):
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())

#This does the lifting for us with counter and elements and the & operator
#All working together to return to the minimum count for the unique elements in the intersection
#Of all the arrays.
#In the future, lets switch from building our own freqDicts and calling count and all that jazz.
#Base idea was this.

def common_non_multisets(a,b,c):
	return sum(set(a) & set(b) & set(c))

def common_multiset_naive(a,b,c):
	unique_numbers = set(a).intersection(set(b)).intersection(set(c))
	total = 0
	for i in in unique_numbers:
		total += i*(min([a.count(i), b.count(i), c.count(i)]))
	return total
