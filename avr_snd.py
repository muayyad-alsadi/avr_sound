#! /usr/bin/python

import array
import sys, os, os.path

from collections import defaultdict

def get_values(value0, value3):
    l = (value3-value0)/3.0
    value1 = int(value0 + l)
    value2 = int(value0 + 2.0*l)
    return (value0, value1, value2, value3)

def error_sum(histo, values):
    # l = (values[1]-values[0])/2.0
    limit0, limit1, limit2 = [ (values[0]+values[1])/2, (values[1]+values[2])/2, (values[2]+values[3])/2 ]
    e=0
    for i in range(256):
        if i>limit2: b = 3
        elif i>limit1: b = 2
        elif i>limit0: b = 1
        else: b=0
        e+=abs(i-values[b])*histo[i]
    return e


def analyze(a):
    """find best linear range"""
    count=len(a)
    histo = defaultdict(int)
    for i in a: histo[i]+=1
    i,i0,j,j0 = 0,0,255,255
    more = True
    e0 = 256 * count
    for i in range(250):
        values = get_values(i, j)
        e = error_sum(histo, values)
        if e<=e0: i0=i; e0=e
    i=i0
    for j in range(255, i+5, -1):
        values = get_values(i, j)
        e = error_sum(histo, values)
        if e<=e0: j0=j; e0=e
    j=j0
    values = get_values(i, j)
    print i,j, "=>", values
    return i,j

def compress(a, i=0, j=255):
  values = get_values(i, j)
  limit0, limit1, limit2 = [ (values[0]+values[1])/2, (values[1]+values[2])/2, (values[2]+values[3])/2 ]
  round_off=0
  current_byte=0
  j=0
  for v in a:
     v=min(255, max(0, round_off+v))
     if v>limit2: o = 3
     elif v>limit1: o = 2
     elif v>limit0: o = 1
     else: o=0
     current_byte|=o<<(2*j)
     # comment out next line to disable round_off
     # round_off=(v-values[o])/8.0 # faded round off
     j+=1
     if j == 4: yield current_byte; current_byte=0; j=0
  if j != 0:
      yield current_byte

def decompress_mapper(a):
   for v in a:
      yield v & 3
      v>>=2
      yield v & 3
      v>>=2
      yield v & 3
      v>>=2
      yield v & 3

def decompress(a,i,j):
  values = get_values(i, j)
  for v in decompress_mapper(a):
     yield values[v]

def test(prefix, file_i, file_o):
    a=array.array('B', (open(file_i, 'r').read()))
    i,j=analyze(a)
    b=compress(a,i,j)
    c=array.array('B', decompress(b,i,j)).tostring()
    out=open(file_o, 'wb+')
    out.write(c)
    out.close()
    os.system("pacat --channels=1 --rate=8000 --format=u8 "+file_o)
    


if __name__ == "__main__":
    main()
