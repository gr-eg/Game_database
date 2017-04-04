#Import section
import sqlite3 # imports to sqlite3 module


def createFile ():
	''''To create a new file'''
	sqliteFile = ''
	sqliteFile = str(input('\nPlease enter your file name: ')).strip()
	sqliteFileLenght = len(sqliteFile)
	while sqliteFileLenght == 0:
		sqliteFile = str(input('\nNo filename entered, please try again.\nPlease enter your file name: ')).strip()
		sqliteFileLenght = len(sqlite_file_enter)