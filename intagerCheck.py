def intager (num):
	"""Check if the input is an integer or not"""
	try:
		num = int(num)
		return (num)
	except:
		print('\nPlease enter a valid number')
		return
