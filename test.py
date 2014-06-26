#! /usr/bin/python

import sys, os, os.path
from avr_snd import *

def main():
  file_i=sys.argv[1]
  prefix='.'.join(os.path.basename(file_i).split('.')[:1])
  file_o=os.path.join(os.path.dirname(file_i), prefix+".out")
  test(prefix, file_i, file_o)

main()
