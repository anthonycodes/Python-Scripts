import urllib.request
from bs4 import BeautifulSoup
from os import system
from sys import argv
from datetime import datetime

system("cls")
print(
"""### URL SCRAPER ###
Please enter a URL to scrape.""")

url = input(">> ")
if url == "":
	print("Please specify a URL")
	quit()

try:
	source = urllib.request.urlopen(url)
except:
	print("Error using that URL,\nCheck it again.")
	quit()

soup = BeautifulSoup(source, "html.parser")
arg = input("What should I scrape for?\n>> ")

if arg == "":
	print(
		"""Options:
		links
		images
		tables
		paragraphs
		source
		all""")
else:
	args = arg.split()
	toOut = True
	result = []
	if args[0] == "links":
		links = soup.find_all("a")
		for link in links:
			result.append(link.get("href"))
	elif args[0] == "images":
		imagesLinks = soup.find_all("img")
		for link in imagesLinks:
			result.append(link.get("src"))
	elif args[0] == "tables":
		name = input("Table name (*): ")
		
		if name == "":
			tables = soup.find("table")
		else:
			tables = soup.find("table", {"class" : "{}".format(name)})
		
		tableRows = tables.find_all("tr")

		for row in tableRows:
			if row.find("th") == None: continue
			result.append("\n" + row.find("th").getText())

			for item in row.find_all("td"):
				result.append("\- " + item.getText())
	elif args[0] == "paragraphs":
		par = soup.find_all("p")
		for paragraphs in par:
			result.append(paragraphs)
	elif args[0] == "source":
		result.append(soup)
	elif args[0] == "all":
		name = input("Table name (*): ")
		
		result.append("\n==[[ TABLES ]]==\n")
		if name == "":
			tables = soup.find("table")
		else:
			tables = soup.find("table", {"class" : "{}".format(name)})
		
		try:
			tableRows = tables.find_all("tr")

			for row in tableRows:
				if row.find("th") == None: continue
				result.append("\n" + row.find("th").getText())

			for item in row.find_all("td"):
				result.append("\- " + item.getText())

		except:
			empty = ""
			# ERROR GETTING TABLES

		result.append("\n==[[ LINKS ]]==\n")
		links = soup.find_all("a")
		for link in links:
			result.append(link.get("href"))
		result.append("\n==[[ IMAGES ]]==\n")
		imagesLinks = soup.find_all("img")
		for link in imagesLinks:
			result.append(link.get("src"))
	else:
		print(
		"""Options:
		links
		images
		tables
		paragraphs
		source
		all""")
		toOut = False

	if toOut:
		logname = datetime.now().strftime("%H-%M-%S")
		logname = "log" + logname + ".txt"
		print("SAVING...")
		try:
			system("cd out")
		except:
			system("mkdir out && cd out")
		with open("./out/" + logname, "w") as file:
			for contents in result:
				file.write(contents + "\n")
		print("SAVED TO {}".format("log" + logname))