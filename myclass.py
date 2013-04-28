#!/usr/bin/python

# NOTE: Terms in double quotes ("term") are things that you should Google to get more info about.
#       Typically searching for "Python <term>" will yield lots of useful information.

class Nick(): # This is how you declare a class in Python. Everything is public in a Python class.
	def __init__(self, num = 1): # __init__ is one of many "magic methods", or methods starting and ending with two underscores
		self.num = num # To refer to class attributes, use self.attributeName. Forget the self and it'll be an error.
		self.theList = [ ] # Brackets ([ and ]) are used for list literals. We init self.theList to an empty list.
		self._protectedAttr = 'Subclasses can use me!' # A single underscore indicates a protected attribute by convention. 
		self.__numPlusOne = num + 1 # Using two underscores before an attribute is a convention to indicate it is private.

	def addToList(self, x = None): # Writing = None means that None is the default value assigned to x if nothing is passed in
		if x is not None: # Let's avoid sticking None into our list
			self.theList.append(x) # Adds x to the end of self.theList

	def printList(self):
		for element in self.theList: # This iterates over each item in self.theList in order (see Python "generators", they're awesome)
			print element

	def printNum():
		""" This is a Python doc string. This function's __doc__ attribute will be equal to this string. """ # Used for auto-documentation
		print num

	def __str__(self): # Calling print X on an object will output the string returned in X.__str__()
		return "Nick object with num = {}".format(self.num)

class SuperNick(Nick): # This is how you declare a derived class; the base class goes in the parentheses
	def __init__(self, num = 0):
		Nick.__init__(self, num)

	def kirby(self):
		print "\n<(^_^<)\n"
		print "<(^_^)>\n"
		print "(>^_^)>\n"

if __name__ == '__main__':
	sn = SuperNick()
	sn.kirby()