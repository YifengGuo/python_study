# fp = open('austen-emma.txt', 'r')
# for line in fp:
# 	print(line)

# write something to the file
fout = open('test_for_io.txt', 'w')
line1 = 'This is the beginning.\n'
fout.write(line1)
# the file object keeps track of where it is, 
# so if you call write again, it adds the new data to the end.
line2 = 'This is the second line.\n'
fout.write(line2)

fout.close()
