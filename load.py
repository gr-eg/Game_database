''' A Game database to catalogue the games I own.'''


#Loading file to select what the user does.


#Import section 
import intagerCheck #File to check and see if it is an intager
import databaseCreate #Create the database


#Varibles set up
userSelect = None
sqliteFile = ''
userSelectOptions = [0,1]

#Body of code#

#Welcome code
print('\nGame database')
print('\nby Matthew Langner')
print('\n\nPlease select on option')

#User selects what they want option the want. 
#Loop to get the right answer

while userSelect != 0:
	print('\n\n1 = Create a new database \n2 = Edit an exsisting database \n0 = Exit the program')
	
	#To save the user file name of the sqlite file to transfer between userSelect options. 
	sqliteFile = sqliteFile
	
	#Get the selection from the user. 
	userSelect = intagerCheck.intager(input('\nPlease enter your selection: ')) # Get the users option and checks for an intager. 
	
	if userSelect in userSelectOptions:
		if userSelect == 1:
			#create database
			databaseCreate.createFile()
		elif userSelect == 2:
			#edit database
		elif userSelect == 0:
			print('\nThanks for playing')
		else:
			print('\nError 01')
	else:
		print('\nPlease choose a valid option')
