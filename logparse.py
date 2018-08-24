import argparse
import time
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-l','--logfiles', nargs='+', help='Test Log Files', required=True)
args = parser.parse_args()

print " "*38 ,
print "\t 1 H",
print "\t 2 H",
print "\t 1 L",
print "\t 2 L",
print "\t bot"
for f in args.logfiles:
  record = open(f)
  print format(f,">38s")+"\t" ,
  try:
    T = record.read().split("\n")
    Lt1r = T[-5]
    Lt2r = T[-4]
    Ht1r = T[-3]
    Ht2r = T[-2]
    arm = T[-1]
    
    print Lt1r[11:16]+"\t" ,
    print Lt2r[11:16]+"\t"  ,
    print Ht1r[11:16]+"\t"  ,
    print Ht2r[11:16]+"\t"  ,
    print arm[0:16]+"\t" ,
    
  except:
    pass
  print
