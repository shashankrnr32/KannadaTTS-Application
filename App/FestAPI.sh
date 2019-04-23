#!/bin/sh

# =============================================================================
# Copyright (C) 2019 Shashank Sharma
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>
# =============================================================================


# =============================================================================
#Developer : 
#
#	Primary Code : Varun S S(varunsridhar614@gmail.com)
#	Production Code , Resampling Analysis : Shashank Sharma(shashankrnr32@gmail.com)
#	Sox Integration : Srinivas N M(srinivasnm471@gmail.com)
#Description : 
#
#	Shell API to call Festvox Project.
#	Appropriate Permissions to be given before Building Project.
#	This Shell Script is called by synthesize() method of Main.py
#
# =============================================================================

#touch $PRODIR/etc/temp.txt
mkdir -p $APP/ignore

#Run TTS from Festvox Project
cd $PRODIR

if [ $1 = "-lab" ]
then
	mkdir -p prompt-lab
	mkdir -p prompt-utt
	./bin/do_build build_prompts etc/temp.txt > $APP/ignore/temp.txt 2>&1
	mv prompt-lab/kan_$2.lab $APP/ignore/kan_$2.lab
	mv prompt-utt/kan_$2.utt $APP/ignore/kan_$2.utt
	rmdir --ignore-fail-on-non-empty -p prompt-lab prompt-utt
	exit

else
	./bin/do_clustergen cg_test tts tts etc/temp.txt > $APP/ignore/temp.txt 2>&1
	rm etc/temp.txt
	mv $PRODIR/test/tts/kan_$2.wav $WAVDIR/NoDSP/kan_$2.wav

	#DSP -Digital Signal Processing Operations

	#==============================================================================
	#Pitch Shift using soundstretch
	#http://www.surina.net/soundtouch/

	b="$1"
	a="1"
	if [ "$b" -eq "$a" ]
	then
		soundstretch $WAVDIR/NoDSP/kan_$2.wav $WAVDIR/DSP/kan_$2.wav -pitch=+2.25 -tempo=-5 > $APP/ignore/temp.txt 2>&1
		
		#==============================================================================
		#Noise Removal using SOX
		#https://en.wikipedia.org/wiki/SoX
		sox $WAVDIR/DSP/kan_$2.wav $WAVDIR/DSP/noise-audio.wav trim 0 00:0.1 > $APP/ignore/temp.txt 2>&1
		sox $WAVDIR/DSP/noise-audio.wav -n noiseprof $WAVDIR/DSP/noise.prof > $APP/ignore/temp.txt 2>&1
		mv $WAVDIR/DSP/kan_$2.wav $WAVDIR/DSP/kan_$2_temp.wav 
		sox $WAVDIR/DSP/kan_$2_temp.wav $WAVDIR/DSP/kan_$2.wav noisered $WAVDIR/DSP/noise.prof 0.21 > $APP/ignore/temp.txt 2>&1

		#Resampling if decided to add		

		rm $WAVDIR/DSP/kan_$2_temp.wav
		rm $WAVDIR/DSP/noise-audio.wav
		rm $WAVDIR/DSP/noise.prof
		#==============================================================================
	fi
	#==============================================================================
fi
