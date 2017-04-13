'''To check and create a new database file.'''

#Import section

import fileCheckExistence
import databaseCreate

def newFile ():
	''''To check for a new file'''
	sqliteFile = ''
	sqliteFile = str(input('\nPlease enter your new file name: ')).strip()
	sqliteFileLenght = len(sqliteFile)
	while True:
		if sqliteFileLenght == 0:
			sqliteFile = str(input('\nInvalid or duplicate file name had been entered, please try again.\nPlease enter your new file name: ')).strip()
			sqliteFileLenght = len(sqliteFile)
		elif sqliteFileLenght > 0:
			sqliteFile += ('.sqlite')
			checkFile = fileCheckExistence.checkFile(sqliteFile)
			if checkFile == 1:
				sqliteFileLenght = 0
			elif checkFile == 0:
				databaseCreate.createDatabase(sqliteFile)
				return # may need to add return sqliteFile for option to in the load file. 
		else:
			print('Error code 02')
			sys.exit('Error code 02')
	return
