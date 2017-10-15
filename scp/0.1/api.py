import config as c

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

def translate(tm, istring):
	ilist = list(istring)
	olist = []

	for letter in ilist:
		translation = tm.get(letter)
		olist.append(str(translation) if translation else letter)
	
	return "".join(olist)

def two_translate(tm, istring):
	ilist = [istring[i:i+2] for i in range(0, len(istring), 2)]
	olist = []

	for letter in ilist:
		translation = tm.get(letter)
		olist.append(str(translation) if translation else letter)
	
	return "".join(olist)

def split_in_four(numbers):
	number_list = [numbers[i:i+4] for i in range(0, len(numbers), 4)]
	int_number_list = []
	for item in number_list: int_number_list.append(int(item))
	salt = sum(int_number_list)
	if c.debug: print("[DEBUG] Phase 1.5 Result: {}".format(salt))
	return salt