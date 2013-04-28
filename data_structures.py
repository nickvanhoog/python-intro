#!/usr/bin/python
import sys

# NOTE: Terms in double quotes (i.e. "term") are things that you should Google to get more info about.
#       Typically searching for "Python <term>" will yield lots of useful information.

def main():
	# Lists: a sequential container of data. Typically used for homogeneous data.
	print "***** LISTS *****"
	emptyList = [ ] # Brackets represent list literals; [] is an empty list
	myList = [ -3, -2, -1, 0, 1, 2, 3 ] # myList is now a list with elements
	zeroToTwo = myList[3:6] # You can use "list slicing" to get sections of a list

	myListButPositive = [ num + 1 for num in myList if num > 0 ] # "List comprehensions" are a great way to make a list from exisiting lists
	print myListButPositive
	print 'List of positive numbers: {}'.format(', '.join(str(x) for x in myListButPositive)) # Use str.join() to combine a list of strings into one big string

	print

	# Dicts: key-value stores. Dict is short for dictionary.
	print "***** DICTS *****"
	emptyDict = { } # Curly brackets represent dict literals. { } is an empty dict.
	emailDict = {'Nick' : 'nickvanhoog@gmail.com', 'Roger' : 'made.up.email@somesite.com', 'Henrietta' : 'mark@facebook.com', 'Mark' : 'mark@gmail.com'}
	gmailDict = { name : emailDict[name] for name in emailDict if 'gmail.com' in emailDict[name]} # There are "dict comprehensions", too!
	print gmailDict

	print

	# Sets: like sets in math! A collection of unique objects.
	print "***** SETS *****"
	emptySet = set() # Sets are relatively new to Python and so you have to use the set constructor to create them. set() returns an empty set.
	anotherList = [ 1, 2, 2, 3 ]
	mySet = set(anotherList) # This will create a set with elements [1, 2, 3] because set elements are unique!
	anotherSet = set([1, 2, 3, 4, 5])
	yetAnotherSet = anotherSet - mySet # You can use the - operator on sets to perform set difference! yetAnotherSet now contains 4 and 5
	print yetAnotherSet

	print

	# Tuples: data separated by commas. Similar to lists, but often used with ordered, heterogeneous data. 
	print "***** TUPLES *****"
	emptyTuple = ( ) # Parentheses represent tuples. ( ) is an empty tuple.
	myTuple = ('Nick', 'nickvanhoog@gmail.com', 22)
	name, email, age = myTuple # "Tuple unpacking": this works for any "sequence type" on the right hand side
	print 'Name: {}, Email: {}, Age: {}'.format(name, email, age)
	print

if __name__ == '__main__':
	main()