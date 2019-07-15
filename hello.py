
def startup():
	try:
		endNum=int(input('Enter a number: '))

	except ValueError:
		startup()
	
	else:
		input('Counting to ' + str(endNum) +' - press Enter to start!')
		for x in range(1, endNum+1,1):
			print(x)

	print('Great Job!')

def startdown(): 
	while True:
		myName=input("Enter your name please? ").capitalize()
		if str.isalpha(myName):
			print("Hello " + myName)
			startup()
			break

		else:
			startdown()
			break

startdown()