
#! /usr/bin/python

import sys

import shutil


if len(sys.argv) != 4:
	print "param err"
	sys.exit()

srcfile = str(sys.argv[1])
firstid = int(sys.argv[2])
lastid  = int(sys.argv[3])
print "------------------------"
print srcfile ,firstid,lastid
print "------------------------"

idx1 = str.rfind(srcfile,'_')
idx2 = str.rfind(srcfile,".")
chgid = srcfile[idx1+1:idx2]
print idx1 , idx2, chgid
print type(chgid), type(idx1)

for name in range (firstid , lastid+1):
	#print type(name)
	newname = srcfile.replace(chgid , str(name))
	#print name , newname
	shutil.copy(srcfile , newname)



