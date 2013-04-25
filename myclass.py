#!/usr/bin/python

class Nick(): # This is how you declare a class in Python
	def __init__(self, num = 1): # __init__ is one of many "magic methods", or methods starting and ending with two underscores
		self.num = num # To refer to class attributes, use self.attributeName. Forget the self and it'll be an error.
		self.theList = [ ] # Brackets ([ and ]) are used for list literals. We init self.theList to an empty list.

	def addToList(self, x = None): # The = None means that None is the default value assigned to x if nothing is passed in
		if x is not None: # Let's avoid sticking None into our list
			self.theList.append(x) # Adds x to the end of self.theList

	def printList(self):
		for element in self.theList: # This iterates over each item in self.theList in order (see Python generators, they're awesome)
			print element

class SuperNick(Nick): # This is how you declare a derived class; the base class goes in the parentheses
	def __init__(self, num = 0):
		Nick.__init__(self, num)

	def kirby(self):
		print "<(^_^<)"

if __name__ == '__main__':
	sn = SuperNick()
	sn.kirby()