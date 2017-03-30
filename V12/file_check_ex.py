def checking_file (sqlite_check):
	""" Check to see if the file exsists. return 0 = no file - 1 = file if there """
	try:
		with open(sqlite_check) as file:
			file_ex_check = 1
			# There is a file return the value 1
			return file_ex_check
	except IOError as f:
		file_ex_check = 0
		# There is no file, return the value 0 
		return file_ex_check
