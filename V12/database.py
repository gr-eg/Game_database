import sqlite3 # use sqlite3 database
import file_check_ex # to check if there is a file
import intCheck # check that it is an integer
import gameDataEntry # entering the data for each game
import ids # getting the ids for the games

def createDatabase ():
	"""To check and create a new database file"""
	new_file = 1
	while new_file != 0:
		sqlite_file = ''
		sqlite_file_enter = str(input('\nPlease enter your file name: ')).strip()
		sqlite_file_lenght = len(sqlite_file_enter)
		while sqlite_file_lenght == 0:
			sqlite_file_enter = str(input('\nNo filename entered, please try again.\nPlease enter your file name: ')).strip()
			sqlite_file_lenght = len(sqlite_file_enter)
		sqlite_file = sqlite_file_enter + ('.sqlite')
		new_file = file_check_ex.checking_file(sqlite_file)
		if new_file == 1:
			print('\nThere is a file here already, please try agian')
		else:
			pass
	print('\nDatabase will now be created')

	# try to make database
	try:

		# Values for set databases
		platform_id_list_values = [('1', 'megadrive'),
		('2', 'megacd'),
		('3', 'saturn'),
		('4', 'n46'),
		('5', 'gamecube'),
		('6', 'wii'),
		('7', 'wiiu'),
		('8', 'xbox'),
		('9', 'psx'),
		('10', 'ps2'),
		('11', 'ps3'),
		('12', 'gameboy'),
		('13', 'gameboy_colour'),
		('14', 'ds'),
		('15', '3ds'),
		('16', 'dreamcast'),
		('17', 'andriod'),
		('18', 'pc'),
		('19', 'Switch'),
		]
		#add things like e-shop as a sub menu, may be new table.

		''' not yet implimented
		# Value set subset of platform
		platform_id_list_sub_values = [('1', 'Wii e-shop'),
		('2', 'WiiU e-shop'),
		('3', 'PSN'),
		('4', '3ds e-shop'),
		('5', 'Steam'),
		('6', 'GOG.com'),
		('7', 'Humble bundel'),
		('8', 'Uplay'),
		('9', 'pc disc'),
		]
		'''

		windowsOS = [('1', 'windows 95',),
		('2', 'windows 98',),
		('3', 'windows 2000',),
		('4', 'windows XP',),
		('5', 'windows 7',),
		('6', 'windows 10',)
		]

		#connecting to the database
		conn = sqlite3.connect(sqlite_file)
		c = conn.cursor()

		# look at what tables we need!!!!

		# c.executescript to create lots of tables at once
		c.executescript("""

		CREATE TABLE games (id_game_main INTEGER PRIMARY KEY, title TEXT, sub_title TEXT, offline_multi_player INTEGER, online_multi_player INTEGER, age_rating INTEGER, publisher TEXT, developer TEXT, completed TEXT, description TEXT, expansion INTEGER, note TEXT);

		CREATE TABLE expansion_games (expansion INTEGER PRIMARY KEY, title TEXT, sub_title TEXT, offline_multi_player INTEGER, online_multi_player INTEGER, age_rating INTEGER, publisher TEXT, developer TEXT, completed TEXT, description TEXT, note TEXT);

		CREATE TABLE id_games_main_format (id_game_main INTEGER, format_id INTEGER, barcode INTEGER);

		CREATE TABLE id_games_expansion_format (expansion INTEGER, format_id INTEGER, barcode INTEGER);

		CREATE TABLE platform_id_list (format_id INTEGER PRIMARY KEY, platform TEXT);

		CREATE TABLE year_id (id_game_main INTEGER, format_id INTEGER, year INTEGER);

		CREATE TABLE year_id_expansion (expansion INTEGER, format_id INTEGER, year INTEGER);

		CREATE TABLE id_game_main_windows_list (id_game_main INTEGER, windows_version_id INTEGER);

		CREATE TABLE id_game_expansion_windows_list (expansion INTEGER, windows_version_id INTEGER);

		CREATE TABLE windows_version_list (windows_version_id INTEGER PRIMARY KEY, windows_version TEXT);

		""")


		# insert preset values in to the database
		c.executemany('INSERT INTO platform_id_list VALUES (?, ?)', platform_id_list_values)
		c.executemany('INSERT INTO windows_version_list VALUES (?, ?)', windowsOS)


		# commite table
		conn.commit()

	#if if fails
	except:
		# Roll back
		conn.rollback()
		print('\nFailed to make database')

	#closing the connection
	conn.close()

	print('\nThe database have been created')

	return sqlite_file


