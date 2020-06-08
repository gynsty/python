
import argparse
parser = argparse.ArgumentParser("POM dependencies checker and downloader")
parser.add_argument('-v', '--verbose',help="be verbose", action="store_true", dest="v", default=False)
parser.add_argument('-c', '--check',help="only check for dependencies", action="store_true", dest="c", default=False)
parser.add_argument('-nd','--nd', help="do not download dependencies", action="store_true", dest="nd", default=False)
parser.add_argument('-l', help="action logfile", action="store", dest="l")
args = parser.parse_args()

verbose = False
check = False
download = False
logfile = ""
message = 'this is test'

if args.v:
 verbose = True

if args.nd:
 download = True

if args.c:
 check = True

if args.l:
 logfile = args.l

 with open(logfile,'a') as logf:
  logf.write(message)
 

# debug
print(args)

if args.l:
 logf.close()


