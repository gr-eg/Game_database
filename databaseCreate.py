#The creation of the game database


def createDatabase(sqliteFile):
	'''The creation of the database'''
	try:
		#connecting to the database
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()
		
		# c.executescript to create lots of tables at once
		c.execute('''
		
		CREATE TABLE games (id_game_main INTEGER PRIMARY KEY, title TEXT, description TEXT, 
		
		
		''')
		
		
	except:
		#Roll back if fails
		conn.rollback()
		print('\nFailed to create database')
