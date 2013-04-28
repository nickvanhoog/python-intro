#!/usr/bin/python
import sys

def main():
	# Lists: a sequential container of data
	emptyList = [ ] # Brackets represent list literals; [] is an empty list
	myList = [ -3, -2, -1, 0, 1, 2, 3 ] # myList is now a list with elements
	zeroToTwo = myList[3:6]

	myListButPositive = [ num + 1 for num in myList if num > 0 ] # List comprehensions are a great way to make a list from exisiting lists
	print myListButPositive
	print 'List of positive numbers: {}'.format(', '.join(str(x) for x in myListButPositive)) # Use str.join() to combine a list of strings into one big string

	# Dicts: key-value stores
	emptyDict = { } # Curly brackets represent dict literals. { } is an empty dict.
	emailDict = {'Nick' : 'nickvanhoog@gmail.com', 'Roger' : 'made.up.email@somesite.com', 'Henrietta' : 'mark@facebook.com'}
	gmailDict = { name : emailDict[name] for name in emailDict if 'gmail.com' in emailDict[name]} # There are dict comprehensions, too!
	print gmailDict

	# Sets: like sets in math! A collection of unique objects.
	emptySet = set() # Sets are relatively new to Python and so you have to use the set constructor to create them. set() returns an empty set.
	anotherList = [ 1, 2, 2, 3 ]
	mySet = set(anotherList) # This will create a set with elements [1, 2, 3] because set elements are unique!
	print mySet

	# Tuples: 
	emptyTuple = ( ) # Parentheses represent tuples. ( ) is an empty tuple.

if __name__ == '__main__':
	main()