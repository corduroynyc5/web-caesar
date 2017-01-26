#### caesar.py ####

import string

def alphabet_position(letter):	
	letters = string.ascii_lowercase	
	if letter.lower() in letters:
		#print(letters.index(letter.lower()))
		return letters.index(letter.lower())
		

def rotate_character(char, rot):
	if char.isalpha():
		o_position = alphabet_position(char)
		n_position = (o_position + rot) % 26
		#print(n_position)
		if char in string.ascii_lowercase:
			return string.ascii_lowercase[n_position]
		elif char in string.ascii_uppercase:
			return string.ascii_uppercase[n_position]
	else:
		return char
		
		
def encrypt(text, rot):
	n_text = []
	for char in text:
		n_text += rotate_character(char, rot)

	string = ''.join(map(str, n_text))
	return string