from algorithm import *

running = True

while running:

	print("-------------Encrytion and Decryption Algorithm-------------")
	print("---------------Made By Iresha Samarakoon--------------------")
	print("What do you want to do?")
	print("Option 1: Encrypt")
	print("Option 2: Decrypt")

	answer = input(": ")

	if answer.lower() == "option 1":
		text = input("Type the text you want to encrypt: ")
		print(encrypt(text))
	elif answer.lower() == "option 2":
		text = input("Type the text you want to decrypt: ")
		print(decrypt(text))

	again = input("Do you want to try again? (Yes or No): ")

	if again.lower() == "yes":
		continue
	elif again.lower() == "no":
		running = False