import sys
class Palindrome():
	"""
			@author Lucas Santos de Paula
			This class detects if a word is a palindrome or reverse string.
	"""
	def __init__(self, file):
		"""This method reads file content and check if each word is a palindrome, mirrored string or both."""
		self.file = open(file, "r")
		self.words = []
		for line in self.file:
			line=line[:-1] #remove the last character because it's a \n
			word = line.upper()
			
			if(self.isPalindrome(word) and self.isMirroredString(word)):
				print word + " -- is a mirrored palindrome."
			elif(self.isPalindrome(word)):
				print word + " -- is a regular palindrome."
			elif(self.isMirroredString(word)):
				print word + " -- is a mirrored string."
			else:
				print word + " -- is not a palindrome."

	def isPalindrome(self, word):
		"""This method returns True when the word is a palindrome"""
		if(word==word[::-1]):
			return True
		return False

	def isMirroredString(self, word):
		"""
		This method returns True when string is a mirrored string.
		Conditions to be a mirrored string:
		1. Every character MUST be a mirror
		2. If you look the mirrored string backwards it's exactly the original one.
		"""
		aux = word
		changes = {'A':'A','E': '3', 'H':'H', 'I':'I', 'J': 'L','L': 'J','M':'M','O':'O','S': '2','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z': '5','1':'1','2': 'S','3': 'E','5': 'Z','8':'8'}

		auxlist = list(aux)
		#Replace all characters. If one cant be replaced, then, return false.
		for i in range(0,len(word)):
			if(not aux[i] in changes):
				return False
			auxlist[i] = changes[aux[i]]
		
		aux = ''.join(auxlist)
		
		#Reverts the replaced string to check if its equal to the original one.
		if(aux[::-1]!=word):
			return False
		return True

p = Palindrome("in.txt")