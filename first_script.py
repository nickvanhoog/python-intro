#!/usr/bin/python
import sys # sys is a "module", this is analogous to #include <iostream>

# NOTE: Terms in double quotes ("term") are things that you should Google to get more info about.
#       Typically searching for "Python <term>" will yield lots of useful information.

# A function is defined with the def keyword.
def main():
	# Python statements do not need a semicolon at the end!

	x = 3 # Don't need to declare variables. And variables don't have strict types.
	x = "Now x is a string" # You can assign any new value to an existing variable.
	x = 'x is still a string' # Strings can be written with single or double quotes

	printArg(x) # Function calls are just as you'd expect

	print # prints a black line

	num = 0;
	while (num < 3):
		#Indentation is not optional!
		print "num is now: {}".format(num) # Use str.format() to format strings
		num += 1 # There is no increment (num++) / decrement (num--) operator

	print

	# You can use the built-in "range()" function to loop over a range of numbers like this. Also see "xrange()".
	for i in range(5):
		print i

	print

	# if statements work as expected; note the "elif" instead of "else if"
	if num is None: # None is analogous to NULL in C++. The is operator compares the identities of its arguments, not their values. See id() built-in function.
		print "num is None"
	elif num is not None: # The is not operator acts as you'd expect; x is not y returns true if id(x) != id(y)
		print "num is not None"
	else:
		print "I just wanted to show an else section"

	print

	# Exceptions are cool! Use them!
	try:
		print y # y has not been defined; notice this error was only caught once we actually ran this code. Way different than C++.
	except NameError: # NameError is a built-in Python exception
		print 'We caught an exception!'

	return 0 # A function without a return value implicitly returns None

def print_arg(arg):
	print arg # To print something, just write "print <thing you want to print>" (without the < >). This automatically appends a newline.

if __name__ == '__main__': # Calling this with "python first_script.py" sets __name__ to '__main__'
	sys.exit(main())