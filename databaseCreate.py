#The creation of the game database


def createDatabase(sqliteFile):
	'''The creation of the database'''
	
		#connecting to the database
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()
