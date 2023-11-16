# -*- coding: utf-8 -*-
# Need these 3rd-party libraries:
# pillow, bottle, gevent

import os
import shutil
import json
from PIL import Image
from bottle import route, run, template, static_file
from gevent import monkey

import azLib as al

DIR_THUMB = 'thumb'
currentFileLst = ''

def imgCompress(fname, sname):
	img = Image.open(fname)
	img.thumbnail((128, 128))
	img.save(sname, 'PNG')


def fileStructure():
	fo = al.FileOperation()
	fileLst = fo.fileLstMaker('.', ['.jpg', '.jpeg', '.gif', '.png', '.JPG', '.PNG'])
	classified = {}

	print('Remove old thumbnail...')
	# os.system('rm ./%s/*' % DIR_THUMB)
	shutil.rmtree(DIR_THUMB, ignore_errors=True)
	os.mkdir(DIR_THUMB)

	currentFolder = ''
	for p in fileLst:
		tmp = os.path.split(p)
		fname = tmp[-1]
		folder = tmp[0]

		if folder != './'+DIR_THUMB:
			imgCompress(p, './%s/'%DIR_THUMB + '%s_%s'%(folder, fname))
			if folder == currentFolder:
				classified[folder].append([p, fname])
			else:
				classified[folder] = [[p, fname]]
			currentFolder = folder
	return classified


def fileLst2JSON():
	return json.dumps(fileStructure())


@route('/')
def access():
	# global currentFileLst
	# currentFileLst = fileLst2JSON()
	with open('index.htm', 'r') as o:
		return o.read().replace('{{file_json}}', currentFileLst).encode('utf-8')

@route('/viewer.htm')
def viewer():
	with open('viewer.htm', 'r') as o:
		return o.read().replace('{{dict_files}}', currentFileLst+'[cata]').encode('utf-8')

@route('/thumb/<imgName>')
def thumbViewer(imgName):
	return static_file(imgName, root='./thumb')

@route('/<cata>/<imgName>')
def imgViewer(cata, imgName):
	return static_file(imgName, root='./'+cata)

@route('/favicon.ico')
def icon():
	return static_file('favicon.ico', root='./')

@route('/<fname>')
def default(fname):
	# name, ext = os.path.splitext(fname)
	# if ext not in ['.jpg', '.JPG', '.png', '.PNG', '.jpeg', '.gif', '.GIF']:
	print(fname)
	with open(fname, 'rb') as o:
		return o.read()


if __name__ == '__main__':
	currentFileLst = fileLst2JSON()
	monkey.patch_all()
	run(host='0.0.0.0', port=8005, debug=True, server='gevent')
