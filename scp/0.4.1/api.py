import config as c
import random

def convert_string_to_number(istring):
	random.seed(istring)
	number = random.random()
	number = str(int(number * ((number + 1) * (number + 2) * 32000000)))
	return number

def convert_scv_to_ptwo_hash(number, length):
	new_number = number
	while int(len(str(new_number))) < int(length):
		new_number = new_number * 3 + 3
	if int(len(str(new_number))) > int(length):
		nn_string = str(new_number)
		a_result = [nn_string[i:i+c.hl] for i in range(0, len(nn_string), c.hl)]
		result = a_result[0]
	else:
		result = str(new_number)

	return result

def translate(tm, istring, amount = 1):
	ilist = [istring[i:i+amount] for i in range(0, len(istring), amount)]
	olist = []

	for letter in ilist:
		translation = tm.get(letter)
		olist.append(str(translation) if translation else letter)
	
	return "".join(olist)

def split_in_four(numbers):
	number_list = [numbers[i:i+4] for i in range(0, len(numbers), 4)]
	int_number_list = []
	dep_list = []
	for item in number_list: dep_list.append(int(item))
	for index, value in enumerate(number_list):
		int_number_list.append(int(value) + (int(index) * (int(value) // 2)) // c.vulnerability)
	salt = sum(int_number_list)
	if c.unsecure: 
		print("[DEBUG] DEP_LIST: {0} = {1}\n[DEBUG] INT_NUMBER_LIST: {2} = {3}".format(dep_list, sum(dep_list), int_number_list, sum(int_number_list)))
		print("[DEBUG] Phase 1.5 Result: {}".format(salt))
	return salt