#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Description : Speak a small poem/song in Kannada using Kannada Speech Synthesis Project
# Developer : Shashank Sharma
# =============================================================================

chutuku = ['ಎಲ್ಲೋ ಮಳೆಯಾಗಿದೆ ಇಂದು',
          'ತಂಗಾಳಿಯು ಬೀಸುತಿದೆ']
import util

import os, time
from pydub import AudioSegment
from pydub.playback import play

print('========================================================')
print('Play small poem demo')
print('Developed by Shashank Sharma')
print('========================================================')
print('''Copyright (C) 2019  Shashank Sharma
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome 
to redistribute it under certain conditions.''')
print('========================================================')

os.chdir(os.path.dirname(os.path.realpath(__file__)))

util.setEnv()

wavenum = list()
temp_file = open(os.environ['PRODIR']+'/etc/temp.txt', 'w')
num_index = 0
for line in chutuku:
    num = str(time.strftime("%Y%m%d_%H%M%S")) + str(num_index)
    num_index+=1
    wavenum.append(num)
    temp_file.write('( kan_{} \" {} \")\n'.format(num,line))

temp_file.close()

os.system('./festivalrun.sh')
for num in wavenum:
    os.system('soundstretch $WAVDIR/kan_{0}.wav $WAVDIR/kan_{0}_dsp.wav -pitch=+2.5 > logfile 2>&1'.format(num))
    
for num in wavenum:
    
    song = AudioSegment.from_wav('{}/kan_{}_dsp.wav'.format(os.environ['WAVDIR'], num))
    play(song)
    os.remove('{}/kan_{}_dsp.wav'.format(os.environ['WAVDIR'], num))
    os.remove('{}/kan_{}.wav'.format(os.environ['WAVDIR'], num))

util.garbage_collect()