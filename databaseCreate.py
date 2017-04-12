#The creation of the game database


def createDatabase(sqliteFile):
	'''The creation of the database'''
	try:
		#connecting to the database
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()
		
		
	except:
		#Roll back if fails
		conn.rollback()
		print('\nFailed to create database')