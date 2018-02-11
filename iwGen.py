# -*- coding: utf-8 -*-
import os
import shutil
import json
from PIL import Image

import azLib as al

DIR_THUMB = 'thumb'

def imgCompress(fname, sname):
	img = Image.open(fname)
	img.thumbnail((128, 128))
	img.save(sname, 'PNG')

def fileStructure():
	
	fo = al.FileOperation()
	fileLst = fo.fileLstMaker('.', ['.jpg', '.jpeg', '.gif', '.png', '.JPG', '.PNG'])
	classified = {}

	currentFolder = ''
	for p in fileLst:
		tmp = os.path.split(p)
		# print tmp
		fname = tmp[-1]
		folder = tmp[0]
		imgCompress(p, './%s/'%DIR_THUMB + fname)
		if folder == currentFolder:
			classified[folder.replace('\\', '/')].append([p.replace('\\', '/'), fname])
		else:
			classified[folder.replace('\\', '/')] = [[p.replace('\\', '/'), fname]]
		currentFolder = folder
	return classified

def fileLstWriteOut(fname):
	try:
		shutil.rmtree(DIR_THUMB)
	except:
		print('It seems that folder [%s] has not been created.' % DIR_THUMB)
	os.mkdir(DIR_THUMB)
	fs = fileStructure()
	with open(fname,'w') as f:
		f.write(json.dumps(fs))

def main():
	fileLstWriteOut('itemList.json')

if __name__ == '__main__':
	main()

