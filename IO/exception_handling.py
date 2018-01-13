# Python starts by executing the try clause. If all goes well, 
# it skips the except clause and proceeds. If an exception occurs, 
# it jumps out of the try clause and executes the except clause.
try:
	fp = open('random_file.txt')
	for line in fp:
		print(line)
	fp.close()
except:
	print('Something went wrong')