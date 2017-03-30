# used to add to the database file. 
import sqlite3

# need to add to all def funcions
#	try:
#		.....
#	except:
#		conn.rollback()
#		return 200 # error code for fail add

def gameValueGames(sqlite_file, gameValues):
	""" Add the user data to the games database, the main data for the game. """
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	

	#Insert into the database
	c.execute('INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.

def gameValueGamesExp(sqlite_file, gameValues):
	"""Add the user data to the expansion database, expansion game information. """
	
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	
	#Insert into the database
	c.execute('INSERT INTO expansion_games VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.

def gameValueGamesId(sqlite_file, gameValues):
	""" Add the user data to the games database, what the main games format is and the barcode. """
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	

	#Insert into the database
	c.execute('INSERT INTO id_games_main_format VALUES (?, ?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.
	
def gameValueGamesIdFormat(sqlite_file, gameValues):
	""" Add the user data to the games database, the list of formats in a list.  """
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	

	#Insert into the database
	c.execute('INSERT INTO format_id_list VALUES (?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.
	
def gameValueGamesIdYear(sqlite_file, gameValues):
	""" Add the user data to the games database, what year the games use made. """
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	

	#Insert into the database
	c.execute('INSERT INTO year_id VALUES (?, ?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.
	
def gameValueGamesIdYearExp(sqlite_file, gameValues):
	""" Add the user data to the games database, the year id for the expansions. """
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	

	#Insert into the database
	c.execute('INSERT INTO year_id_expansion VALUES (?, ?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.
		
def gameValueGamesIdWindows(sqlite_file, gameValues):
	""" Add the user data to the games database, Windows version list. """
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	

	#Insert into the database
	c.execute('INSERT INTO id_game_main_windows_list VALUES (?, ?)', gameValues)
	
	# commite table
	conn.commit() #the data comits to the file but the program hanges at this point.
	
