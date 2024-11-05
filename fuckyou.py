from distutils.command.clean import clean

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
		print(content)
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
		print(pages)

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
		print(book)
		return codebook

def

def main():
	book = 'books/poem.txt'
	codebook = read_book(book)

main()