avr-sound
=========

Sound compression and output with bare AVR/Arduino
using two digital pins and R-2R resistor ladder.

Features
--------

 - a script to convert audio file to .h header file
 - the audio file is actually stored in flash memory
 - you can use more than one audio file in one project
 - very compact (2Kb per second)
 



Installation
------------

Put this directory into sketchbook/libraries/ (create it if needed)


Demos
-----

Restart your arduino IDE and open file->examples->avr_sound and pick any of the 3 included samples.

Connect digital pin 8 and digital pin 9 to a resistor ladder then to an earphone.
If you want to use a bigger speaker then you need a transistor.


Usage
-----

convert your audio file into file with the following options:

 - raw file format (headerless, just data)
 - single channel 
 - 8000 Hz sampling rate
 - unsigned 8-bit per sample

you can do that using feesoftware like Audacity by following those steps

 - if you have stereo audio click on the audio track menu (arrow down icon) then split then delete one track then pick mono
 - tracks -> reample -> 8000Hz
 - file -> export -> uncompressed files -> options -> raw, unsigned 8-bit PCM

then run the included python script on the resulting file

