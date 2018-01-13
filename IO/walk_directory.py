import os
# def walk(directory):
# 	for name in os.listdir(directory):
# 		# os.path.join takes directory and a filename and joins
# 		# them into a complete path
# 		path = os.path.join(directory, name)

# 		if os.path.isfile(path):
# 			print(path)
# 		else:
# 			walk(path) # recursively go through the current directory

# walk('/Users/guoyifeng/PycharmProjects/python_study/')

# walk directory by os.walk
# print(os.walk('/Users/guoyifeng/PycharmProjects/python_study/'))

# Modify walk so that instead of printing the names of the files, 
# it returns a list of names.
res = []
def walk(dir, res):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)

		if os.path.isfile(path):
			res.append(path)
		else:
			walk(path, res)
	return res

final_res = walk('/Users/guoyifeng/PycharmProjects/python_study/', res)
for path in final_res:
	print(path)