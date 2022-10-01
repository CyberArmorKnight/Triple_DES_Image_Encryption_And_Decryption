# importing libraries
import subprocess
import os


# functio to change the permissions
# of a given file
def change_permissions(args, filename):

	# command name
	cmd = 'chmod'

	# getting the permissions of
	# the file before chmod
	ls = 'ls'

	data = subprocess.Popen([ls, '-l', filename], stdout = subprocess.PIPE)

	output = str(data.communicate())

	print('file permissions before chmod % s: ' %(args))
	print(output)

	# executing chmod on the specified file
	temp = subprocess.Popen([cmd, args, filename], stdout = subprocess.PIPE)

	# getting the permissions of the
	# file after chmod
	data = subprocess.Popen([ls, '-l', filename], stdout = subprocess.PIPE)

	output = str(data.communicate())

	# printing the permissions after chmod
	print('file permissions after chmod % s: ' %(args))
	print(output)

if __name__ == '__main__':
		
	# changing the permissions of 'sample.txt'
	change_permissions('755', 'sample.txt')
