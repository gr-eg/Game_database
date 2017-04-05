#Import section
import sqlite3 # imports to sqlite3 module


def createFile ():
	''''To create a new file'''
	sqliteFile = ''
	sqliteFile = str(input('\nPlease enter your new file name: ')).strip()
	sqliteFileLenght = len(sqliteFile)
	while True:
		if sqliteFileLenght == 0:
			sqliteFile = str(input('\nNo filename entered, please try again.\nPlease enter your new file name: ')).strip()
			sqliteFileLenght = len(sqliteFile)
			#add in file check
		elif sqliteFileLenght > 0:
			return sqliteFile
		else:
			print('Error code 02')
			sys.exit('Error code 02')
			return 
