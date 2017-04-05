#Check to see of the file is there or not

def checkFile (sqliteCheck):
	""" Check to see if the file exsists. return 0 = no file - 1 = file if there """
	try:
		with open(sqliteCheck) as file:
			fileCheck = 1
			# There is a file return the value 1
			return fileCheck
	except IOError as f:
		fileCheck = 0
		# There is no file, return the value 0 
		return fileCheck
