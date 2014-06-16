#! /usr/bin/python

import sys, os, os.path
from avr_snd import *

SEGMENT_MAX = 256
SEGMENT_TMP = """
#define %s%d_len %d
const unsigned char %s%d[] PROGMEM=%s;

"""

PLAY_TMP = """
void play_%s() {
%s
}
"""

def convert(prefix, file_i, file_o):
    a=array.array('B', (open(file_i, 'r').read()))
    i,j=analyze(a)
    b=array.array('B', compress(a,i,j)).tostring()
    print "size=", len(b)
    out=open(file_o, "w+")
    for l, i in enumerate(range(0, len(b), SEGMENT_MAX)):
        segment=b[i:i+SEGMENT_MAX]
        out.write( SEGMENT_TMP % (prefix, l, len(segment), prefix, l, repr(segment).replace("'", '"')))
    out.write(PLAY_TMP % (prefix, "\n".join(map(lambda i: "avr_sound_play(%s%d, %s%d_len);" % (prefix, i, prefix, i), range(l+1)))))
    out.close();

def main():
  file_i=sys.argv[1]
  prefix='.'.join(os.path.basename(file_i).split('.')[:1])
  file_o=os.path.join(os.path.dirname(file_i), prefix+".h")
  convert(prefix, file_i, file_o)

if __name__ == "__main__":
    main()
