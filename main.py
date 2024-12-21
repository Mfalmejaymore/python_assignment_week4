cnt = 2

if cnt == 2:
	print('is')
else:
	print('no')

print(str(cnt))

# now the real code begins

# functions


def question1():
	myfile = '';
	thedata = "---"
	# get log.txt
	try:
		myfile = open('log.txt','r')
		print('[log.txt] has been read successfully (first try)')
	except FileNotFoundError:

		print('[log.txt] doesnt exist, attempting to create it')

		# mek it if not exist
		myfile = open('log.txt','w')
		with myfile:
			thedata = 'file log is in here ....'
			myfile.write(thedata)
			print('file created successfully [log.txt]')

		myfile = open('log.txt','r')
		print('file has been read [log.txt]')

	# put its content into a new file
	with myfile:
		thedata = myfile.read()
		thedata = "-> " + thedata
		print('file content has been retreived [log.txt]')

	myfile = open('log_copy.txt','w')

	with myfile:
		myfile.write(thedata)
		print('file content has copied to a new file [log_copy.txt]\n')

	print('\n[end of question 1 code]')

	return 0;

def question2():

	fname = input('enter the name of a file : ')
	myfile = ''

	try:
		myfile = open(fname,'r')

		with myfile:
			data = myfile.read()
			data = '\n +------[start]----+\n\n' + str(data) + '\n\n +------[end]------+\n'
			print(data)

	except FileNotFoundError:
		print('\nsorry ['+ fname +'] doesn\'t exist')
	except:
		print('an unknown error occurred, please try again')
	finally:
		print('\n[end of question 2 code]')

	return 0;

# the system itself

myop = input("enter request number. \n[0 - modify a file]\n[1 - read a file]\nyour request number : ")

try:
	if int(myop) == 0:
		question1()
	else:
		question2()

	print("[end of code]")
except:
	print('the input was not valid, try again later')

