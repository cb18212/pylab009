from distutils.command.clean import clean

from Tools.demo.sortvisu import Array

HOW_MANY_BOOK = 3
LINE = 6
PAGE = 4

pages = {}
page_number = 0
line_window = {}
line_number = 0
char_window =[]

def clean_line(line):
	return line.strip().replace('-', '') + ' ' #add space instead of newline

def process_page(line, line_num):
	global line_window, pages, page_number
	line_window[line_num] = line
	if len(line_window) == PAGE:
		page_number += 1
		pages[page_number] = dict(line_window)
		line_window.clear()

def process_char(c):
	global char_window
	char_window.append(c)
	if len(char_window) == LINE:
		add_line()

def add_line():
	global char_window, line_number
	line_number += 1
	process_line("".join(char_window.copy()))
	char_window.clear()

def process_line(p):
	global line_window
	line_window.append(p)
	# print(line_window)
	if len(line_window) == PAGE:
		add_page()

def add_page():
	global line_window, line_number
	print(line_number)
	process_page(line_window.copy(), line_number)
	line_window.clear()



def read_book(file_path):
	with open(file_path, 'r', encoding='utf-8') as fp:
		for line in fp:
			line = clean_line(line)
			if line.strip():
				for c in line:
					process_char(c)
					# print(c, end='')
	add_line()

def main():
	book = 'books/poem.txt'
	read_book(book)

main()