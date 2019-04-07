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
echo Synthesing...
./bin/do_clustergen cg_test tts tts $1 > kss.log 2>&1
echo "Successfully Synthesized. 
Check the Audio Files in $WAVDIR"


