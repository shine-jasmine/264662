file = open("/usercode/files/books.txt", "r")

for line in file:
	title=line.replace('\n','')
	count=len(title)
	print(f'{title[0]}{count}')
file.close()