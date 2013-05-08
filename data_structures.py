#!/usr/bin/python
import sys
from myclass import Nick

# NOTE: Terms in double quotes (i.e. "term") are things that you should Google to get more info about.
#       Typically searching for "Python <term>" will yield lots of useful information.

def main():
	# Lists: a sequential container of data. Typically used for homogeneous data, but they can hold different types.
	print "***** LISTS *****"
	empty_list = [ ] # Brackets represent list literals; [] is an empty list
	my_list = [ -3, -2, -1, 0, 1, 2, 3 ] # myList is now a list with elements
	zero_to_two = my_list[3:6] # You can use "list slicing" to get sections of a list

	my_list_but_positive = [ num + 1 for num in my_list if num > 0 ] # "List comprehensions" are a great way to make a list from exisiting lists
	print 'List of positive numbers: {}'.format(', '.join(str(x) for x in my_list_but_positive)) # Use str.join() to combine a list of strings into one big string

	print

	# Dicts: key-value stores. Dict is short for dictionary.
	print "***** DICTS *****"
	empty_dict = { } # Curly brackets represent dict literals. { } is an empty dict.
	email_dict = {'Nick' : 'nickvanhoog@gmail.com', 'Roger' : 'made.up.email@somesite.com', 'Henrietta' : 'mark@facebook.com', 'Mark' : 'mark@gmail.com'}
	print email_dict['Nick']
	gmail_dict = { name : email_dict[name] for name in email_dict if 'gmail.com' in email_dict[name]} # There are "dict comprehensions", too!
	print gmail_dict

	print

	# Sets: like sets in math! A collection of unique objects.
	print "***** SETS *****"
	empty_set = set() # You have to use the set constructor to create sets. set() returns an empty set.
	another_list = [ 1, 2, 2, 3 ]
	my_set = set(another_list) # This will create a set with elements [1, 2, 3] because set elements are unique!
	another_set = set([1, 2, 3, 4, 5])
	yet_another_set = another_set - my_set # You can use the set operators on Python sets! yet_another_set now contains 4 and 5 after performing set difference
	print yet_another_set

	print

	# Tuples: data separated by commas. Similar to lists, but often used with ordered, heterogeneous data (e.g. database rows).
	print "***** TUPLES *****"
	empty_tuple = ( ) # Parentheses represent tuples. ( ) is an empty tuple.
	my_tuple = ('Nick', 'nickvanhoog@gmail.com', 22)
	name, email, age = my_tuple # "Tuple unpacking": this works for any "sequence type" on the right hand side
	print 'Name: {}, Email: {}, Age: {}'.format(name, email, age)
	print

if __name__ == '__main__':
	main()