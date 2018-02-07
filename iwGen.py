# -*- coding: utf-8 -*-
import os

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
	text = ''
	for k in fs.keys():
		text += '#%s\n' % k
		for p in fs[k]:
			text += '%s\n' % p
	with open(fname, 'w') as o:
		o.write(text.strip())

def main():
	fileLstWriteOut('itemList.htm')

if __name__ == '__main__':
	main()

