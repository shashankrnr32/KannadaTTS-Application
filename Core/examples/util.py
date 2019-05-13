#!/usr/bin/env python3

#Utilities Code
# Developer : Shashank Sharma

import os, time, shutil
from pydub import AudioSegment
from pydub.playback import play

def setEnv():
    # =========================================================================
    # Set Environment Variables of EST, Festvox, SPTK, Project and App
    # Change Paths as needed
    # =========================================================================
    
    #Get the current Username
    user = os.environ['USER']
    
    #Project Directory
    project_directory = '/home/{}/Project'.format(user)
    
    #Set Environment Variables for EST, FESTVOX and SPTK
    os.environ['ESTDIR'] = '{}/Main/speech_tools'.format(project_directory)
    os.environ['FESTVOXDIR'] = '{}/Main/festvox'.format(project_directory)
    os.environ['SPTKDIR'] = '{}/Main/sptk'.format(project_directory)
    
    #Set Path for Trained Model [MANUAL]
    os.environ['PRODIR'] = '/home/{}/Project/Main/cmu_indic_kan_female'.format(user)
    os.environ['WAVDIR'] = '{}/test/tts'.format(os.environ['PRODIR'])


#Copy this dict and the function `number2kn` to convert any number below 100 to Kannada Word
# Developer : Shashank Sharma
number_dict = {0 : 'ಸೊನ್ನೆ', 1 : 'ಒಂದು', 2 : 'ಎರಡು', 3: 'ಮೂರು',
               4 : 'ನಾಲ್ಕು', 5 : 'ಐದು', 6 : 'ಆರು',
               7 : 'ಏಳು', 8 : 'ಎಂಟು', 9 : 'ಒಂಬತ್ತು' , 10 : 'ಹತ್ತು', 
               11 : 'ಹನ್ನೊಂದು', 12 : 'ಹನ್ನೆರಡು', 13 : 'ಹದಿಮೂರು', 14 : 'ಹದಿನಾಲ್ಕು', 15 : 'ಹದಿನೈದು',
               16 : 'ಹದಿನಾರು', 17 : 'ಹದಿನೇಳು', 18 : 'ಹದಿನೆಂಟು', 19 : 'ಹತ್ತೊಂಬತ್ತು', 20 : 'ಇಪ್ಪತ್ತು',
               22 : 'ಇಪ್ಪತ್ತ್ ಎರಡು', 30 : 'ಮೂವತ್ತು' , 33 : 'ಮೂವತ್ತ್ ಮೂರು' , 40 : 'ನಲವತ್ತು' , 44 : 'ನಲವತ್ತ್ ನಾಲ್ಕು',
               50 : 'ಐವತ್ತು', 55 : 'ಐವತ್ತ್ ಐದು', 60 : 'ಅರವತ್ತು', 66 : 'ಅರವತ್ತ್ ಆರು' , 70 : 'ಎಪ್ಪತ್ತು', 77 : 'ಎಪ್ಪತ್ತ್ ಏಳು',
               80 : 'ಎಂಬತ್ತು', 88 : 'ಎಂಬತ್ತ್ ಎಂಟು', 90 : 'ತೊಂಬತ್ತು', 99 : 'ತೊಂಬತ್ತ್ ಒಂಬತ್ತು'  }
def number2kn(num):
    if num < 100:
        try : 
            return number_dict[num]
        except :
            tens_place = number_dict[int(str(num)[0]*2)].split()[0]
            units_place = number_dict[int(str(num)[1])]
            return tens_place + ' ' + units_place

           
def setup_synthesis(txt):
    wavenum = str(time.strftime("%Y%m%d_%H%M%S"))

    with open(os.environ['PRODIR']+'/etc/temp.txt', 'w') as temp_file:
                        temp_file.write('( kan_{} \" {} \")'.format(wavenum,txt))
    return wavenum


def play_audio(wavenum):
    try:
        song = AudioSegment.from_wav('{}/kan_{}_dsp.wav'.format(os.environ['WAVDIR'], wavenum))
    except:
        song = AudioSegment.from_wav('{}/kan_{}.wav'.format(os.environ['WAVDIR'], wavenum))  
    play(song)

    
def synthesize():
    os.system('./festivalrun.sh')

def run_dsp(wavenum):
    os.system('soundstretch $WAVDIR/kan_{0}.wav $WAVDIR/kan_{0}_dsp.wav -pitch=+1.5 > logfile 2>&1'.format(wavenum))
    
def garbage_collect():
    try:
        os.remove('logfile')
    finally:
        for file in os.listdir(os.environ['WAVDIR']):
            os.remove(os.path.join(os.environ['WAVDIR'], file))
        shutil.rmtree('./__pycache__',ignore_errors=True)