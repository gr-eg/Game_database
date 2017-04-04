#Import section
import sqlite3 # imports to sqlite3 module


def createFile ():
	''''To create a new file'''
	while True:
		sqliteFile = ''
		sqliteFile = str(input('\nPlease enter your new file name: ')).strip()
		sqliteFileLenght = len(sqliteFile)
		if sqliteFileLenght == 0:
			sqliteFile = str(input('\nNo filename entered, please try again.\nPlease enter your new file name: ')).strip()
			sqliteFileLenght = len(sqlite_file_enter)
		elif sqliteFileLenght > 0:
			return sqliteFile
		else:
			print('Error code 02')
			return 