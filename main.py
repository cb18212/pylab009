from distutils.command.clean import clean
import random
import re
from Tools.demo.sortvisu import Array

HOW_MANY_BOOK = 3
LINE = 6
PAGE = 4

book = {}
codebook = {}

def clean_line(line):
	return line.strip().replace('-', '') + ' ' #add space instead of newline

def setcoord(a,b,c, content):
	book[a][b][c] = content

def read_book(file_path):
	index = 0
	with open(file_path, 'r', encoding='utf-8') as fp:
		content = []
		for line in fp.readlines():
			content.append(line.strip().replace('-', '') + ' ')
		content = "".join(content)
		# print(content)
		processed_words = []
		while len(content) > LINE:
			processed_words.append(content[:LINE])
			content = content[LINE:]
		processed_words.append(content)
		#At this point processed_words is an array of mostly fixed-length 'words'

		pages = []
		while len(processed_words) > PAGE:
			pages.append(processed_words[:PAGE])
			processed_words = processed_words[PAGE:]
		pages.append(processed_words)
		# print(pages)

# 		now we have a list of lists of words
		for pindex, page in enumerate(pages):
			total = {}
			for lindex, line in enumerate(page):
				total[lindex] = line
				for chindex, ch in enumerate(line):
					if not ch in codebook.keys():
						codebook[ch] = [(pindex, lindex, chindex)]
					else:
						codebook[ch].append((pindex, lindex, chindex))
			book[pindex] = total.copy()
		# print(book)
		return codebook

def reverse_book(c_book):
	output = {}
	# print(c_book.keys())
	for letter in c_book.keys():
		for coord in c_book[letter]:
			output[coord] = letter
	return output

def encrypt_letter(letter, c_book):
	index = random.randint( 0, len(c_book[letter])-1 )
	return c_book[letter][index]

def decrypt_letter(letter, c_rev_book):
	return c_rev_book[letter]

def encrypt(cleartext, codebook):
	arr = [encrypt_letter(letter, codebook) for letter in cleartext]
	result = ""
	for tup in arr:
		result += str(tup[0])+"-"+str(tup[1])+"-"+str(tup[2])+"-"
	return result[:-1]

def decrypt(ciphertext, rev_codebook):
	ciphertext_tupled = []
	for tuples in re.findall("\d+-\d+-\d+", ciphertext):
		tuples = tuples.split("-")
		ciphertext_tupled.append((int(tuples[0]), int(tuples[1]), int(tuples[2])))
	return "".join([decrypt_letter(letter, rev_codebook) for letter in ciphertext_tupled])

def main_menu():
	print("MAIN MENU\nPlease select an option:\n1) ENCRYPT\n2) DECRYPT\n3) QUIT")
	return int(input(">"))

def main():
	book = 'books/principia_discordia'
	codebook = read_book(book)
	rev_codebook = reverse_book(codebook)

	cipher = encrypt("The eagle has landed.", codebook)
	print(f"ciphertext: {cipher}")
	print(f"cleartext: {decrypt(cipher, rev_codebook)}")

	while True:
		try:
			choice = main_menu()
			match choice:
				case 1:
					message = input("Please enter your message to encrypt: ")
					print(encrypt(message, codebook))
					continue
				case 2:
					message = input("Please enter your message to decrypt: ")
					print(decrypt(message, rev_codebook))
					continue
				case 3:
					break
		except:
			print("ERROR: Invalid option selected.")
main()