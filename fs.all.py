#!/usr/bin/python3 

import os
import shutil
import glob

# get cwd:
print("CWD is:"+os.getcwd())

# change cwd 
os.chdir('/tmp')

# verify change
print("CWD is:"+os.getcwd())

# get current file name:
print(__file__)

print(os.getcwd())

dirname = 'testik'
filename = 'testikovy.txt'

if not os.path.isdir(dirname):
 os.mkdir(dirname)
 os.mkdir(dirname+"/"+"testikovy2")
 print('Directory created')
 os.chdir(dirname)
 print("CWD is:"+os.getcwd())
 os.mknod(filename)
 os.mknod("test1.txt")
 os.mknod("test3.txt")
 if os.path.exists(filename):
  print("File created")
  os.remove(filename)
  os.chdir('/tmp/')
  os.rmdir(dirname)
 else:
  print('File was not created!')

# creating multiple directories

if not os.path.isdir('/tmp/a/'):
 os.makedirs('/tmp/a/b/c/d')
 os.mknod('/tmp/a/test1.txt')
 os.mknod('/tmp/a/b/test2.txt')

#if os.path.exists(filename):
# if os.path.isdir('/tmp/testik'):

# find recursively files

for f in glob.iglob("/tmp/a/*.txt", recursive=True):
    print("found file:"+f)

# recursively remove directories and its content
# shutil.rmtree('/tmp/a')

