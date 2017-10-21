# SCP
# Made by AnthonyCodes
# Source Code: https://github.com/anthonycodes/Python-Scripts/tree/master/scp/

# Imports
import config as conf
import api as appapi
from sys import argv, exit
from argparse import ArgumentParser

# Variables
unsecure = conf.unsecure
parser = ArgumentParser()

# Argument Parsing
mode = parser.add_mutually_exclusive_group()
mode.add_argument("-f", "--file", help = "indicates if what you want to hash is a file", action = "store_true")
mode.add_argument("-b", "--bytes", help = "indicates if what you want to hash is a bytes file", action = "store_true")
parser.add_argument("source", type = str, help = "if you're hashing a string, put any text here.\n if you chose file or bytes, put the filename here.", nargs='+')
args = parser.parse_args()
sf = " ".join(args.source)

# Functions
def phaseone(istring):
	result = appapi.convert_string_to_number(istring)
	if unsecure: print("[DEBUG] Phase 1 Result: {}".format(result))
	return result

def phasetwo(integer):
	result = appapi.convert_scv_to_ptwo_hash(int(integer), conf.hl)
	if unsecure: print("[DEBUG] Phase 2 Result: {}".format(result))
	return result

def phasethree(string, salt):
	result = appapi.translate(conf.scv_to_chars, string, 2)
	if unsecure: print("[DEBUG] Phase 3 Result: {}".format(result))
	newsalt = appapi.translate(conf.salt1, str(salt))
	index = 1
	while index <= int(salt):
		newsalt = appapi.translate(conf.salt2, newsalt)
		index += 1
	result = result.lower()
	newsalt = newsalt.lower()
	return result, newsalt

def main(args, sf):
	if args.file or args.bytes:
		file_contents = []
		try:
			if args.bytes:
				if unsecure: print("[DEBUG] Opening bytes file '{}'...".format(sf))
				with open(sf, "rb") as file:
					file_contents.append(str(file.read()))
				rawfile = "".join(file_contents)
			elif args.file:
				if unsecure: print("[DEBUG] Opening file '{}'...".format(sf))
				with open(sf, "r") as file:
					rawfile = str(file.read())
			sf = rawfile
		except Exception as err:
			if conf.errors: print("[ERROR] {}".format(err))
			else:
				print("There was a problem opening the file.")
			exit()

	pone = phaseone(sf)
	ponepointfive = appapi.split_in_four(pone)
	ptwo = phasetwo(ponepointfive)
	result, salt = phasethree(ptwo, ponepointfive)
	if unsecure: print("{0} : {1}".format(result, salt))
	else: print(result)

# Main
if __name__ == "__main__":
	main(args, sf)