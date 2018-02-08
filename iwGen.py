# -*- coding: utf-8 -*-
import os
import json

import azLib as al

def fileStructure():
	fo = al.FileOperation()
	fileLst = fo.fileLstMaker('.', ['.jpg', '.jpeg', '.gif', '.png'])
	classified = {}

	currentFolder = ''
	for p in fileLst:
		folder = os.path.split(p)[0]
		if folder == currentFolder:
			classified[folder.replace('\\', '/')].append(p.replace('\\', '/'))
		else:
			classified[folder.replace('\\', '/')] = [p.replace('\\', '/')]
		currentFolder = folder
	return classified

def fileLstWriteOut(fname):
	fs = fileStructure()
	with open(fname,'w') as f:
		f.write(json.dumps(fs))


def main():
	fileLstWriteOut('itemList.json')

if __name__ == '__main__':
	main()

