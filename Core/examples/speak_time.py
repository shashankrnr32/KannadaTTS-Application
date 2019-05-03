#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Description : Speak current time in Kannada using Kannada Speech Synthesis Project
# Developer : Shashank Sharma
# =============================================================================

import os, datetime

import util

# Set Working directory to this file's directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

util.setEnv()
now = datetime.datetime.now()

# Convert Military time to normal time
hour = now.hour
if now.hour > 12:
    hour = hour%12

# Get Kannada Transcripts
hour = util.number2kn(hour)
minute = util.number2kn(now.minute)

if now.minute == 0 :
    speech = 'ಈಗ ಸಮಯ {} ಘಂಟೆ'.format(hour)
else :
    speech = 'ಈಗ ಸಮಯ {} ಘಂಟೆ {} ನಿಮಿಷ'.format(hour, minute)

wavenum =  util.setup_synthesis(speech)
util.synthesize()
util.run_dsp(wavenum)
util.play_audio(wavenum)
util.garbage_collect()

