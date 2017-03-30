import sqlite3
import random

def gameid (sqlite_file):
	"""Generating the ids"""
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	#Generate random number
	#set up for loop
	id_loop = 0
	# while loop for id generation
	while id_loop != 1:
		id_game_main = random.randint(1, 3000) # random number
		c.execute('SELECT id_game_main FROM games WHERE id_game_main = {} '.format(id_game_main))
		data = c.fetchone()
		id_game_check = data
		if id_game_check == None:
			id_loop = 1
			return id_game_main # return the id for the game. 
		else:
			continue
			
	
# old code #	c.execute('SELECT MAX(id_game_main) FROM games')
#	id_num = c.fetchone()[0]
#
#	if id_num == None:
#		id_game_main = 1
#		return id_game_main
#	else:
#		id_game_main = id_num +1
#		return id_game_main
	

# not right yet, need to be the same ish as above. may be 3001 to 5000 id range
def gameidExp(sqlite_file):
	"""Expansion id"""
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	#Generate random number
	#set up for loop
	id_loop = 0
	# while loop for id generation
	while id_loop != 1:
		id_game_main = random.randint(5000, 10000) # random number
		c.execute('SELECT expansion FROM expansion_games WHERE expansion = {} '.format(id_game_main)) # id_game_main ERROR
		data = c.fetchone()
		id_game_check = data
		if id_game_check == None:
			id_loop = 1
			return id_game_main # return the id for the game. 
		else:
			continue

def game_platform (sqlite_file):
	"""Generating a list for the platforms"""
	#connect to database
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	
	#set up for loop
	id_loop = 0
	# while loop for id generation
	while id_loop != 1:
		id_game_main = random.randint(1, 3000) # random number
		c.execute('SELECT id_game_main FROM games WHERE id_game_main = {} '.format(id_game_main))
		data = c.fetchone()
		id_game_check = data
		if id_game_check == None:
			id_loop = 1
			return id_game_main # return the id for the game. 
		else:
			continue
