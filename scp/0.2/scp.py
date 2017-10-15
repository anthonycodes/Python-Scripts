# Steganography Cypher Program
# Made by AnthonyCodes
# Source Code: https://github.com/anthonycodes/Python-Scripts/tree/master/scp/

# Imports
import config as conf
import api as appapi
from sys import argv, exit

# Variables
debug = conf.debug

# Functions
def getstring():
	try: arg = argv[1]
	except:
		print("Please enter a string to encrypt. To encrypt only a space use \"'space'\"")
		exit()
	try:
		arg = argv[2]
		longer = True
	except:
		longer = False
	if not longer:
		args = argv[1]
	else:
		indices = [1, len(argv) - 1]

		args = " ".join([argv[i] for i in indices])

	if argv[1] == "'space'":
		args = " "

	return args

def phaseone():
	to_encrypt = getstring()
	numbers_grouped = appapi.translate(conf.chars_to_scv, to_encrypt)
	if debug: print("[DEBUG] Phase 1 Result: {}".format(numbers_grouped))
	return numbers_grouped

def phasetwo(integer):
	result = appapi.convert_scv_to_ptwo_hash(int(integer), conf.hl)
	if debug: print("[DEBUG] Phase 2 Result: {}".format(result))
	return result

def phasethree(string, salt):
	result = appapi.two_translate(conf.scv_to_chars, string)
	if debug: print("[DEBUG] Phase 3 Result: {}".format(result))
	newsalt = appapi.translate(conf.salt1, str(salt))
	index = 1
	while index <= int(salt):
		newsalt = appapi.translate(conf.salt2, newsalt)
		index += 1
	return result, newsalt

def main():
	pone = phaseone()
	ponepointfive = appapi.split_in_four(pone)
	ptwo = phasetwo(ponepointfive)
	result, salt = phasethree(ptwo, ponepointfive)
	print("{0} : {1}".format(result, salt))

# Main
if __name__ == "__main__":
	main()