def editDatabase (sqlite_file):
	"""Make ready to use an exsiting database file"""
	# Variables
	foo = "a"
	sqlite_file_enter = "0"

	if sqlite_file != "":
		print('\nResently made database file - ', sqlite_file) # Ask if they what to use the database they have just made.

		while foo != "i":
		#ask if the user wants to use the file they have just made.
			sqlite_file_enter = str(input('\nEnter 1 if you want to used ' + sqlite_file + ' or \nEnter 2 to enter an exsisting database file name\nEnter number = ')).strip()
			if sqlite_file_enter == "1":
				sqlite_file = sqlite_file
				databaseEntryCommon(sqlite_file)
				foo = "i"
			elif sqlite_file_enter == "2": # if not they will be asked to open up an exsiting file. It also checks to see if the file is there or not.
				file_open_check = ""
				sqlite_file = sqlite_file_enter + ('.sqlite')
				# used to check if the file is there or not.
				file_open_check = file_check_ex.checking_file(sqlite_file)
				while file_open_check != 1:
					sqlite_file = str(input('\nPlease re-enter the file name you want to open: ')).strip()
					sqlite_file = sqlite_file + ('.sqlite')
					file_open_check = file_check_ex.checking_file(sqlite_file)
					if file_open_check == 1:
						foo= "i"
					elif file_open_check == 0:
						print('\nThere isn\'t a file here, please try agian')
					else:
						pass
				# goes to the def common database section
				databaseEntryCommon(sqlite_file)

			else:
				print("\nInvalid selection, please rselect an option")


	# if no file has just been created the user is asked to open a file that has been made already.
	elif sqlite_file == "":
		file_open_check = ""
		while file_open_check != 1:
			sqlite_file = str(input('\nPlease enter the file name you want to open: ')).strip()
			sqlite_file = sqlite_file + ('.sqlite')
			file_open_check = file_check_ex.checking_file(sqlite_file)
			if file_open_check == 0:
				print('\nThere isn\'t a file here, please try agian')
			else:
				pass
		# goes to the def common database section
		databaseEntryCommon(sqlite_file)

	else:
		input('\nAn error for file open. Please exit and re-start the program. Press enter to close the stop the program')
		sys.exit


def databaseEntryCommon (sqlite_file):
	"""To edit and comit the data to the database"""
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	#Show how many games there are in the database
	c.execute('SELECT count(*) FROM games')
	data_count = c.fetchone()[0]
	data_str = str(data_count)
	print('\nYou currently have ' + data_str + ' game(s) in your database')

	# creating a loop to get the data to at to the fields at a later time. This next section could be put into a class or def, once I find out how to do it.

	# while loop to loop getting data

	# variable for game data while loop
	add_game = 100
	add_game_list = (0, 1, 2, 3)
	while add_game != 0:
		add_game = intCheck.int_check(input('\nPlease select an option\nAdd a game = 1\nEdit an game = 2\nDelete a game = 3\nFinished adding games = 0: '))

		while add_game not in add_game_list:
			add_game = intCheck.int_check(input('\nPlease select an option\nAdd a game = 1\nEdit an game = 2\nDelete a game = 3\nFinished adding games = 0: '))
		# add a game
		if add_game == 1:
			numVal = 0
			gameData = gameDataEntry.gameDataComm(sqlite_file, numVal)

			if gameData[0] == "Expansion":
				expansion = gameData[1]
				numVal = 1
				gameData = gameDataEntry.gameDataComm(sqlite_file, numVal, expansion)
			elif gameData[0] == "noExpansion":
				continue
			else:
				continue

		# edit a game
		elif add_game == 2:
			print('\nCan\'t edit yet')

		# delete a game and expansions
		elif add_game == 3:
			print('\nCan\'t delete games yet')

		# finished adding games and commit it to the database
		elif add_game == 0:
			print('\nGames added - nearly')
			add_game = 0

		else:
			print("\nHas it stopped?")
