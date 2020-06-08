
import glob,os

#for f in glob.glob('/tmp/a/*.txt',recursive=False):
# print(f)

results= []

for x in os.walk('/tmp/a/'):
 # this will create [] with all files and directories inside
 for y in glob.glob(os.path.join(x[0],'*.txt')):
 # go through all content and just get first level directory + '.txt' files
  print(y)

