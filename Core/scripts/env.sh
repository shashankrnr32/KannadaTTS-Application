#!/bin/sh
# ===========================================================
# Set Environment Variables
# Dev : Shashank Sharma
# ===========================================================

cwd=$(pwd)
export ESTDIR="$cwd/speech_tools"
export FESTVOXDIR="$cwd/festvox"
export SPTKDIR="$cwd/sptk"
export VOICEDIR="$cwd/cmu_indic_kan_female"
export WAVDIR="$PRODIR/test/tts"

echo "ESTDIR set to $ESTDIR"
echo "FESTVOXDIR set to $FESTVOXDIR"
echo "SPTKDIR set to $SPTKDIR"
echo "PRODIR set to $PRODIR"

#Change Directory to VOICE
cd $VOICEDIR

if [ $# -eq 0 ];
then
	$1=etc/text.done.data.test
fi	

time ./bin/do_clustergen cg_test tts tts $1 > kss.log 2>&1
echo 
"Successfully Synthesized. 
Check the wavfiles in $WAVDIR
Check for logs in $VOICEDIR/kss.log"


