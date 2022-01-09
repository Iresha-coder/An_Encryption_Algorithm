# Letters to Numbers dictionary to encrypt
characters = {"a":"100", "b":"101", "c":"102", "d":"103", "e":"104", "f":"105", "g":"106", "h":"107", "i":"108", "j":"109", "k":"110", "l":"111", "m":"112", "n":"113", "o":"114", "p":"115", "q":"116", "r":"117", "s":"118", "t":"119", "u":"120", "v":"121", "w":"122", "x":"123", "y":"124", "z":"125", "A":"126", "B":"127"," ":"000"} 

# function to return key for any value
def get_key(val):
    for key, value in characters.items():
         if val == value:
             return key

# function to encrypt text
def encrypt(text):
	en_val = ""

	for i in text:
		en_val += characters[i]

	return en_val

# function to decrypt text
def decrypt(text):
	de_val = ""
	triple = ""

	for i in text:
		triple += i
		if len(triple) == 3:
			de_val += get_key(triple)
			triple = ""

	return de_val