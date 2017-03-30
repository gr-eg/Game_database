import gameValueEntry # enters the game data to the database
import ids
import sqlite3

# add the game data to the games database. 
def gameDataComm(sqlite_file, numVal=0, expansion = ""):
	"""Getting the data for each game to enter into the database"""
	# for database table - games
	# numVal = 0, no expansion. numVal = 1, there is and expansion.
	#Getting the game data
	
	#Expansion or no expansion title print text
	if numVal == 0:
		# for database table - games
		id_game_main = ids.gameid(sqlite_file)
		print('Now please enter your game data')
	elif numVal == 1:
		# id game expanstion # need to get id for epansion and id of original game
		print('Now please enter your expansion game data')
	else:
		return(200)

	#Title
	#Title Main
	if numVal == 0:
		title = input('Please enter your game title: ')
	#Title expansion
	elif numVal == 1:
		title = input('Please enter your game title for the expansion: ')
	else:
		return(200)

	#Sub title
	sub_title = input('Please enter your sub title: ')

	#offline multi player or single player
	offline_player_number = range(1,13,1)
	offline_multi_player = ""

	while offline_multi_player not in offline_player_number:
		offline_multi_player = input('1 = single player, 2 - 12 = local multi player: ')
		try:
			offline_multi_player = int(offline_multi_player)
		except:
			print('Please try again')
		else:
			continue

	#Online multi payer #change code to match above
	online_player_number = range(0,33,1)# need to add an option for 0 - can we do a list of sorts like [0, range(2, 33, 1)] this doesn't work. 
	online_multi_player = ""
	while online_multi_player not in online_player_number:
		online_multi_player = input('Please enter the number of online multi players (Max 32): ')
		try:
			online_multi_player = int(online_multi_player)
		except:
			print('Please try again')
		else:
			online_multi_player = int(online_multi_player)

	#Age rating
	age_rating_number = range(1,19,1)
	age_rating = ""
	while age_rating not in age_rating_number:
		age_rating = input('Enter the age rating (max 18): ')
		try:
			age_rating = int(age_rating)
		except:
			print('Please try again')
		else:
			age_rating = int(age_rating)
	
	#Platform / format - need loop to ask for / to get platform
	#have other option for platforms that are not listed to add
	
	#connecting to the database o get the list of platforms 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	#Quary database to get the list 
	c.execute('SELECT * FROM platform_id_list')
	#print the list of platforms. 
	plist = c.fetchall()
	
	platform_option = [0]
	
	for i in plist:
		iplist0 = i[0]
		iplist1 = i[1]
		print(iplist0, ' ', iplist1)
		platform_option.append(iplist0)
		
	print(platform_option)
	
	platform_option_selection = '#'
	print('first show') # temp line
	
	while platform_option_selection not in platform_option:
		platform_option_selection = input('Please select your platform or 0 to add a new one: ')
		platform_option_selection = int(platform_option_selection)
		print('second one') # temp line
		try:
			format_id = int(platform_option_selection)
			print(format_id, 'this is the format id') #temp line
		except:
			print('Please try again')
		else:
			continue
		
	input('stop')
		
	# year - need year id and year. use with platform
	
	#Publisher
	publisher = input('Publisher: ')

	#Developer
	developer = input('Developer: ')

	#Completed - needs a loop to get y or n answer
	completed_list = ('y', 'Y', 'n', 'N')
	completed = ""
	while completed not in completed_list:
		completed = input('Completed, Y or N: ')

	# the game description
	description = input('Description: ')

	# notes for each game
	notes = input('Any notes? ')
	
	
	if numVal == 0: 
		#ask to see if there is an expansion
		expansion_list_val = ('y', 'Y', 'n', 'N')
		expansion_val = ''
		numValEntry = 0
		while expansion_val not in expansion_list_val:
			expansion_val = input('Does the game have expansion(s) or DLCs?, Y or N: ')
# need to add more thatn one expansion option?		# the if has an error, not checking the y or n. Going stright to else	
		if expansion_val in ('y', 'Y'): # y if there is an expansion
			# there is an expansion
			expansion = ids.gameidExp(sqlite_file)	#generate an id for the game expansion table
			numVal = 1
		elif expansion_val in ('n', 'N'):
			numVal = 0
		else:
			numVal = 0
	elif numVal == 1:
		numValEntry = 1
	
	else:
		Print ("error")
		
	# if there was an expansion or not	
	if numValEntry == 0: # normal game insert
		# set up for the INSERT into main table 
		gameValues = [id_game_main, title, sub_title, offline_multi_player, online_multi_player, age_rating, publisher, developer, completed, description, expansion, notes]
			
		#inseting into the games table
		gameValueEntry.gameValueGames(sqlite_file, gameValues)
		
		# id_games_format
		gameValues = [id_game_main, format_id, barcode]
		
		gameValueEntry.gameValueGamesId(sqlite_file, gameValues)
		
		#format_id_list
		
		#year_id
		
		#year_id_expansion
		
		#id_game_win_list
		
		#win_version_list
		
		
		
	elif numValEntry == 1: #expansion insert
		# set up for the INSERT into
		gameValues = [expansion, title, sub_title, offline_multi_player, online_multi_player, age_rating, publisher, developer, completed, description, notes]
		
		#inseting into the games table
		gameValueEntry.gameValueGamesExp(sqlite_file, gameValues)
		
		# add smae for dlc as needed. 

	else:
		print("Game failed to add, please re-enter your game details")
			
	#return the value
	if numVal == 1: 
		return ("Expansion", expansion) # returns 1 and id for expansion
	else:
		return ("noExpansion")
