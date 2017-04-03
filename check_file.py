#Check if the file is there or not
import file_check_ex


def check_file(sqlite_file):
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
