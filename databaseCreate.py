#The creation of the game database
import sqlite3
import databaseVersion


def createDatabase(sqliteFile):
	'''The creation of the database'''
	try:
		#connecting to the database
		conn = sqlite3.connect(sqliteFile)
		c = conn.cursor()
		
		print('Connected') #temp line
		
		# c.executescript to create lots of tables at once
		c.execute('''CREATE TABLE games (id_game_main INTEGER PRIMARY KEY, title TEXT, description TEXT)''')
		
		print('created table games')
		
		#database version identifier 
		c.execute('''CREATE TABLE databaseVersion (version INTEGER PRIMARY KEY)''')
		
		print('created table databaseversion')
		DBversionNumber = databaseVersion.versionCreate()
		print(DBversionNumber, ' not in function')
		input('wait')
		
		#add preset values
		c.execute('INSERT INTO databaseVersion VALUES(?)', DBversionNumber) # not working
		
		print('inserted databaseversion')
		
		conn.commit()
		
		return 
		
	except:
		#Roll back if fails
		conn.rollback()
		print('\nFailed to create database')
		
		return
