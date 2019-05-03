#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Description : Speak current weather in Kannada using Kannada Speech Synthesis Project
# Developer : Shashank Sharma
# =============================================================================

import os
import util
import requests
os.chdir(os.path.dirname(os.path.realpath(__file__)))

util.setEnv()

api_key = '401d1b66fcf98e6b84be4bf599b4b7c0'

# Location ID for Bangalore
location_id = 1277333

# API URL
url = "https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(location_id, api_key)

# Get Data from API and parse data
raw_data = requests.get(url)
data = raw_data.json()

temp = str(data['main']['temp']).split('.')

temp_int = util.number2kn(int(temp[0]))
temp[1] = str(int(temp[1])*100)
temp_dec1 = util.number2kn(int(temp[1][0]))
temp_dec2 = util.number2kn(int(temp[1][1]))

speech = 'ಈಗ ಬೆಂಗಳೂರಿನಲ್ಲಿ ತಾಪಮಾನ {} ಪಾಯಿಂಟ್ {} {} ಸೆಲ್ ಶಿಯಸ್'.format(temp_int,temp_dec1,temp_dec2)

wavenum = util.setup_synthesis(speech)
util.synthesize()
util.run_dsp(wavenum)
util.play_audio(wavenum)
util.garbage_collect()