import sqlite3 # sqlite 3 database
import file_check_ex # to check if there is a file
import database # creating, editing, deleting the database
import intCheck # check that it is an integar


option = None # choose what manu option they want
sqlite_file = "" # the name of the sqlite3 file
option_list = (0, 1, 2, 3) # the menu list option to use with option variable
#option_tuple = None # Info from the intCheck held in a tuple. Use var[0] 


# print opening line
print('\nWelcome to the texted based game database of your games')
print('\nPlease enter a number to select an option')

# user selection of options 
while option != 0:
	print('\nExit program = 0 \nNew database = 1\nEdit database = 2 \nDelete database = 3')
	
	# remember the sqlit3 file name 
	sqlite_file = sqlite_file
	
	#Get user input for menu select
	option = intCheck.int_check(input('\nEnter number: ')) # get user input and check it is an intager
	if option in option_list:
		option = option
		if option == 1:
			sqlite_file = database.createDatabase()
		elif option == 2:
			database.editDatabase(sqlite_file)
		elif option == 3:
			print("\nThis is where you would delete a database, but not yet.")
		elif option == 0:
			
			print("\nThanks for playing")
		else:
			print("\nother option") # temp line
	else:
		print("\nPlease re-enter a valid number")


# add to the columes in the database to make them equel for the game and game expasion so I can use the same gameVaule to input both. 
