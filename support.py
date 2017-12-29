import os
clear = lambda: os.system('cls')

def strP(string, size):
	string = str(string)
	if len(string) > size:
		print("String Parsing Error")
		return 0
	else:
		while len(string) < size:
			string += " "
		return string


def txt(string, size, n):
	string = str(string)
	if len(string) < 50 * n:
		string = string[(n-1) * size : n * size]
		while len(string) < 50:
			string += " "
		return string
	string = string[(n-1) * size : n * size]
	if string[0] == " ":
		string = list(string)
		del(string[0])
		string = ''.join(string)
		string += " "
	return string


def debug(x):
	print("debug {}".format(x), end=' ')
	input()


def error():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗  
\t║\t\t\t\tError! Something Went Wrong!\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
