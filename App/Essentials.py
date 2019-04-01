# -*- coding: utf-8 -*-

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

import json
import os
from scipy.io import wavfile as wav
#TRANSLATE
from google.cloud import translate
#MAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
#DATABASE
import sqlite3

# =============================================================================
#Developer : Shashank Sharma
#Description : 
#     Google Translate API Implementation
#     Needs an Internet Connection
# =============================================================================
def en2kn(text):
    #Path to Private Key
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/res/GCredentials.json'
    
    client = translate.Client()
    res = client.translate(text, source_language='en',target_language = 'kn')
    return res['translatedText']


# =============================================================================
#Developer : Shashank Sharma
#Description : 
#     Send Mails (Audio File)
# =============================================================================
def send_mail(to_address, entry):
    # =========================================================================
    # Sends Mail with audio file attached
    # =========================================================================
    
    #Get Credentials from JSON File
    with open('res/MailCredentials.json') as json_file:
        credentials = json.load(json_file)
        
    username = credentials['username']
    password = credentials['password']
    
    #Determine the Server
    hosts = {
            'yahoo.com' : 'smtp.mail.yahoo.com',
            'gmail.com' : 'smtp.gmail.com',
            'outlook.com' : 'smtp-mail.outlook.com',
            }
    
    for x in hosts:
        if x in username:
            host = hosts[x]

    #HTML Message
    mail_text = '''
    Hey There,<br>
    Thank you for using Kannada Speech Synthesis GUI Application. We have attached the audio file in this mail (.wav)  <br><br>
    <b>File Name</b> : {0}                  <br>
    <b>Kannada Transcript</b> : {1}         <br>
    <b>Processed</b> : {2}
    <p>You are allowed to use the audio for any purpose, with certain conditions of the application specified by FSF's GPL v3.0.</p>
    <p>Check out the Project <a href="https://github.com/shashankrnr32/KannadaTTS_APP">here</a>  </p>
    <a href="https://www.linkedin.com/in/shashank-sharma-932701108/">Shashank Sharma</a><br>
    Project Developer<br>
    RIT-Bangalore<br>
    '''
    
    #Subject of Mail
    subject = 'Kannada Speech Synthesis'
    
    try:
        #Connect to Server
        server = smtplib.SMTP(host,587)
        
        #Generate Message
        mail = MIMEMultipart()
  
        #Add headers
        mail['Subject'] = subject
        mail['From'] = username
        mail['To'] = to_address
        
        #Add Message
        msg_text = mail_text.format('kan_'+entry[1]+'.wav', entry[2], bool(entry[3]))
        msg_text = MIMEText(msg_text.encode('utf-8'), 'html',  _charset='utf-8')
        mail.attach(msg_text)
        
        #Check for DSP
        if bool(entry[3]):
            wav_file = os.environ['WAVDIR'] + '/DSP/kan_' + entry[1] + '.wav'
        else:
            wav_file = os.environ['WAVDIR'] +'/NoDSP/kan_'+entry[1]+'.wav'
        
        #Read Audio to attach
        with open(wav_file,'rb') as audio_file:
            audio = MIMEAudio(audio_file.read())
        audio.add_header('Content-Disposition', 'attachment', filename= 'kan_' + entry[1] + '.wav')
        mail.attach(audio)
        
        #Ping
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        #Login to Server
        server.login(username,password)
        
        #Send Mail
        server.sendmail(username, to_address, mail.as_string())
        
        #Quit Server
        server.quit()    
        
        #Successfully sent
        return True
    
    except Exception as e :
        print(e.with_traceback())
        # Any Error
        return False
    
# =============================================================================
#Developer : Shashank Sharma(shashankrnr32@gmail.com)
#Description : 
#       Database Implementation for Application. Uses SQLite       
# =============================================================================

class Database:
    
    def __init__(self,database = 'res/DB'):
        
        self.wav_path = os.environ['WAVDIR']
        
        #Establish Connection to DB
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
    
    def search_duplicate(self,txt):
        return list(self.cursor.execute('SELECT wav_id FROM kan WHERE txt=?',(txt,)))
    
    def get_entry(self,wid):
        # =====================================================================
        # Retrieves the entry with id =`wid`
        # =====================================================================
        entry = self.cursor.execute('SELECT * FROM kan WHERE wav_id=?',(wid,))
        return list(entry)
    
    
    def get_last_entry(self):
        #======================================================================
        #Retrieves The Last Entry of the Database
        #======================================================================
        entry = self.cursor.execute('SELECT * FROM kan WHERE id = (SELECT MAX(id) FROM kan);')
        return list(entry)
    
    def get_next_entry(self,wid):
        #======================================================================
        #Retrieves The Next Entry of the Database (wid)
        #======================================================================
        entry = self.cursor.execute('SELECT * FROM kan WHERE id = (SELECT MIN(id) FROM kan WHERE id>?);',(wid,))
        return list(entry)
            
    def get_prev_entry(self,wid):
        #======================================================================
        #Retrieves The Previous Entry of the Database (wid)
        #======================================================================
        entry = self.cursor.execute('SELECT * FROM kan WHERE id = (SELECT MAX(id) FROM kan WHERE id<?);',(wid,))      
        return list(entry)
    
    def get_all_entries_for_table(self):
        #======================================================================
        #Retrieves All Entries for Table View
        #======================================================================
        return self.cursor.execute('SELECT id,wav_id,txt,dsp,rating FROM kan ORDER BY id DESC;')

    def update_rating(self,wid,val):
        self.cursor.execute('UPDATE kan SET rating=? WHERE id=?',(val,wid))
        self.conn.commit()
    
    def add_entry(self,kan_txt, wav_id, dsp = True, reverse_id = -1):
        #======================================================================
        #Adds an entry to the database
        #======================================================================
        
        #Read File and determine Duration of the Wave File
        if dsp:
            fs,samples = wav.read('{}/DSP/kan_{}.wav'.format(self.wav_path,wav_id))
        else:
            fs,samples = wav.read('{}/NoDSP/kan_{}.wav'.format(self.wav_path,wav_id))
        
        #Duration in seconds
        dur = len(samples)/fs
        
        #Insert into Database
        self.cursor.execute('INSERT INTO kan(wav_id,txt,dsp,duration,reverse_id) VALUES (?,?,?,?,?)', (wav_id, kan_txt, int(dsp), dur, reverse_id))
        
        #Add Reverse ID to the reverse entry
        if reverse_id != -1:
            self.cursor.execute('UPDATE kan SET reverse_id = ? WHERE wav_id = ?;',(wav_id, reverse_id))
        
        #Commit Changes
        self.conn.commit()

class TranslateDatabase:
    def __init__(self,database = 'res/DB'):
        
        #Establish Connection to DB
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
    
    def add_new_translation(self,en_text,kan_text):
        # =====================================================================
        # Add New Translation Entry to Database
        # =====================================================================
        
        #Adds New Entry
        self.cursor.execute('INSERT INTO en2kan(en_text,kan_text) VALUES (?,?);',(en_text, kan_text))      
        
        #Commit Changes
        self.conn.commit()
    
    def get_all_entries_for_table(self):
        #======================================================================
        #Retrieves All Entries for Table View
        #======================================================================
        return self.cursor.execute('SELECT id,en_text,kan_text FROM en2kan ORDER BY id DESC;')


