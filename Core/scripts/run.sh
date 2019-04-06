#!/bin/sh
# ===========================================================
# Set Environment Variables
# Dev : Shashank Sharma
# ===========================================================

echo Setting Environment Variables...

cwd=$(pwd)
export ESTDIR="$cwd/speech_tools"
export FESTVOXDIR="$cwd/festvox"
export SPTKDIR="$cwd/sptk"
export VOICEDIR="$cwd/cmu_indic_kan_female"
export WAVDIR="$VOICEDIR/test/tts"

echo Changing to Voice Directory...
cd $VOICEDIR

if [ $# -eq 0 ];
then
	echo Using Default Test File...
	$1=etc/txt.done.data.test
fi

echo Checking \for Test File...
if [ -f $1 ];
then
	echo Test File Found...
	echo Synthesing...
	./bin/do_clustergen cg_test tts tts $1 > kss.log 2>&1
fi

echo "Successfully Synthesized. 
Check the Audio Files in $WAVDIR"


