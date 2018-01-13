# -*- coding: utf-8 -*-
# In a large collection of MP3 files,there may be more than one copy of the same song, 
# stored in different directories or with different file names. The goal of this 
# exercise is to search for these duplicates.
import os
import hashlib


# step 1: search the directory recursively and find all the mp3 files
mp3_list = []
def search_mp3(dir, mp3_list):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)

		if os.path.isfile(path):
			if path.split('.')[-1] == 'mp3':  # if suffix is mp3
				mp3_list.append(path)
			else:
				continue
		else:
			search_mp3(path, mp3_list)  # recursively search in the sub-directory
	return mp3_list

mp3_list = search_mp3('test_mp3_file', mp3_list)
# for mp3 in mp3_list:
# 	print(mp3)

def calc_checksum(mp3_list):
    '''
    calculate checksum of each mp3 file in the list by using md5 hash algorithm
    :param mp3_list: 
    :return: 
    '''
    res = {}  # key: checksum, value: file
    for mp3_path in mp3_list:
        md5sum = hashlib.md5(open(mp3_path, 'rb').read()).hexdigest()
        if md5sum not in res:
            res[md5sum] = mp3_path
        else:
            print('There is duplicate in the current mp3 list which is %s') \
                 %(mp3_path.split('/')[-1])
            return
    print('No duplicate mp3 file in current directory.')

calc_checksum(mp3_list)

