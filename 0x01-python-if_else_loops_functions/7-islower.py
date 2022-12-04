#!/usr/bin/python3
def islower(c):
	if (ord(c) >= 97 and ord(c) < 123):
		return True
	elif (ord(c) >= 48 and ord(c) < 58):
		 return False
	else:
		return False
