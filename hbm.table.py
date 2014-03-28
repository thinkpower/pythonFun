#! python
#coding:utf-8
import sys
import os
import shutil
import xml.dom.minidom as xml


dir='E:/ikang/dev_ba_FDI/src/com/ikang/ba/pojo'

resultFile = 'schema.table.txt'

flist = list()


def getXml(dir):
	list = os.listdir(dir)
	for f in list:
		path = dir+'/'+f
		#print('�ļ����ƣ�%s' %(path))
		isdir = os.path.isdir(path)
		if isdir :
			print('�ļ����ƣ�%s' %(f))
			print('�Ƿ���Ŀ¼��%s' %(isdir))
			getXml(path)
		else:
			p,ext = os.path.splitext(path)
			if ext=='.xml':
				print(path)
				flist.append(path)
				
				
getXml(dir)


rfile = open(resultFile,'w')
for f in flist:
		print('������'+f)
		doc = xml.parse(f)
		clazz = doc.getElementsByTagName('class')[0]
		table = clazz.getAttribute('table')
		schema = 'ba'
		if clazz.hasAttribute('schema'):
			schema = clazz.getAttribute('schema').lower()
		rfile.write(schema+'.'+table+'\n')
		print(schema+'.'+table)

rfile.close()
	