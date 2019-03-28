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


# =============================================================================
#Developer : Shashank Sharma
# 
#Description : 
#     Google Translate API Implementation
#     Needs an Internet Connection
# =============================================================================

from google.cloud import translate
import os

#Path to Private Key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/res/GCredentials.json'

def en2kn(text):
    client = translate.Client()
    res = client.translate(text, source_language='en',target_language = 'kn')
    return res['translatedText']


# =============================================================================
#Developer : 
#       Shashank Sharma(shashankrnr32@gmail.com)
# 
#Description : 
#       Database Implementation for Application. Uses SQLite       
# =============================================================================

import sqlite3
from scipy.io import wavfile as wav

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
