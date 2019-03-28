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
#Developers : 
#       Shashank Sharma(shashankrnr32@gmail.com)
#           - User Interface
#           - Kannada to English Translate
#           - SQLite Database Implementation
#           - Media Player Integration
#           - About Window
#           - Table Window
#           - Plot Window
#       
#       Varun S S(varunsridhar614@gmail.com)
#           - FestAPI.sh
#
#Description : 
#       Main Application Executable
# =============================================================================

#INBUILT
import sys,time,os,shutil
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
import gc
import numpy as np
from scipy import signal
import scipy.io.wavfile as wave
import pysptk.sptk as sptk

#PLOTS
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

#UI
from Application import Ui_MainWindow
from Plot import Ui_PlotDialog
from AboutWindow import Ui_about_dialog
from SynDB import Ui_Dialog as SUi_dialog
from TraDB import Ui_Dialog as TUi_dialog

#SUPPORT BACKEND
import Essentials
from Essentials import Database as sdb
from Essentials import TranslateDatabase as tdb

# =============================================================================
# Thread Implementation for Play Progress Bar 
# =============================================================================

    
class PlayThread(QtCore.QThread):
    
    def __init__(self,seconds,parent = None):
        
        #Call Inherited Constructor
        super(PlayThread,self).__init__(parent)
        self.seconds = seconds/100
    
    def set_seconds(self,seconds):
        # =====================================================================
        # Each percentage of the progress bar occurs for `seconds` sec
        # =====================================================================
        self.seconds = seconds/100
        
    def run(self):
        # =====================================================================
        # Called when the thread is started
        # =====================================================================
        signal = 0
        
        while signal != 100:
            #Thread sleeps for `seconds` sec
            self.msleep(self.seconds*1000)
            
            #Increment in Percentage
            signal += 1
            
            #Emit SIGNAL : bar_percent that is caught by Implementation Window
            self.emit(QtCore.SIGNAL('bar_percent'),signal)
        self.emit(QtCore.SIGNAL('bar_percent'),0)

# =============================================================================
# About Dialog Implementation
# =============================================================================
class AboutDialog(QtGui.QDialog):
    
    def __init__(self, *args, **kwargs):
        
        #Setup About Window UI
        QtGui.QWidget.__init__(self, parent = kwargs.get('parent'))
        self.ui = Ui_about_dialog()
        self.ui.setupUi(self)
        
        
    def set_focus(self, index):
        self.ui.tabWidget.setCurrentIndex(index)   

# =============================================================================
# Synthesis Table Dialog Implementation
# =============================================================================
class SynTableView(QtGui.QDialog):
    
    def __init__(self, *args, **kwargs):
        
        #Setup Table Window UI
        QtGui.QWidget.__init__(self, parent = kwargs.get('parent'))
        self.parent = kwargs.get('parent')
        self.ui = SUi_dialog()
        self.ui.setupUi(self)
        
        #Database Object
        self.db = kwargs.get('parent').syn_db
        
        #Set Column Width
        self.set_column_width()  
        
        #Add Data to Rows
        self.populate_data()
        
        #When an item is double Clicked Change Media Player to that item
        self.ui.tableWidget.itemDoubleClicked.connect(self.item_double_clicked)
        
    def set_column_width(self):
        # =====================================================================
        # Sets Table Column Width
        # =====================================================================
        width = [133,200,500,133,134]
        for column in range(len(width)):
            self.ui.tableWidget.setColumnWidth(column,width[column])
    
    def populate_data(self):
        # =====================================================================
        # Creates Rows and Adds Data from Database
        # =====================================================================
        entries = self.db.get_all_entries_for_table()
        for entry in entries:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setRowHeight(rowPosition,40)
            for column in range(0,5):
                self.ui.tableWidget.setItem(rowPosition,column,QtGui.QTableWidgetItem(str(entry[column])))

    def item_double_clicked(self,item):
        # =====================================================================
        # Update Media Player with the double clicked item
        # =====================================================================
        row = item.row()
        wav_id = self.ui.tableWidget.item(row,1).text()
        self.parent.update_media_player(wav_id)
        self.done(0)


# =============================================================================
# Translation Table Dialog Implementation
# =============================================================================
class TraTableView(QtGui.QDialog):
    
    def __init__(self, *args, **kwargs):
        
        #Setup Table Window UI
        QtGui.QWidget.__init__(self, parent = kwargs.get('parent'))
        self.parent = kwargs.get('parent')
        self.ui = TUi_dialog()
        self.ui.setupUi(self)
        
        #Database Object
        self.db = kwargs.get('parent').tra_db
        
        #Set Column Width
        self.set_column_width()  
        
        #Add Data to Rows
        self.populate_data()
        
        
    def set_column_width(self):
        # =====================================================================
        # Sets Table Column Width
        # =====================================================================
        width = [100,500,500]
        for column in range(len(width)):
            self.ui.tableWidget.setColumnWidth(column,width[column])
    
    def populate_data(self):
        # =====================================================================
        # Creates Rows and Adds Data from Database
        # =====================================================================
        entries = self.db.get_all_entries_for_table()
        for entry in entries:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setRowHeight(rowPosition,40)
            for column in range(0,3):
                self.ui.tableWidget.setItem(rowPosition,column,QtGui.QTableWidgetItem(str(entry[column])))
       
        
# =============================================================================
# Plot Dialog Implementation
# =============================================================================
class PlotView(QtGui.QDialog):
    
    def __init__(self, *args, **kwargs):
        
        #Setup Plot Window UI
        QtGui.QWidget.__init__(self, parent = kwargs.get('parent'))
        self.ui = Ui_PlotDialog()
        self.ui.setupUi(self)
        
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        
        self.entry = kwargs.get('parent').entry
        
        if bool(self.entry[3]):
            (self.fs,self.samples) = wave.read('{}/DSP/kan_{}.wav'.format(os.environ['WAVDIR'],self.entry[1]))
        else:
            (self.fs,self.samples) = wave.read('{}/NoDSP/kan_{}.wav'.format(os.environ['WAVDIR'],self.entry[1]))
        
        #Memory Management
        gc.collect()
        
    def tab_changed(self,index):
        # =====================================================================
        # Runs Everytime Tab is changed
        # =====================================================================
        
        #Delete Items in Tab1
        for i in reversed(range(self.ui.plot0.count())): 
            self.ui.plot0.itemAt(i).widget().setParent(None)
        
        #Delete Items in Tab2
        for i in reversed(range(self.ui.plot1.count())): 
            self.ui.plot1.itemAt(i).widget().setParent(None)
        
        #Delete Items in Tab3
        for i in reversed(range(self.ui.plot2.count())): 
            self.ui.plot2.itemAt(i).widget().setParent(None)
        
        #Delete Items in Tab3
        for i in reversed(range(self.ui.plot3.count())): 
            self.ui.plot3.itemAt(i).widget().setParent(None)
        
        #Memory Management
        gc.collect()
        
        if index == 0:
            self.plot_wave()
        if index == 1:
            self.plot_spectrum()
        if index == 2:
            self.plot_pitch()
        if index == 3:
            self.plot_specgram()
        if index == 4:
            self.plot_label()
    
    def set_focus(self,index):
        # =====================================================================
        # Sets Tab Focus based on Button
        # =====================================================================
        self.ui.tabWidget.setCurrentIndex(index)
        self.tab_changed(index)
    
    def plot_wave(self):
        # =====================================================================
        # Plot Waveform
        # =====================================================================
        
        #Add Canvas Widget to Layout
        figure = Figure()
        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self.ui.tabWidget)
        self.ui.plot0.addWidget(canvas)
        self.ui.plot0.addWidget(toolbar)

        #Create axis and clear Previous figure
        ax = figure.add_subplot(111)
        ax.clear()
        ax.grid(linestyle = '--')

        y_axis = self.samples/max(self.samples)
        x_axis = np.arange(0,len(y_axis)/self.fs,1/self.fs)
        
        #Plot x vs y
        ax.plot(x_axis, y_axis)
        
        ax.set_title('Waveform {}'.format(self.entry[1]), fontfamily = 'Manjari')
        
        ax.set_xlabel('Time (s)', fontfamily = 'Manjari')
        ax.set_ylabel('Normalized Amplitude (V)', fontfamily = 'Manjari')
        
        #Show Canvas
        canvas.draw()
        
        #Memory Management
        del canvas, ax, figure, toolbar, y_axis, x_axis
        gc.collect()
        
    def plot_spectrum(self):
        # =====================================================================
        # Plot Magnitude Spectrum
        # =====================================================================
        
        #Add Canvas Widget to Layout
        figure = Figure()
        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self.ui.tabWidget)
        self.ui.plot1.addWidget(canvas)
        self.ui.plot1.addWidget(toolbar)
        
        #Create axis and clear Previous figure
        ax = figure.add_subplot(111)
        ax.clear()
        ax.grid(linestyle = '--')

        signal = self.samples/max(self.samples) 
        spectrum, freqs, line = ax.magnitude_spectrum(signal, Fs = self.fs, scale = 'dB')
        
        #Particularly for Axis configuration
        spectrum_db = 20*np.log10(spectrum)
        ax.set_ylim([max(min(spectrum_db)-5,-100),max(spectrum_db)+5])
        
        # Audacity Style Plot
        ax.fill_between(freqs,spectrum_db,-110)

        ax.set_title('Magnitude Spectrum {}'.format(self.entry[1]), fontfamily = 'Manjari')
        ax.set_xlabel('Frequency (Hz)', fontfamily = 'Manjari')
        ax.set_ylabel('Magnitude (dB)', fontfamily = 'Manjari')
        
        #Show Canvas
        canvas.draw()
        
        #Memory Management
        del canvas, ax, figure, toolbar,signal, spectrum, spectrum_db
        gc.collect()
        
    def plot_pitch(self):
        # =====================================================================
        # Plot Pitch Contour
        # =====================================================================
        
        #Add Canvas Widget to Layout
        figure = Figure()
        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self.ui.tabWidget)
        self.ui.plot2.addWidget(canvas)
        self.ui.plot2.addWidget(toolbar)
        
        #Create axis and clear Previous figure
        ax = figure.add_subplot(111)
        ax.clear()
        ax.grid(linestyle = '--')
        
        
        sig = self.samples.astype('float32')
        y_axis = sptk.rapt(sig,self.fs,250,float(120),float(400))
        x_axis = np.linspace(0,len(sig)/self.fs,len(y_axis))
        
        ax.plot(x_axis,y_axis)
        ax.set_ylim([120,400])
        ax.set_title('Pitch Contour {}'.format(self.entry[1]), fontfamily = 'Manjari')
        ax.set_xlabel('Time (s)', fontfamily = 'Manjari')
        ax.set_ylabel('Pitch (Hz)', fontfamily = 'Manjari')
        
        #Show Canvas
        canvas.draw()
        
        #Memory Management
        del canvas, ax, figure, toolbar,sig, y_axis, x_axis
        gc.collect()
    
    def plot_specgram(self):
        # =====================================================================
        # Plot Spectrogram
        # =====================================================================
        
        #Add Canvas Widget to Layout
        figure = Figure()
        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self.ui.tabWidget)
        self.ui.plot3.addWidget(canvas)
        self.ui.plot3.addWidget(toolbar)
        
        #Create axis and clear Previous figure
        ax = figure.add_subplot(111)
        ax.clear()
        ax.grid(linestyle = '--')
    
        #x_axis = np.arange(0,len(self.samples)/self.fs,1/self.fs)
        f, t, spectrogram = signal.spectrogram(self.samples,self.fs, window = signal.get_window('hamming',256), noverlap = 128)
        
        ax.pcolormesh(t, f, spectrogram, cmap = 'magma')
        ax.set_title('Pitch Contour {}'.format(self.entry[1]), fontfamily = 'Manjari')
        ax.set_ylabel('Frequency (Hz)', fontfamily = 'Manjari')
        ax.set_xlabel('Time (s)', fontfamily = 'Manjari')
        ax.set_yscale('symlog')
        
        #Show Canvas
        canvas.draw()
        
        #Memory Management
        del canvas, ax, figure, toolbar, f, t, spectrogram
        gc.collect()
     
    def plot_label(self):
        pass
#==============================================================================
class MyApp(QtGui.QMainWindow):

    def __init__(self, *args, **kwargs):
        QtGui.QMainWindow.__init__(self, parent = None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Application Object
        self.app = kwargs.get('app')

        #Connect to Synthesis Database
        self.syn_db = sdb()
        
        #Connect to Translation Database
        self.tra_db = tdb()
        
        #Configure Buttons
        self.button_config()
        
        #Configure Actions of UI
        self.action_config()
        
        #Configure Audio
        self.audio_config()
        
        #Configure Status Bar
        self.statusBar = QtGui.QStatusBar()
        self.setStatusBar(self.statusBar)
        
        #Disable Maximize Button
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    

    def contextMenuEvent(self, event):
        # =====================================================================
        # Right Click Menu For Application
        # =====================================================================
        
        #Create a Menu
        menu = QtGui.QMenu(self)
        
        #Create Actions
        tableAction = menu.addAction("View All Synthesis")
        aboutAction = menu.addAction("About Project")
        
        minimizeAction = menu.addAction("Minimize")
        quitAction = menu.addAction("Quit")
        
        #Get the action that is clicked
        action = menu.exec_(self.mapToGlobal(event.pos()))
       
        #Handle the Click Action
        if action ==aboutAction:
            self.about(0)
        if action == tableAction:
            self.showTable()
        if action == minimizeAction:
            self.showMinimized()
        if action == quitAction:
            self.close()
        
    def action_config(self):
        # =====================================================================
        # Configure Actions
        # =====================================================================
        
        #About Window
        self.ui.actionAbout_Project.triggered.connect(lambda: self.about(0))
        self.ui.actionDevelopers.triggered.connect(lambda: self.about(1))
        self.ui.actionMentor.triggered.connect(lambda: self.about(2))
        self.ui.actionLicense.triggered.connect(lambda: self.about(3))
        
        #Table Window
        self.ui.actionSynthesized_Text.triggered.connect(lambda: self.show_table(1))
        self.ui.actionTranslations_Text.triggered.connect(lambda: self.show_table(-1))

        #Theme Selector
        self.ui.actionGTK.triggered.connect(lambda: self.theme_select('GTK+'))
        self.ui.actionWindows.triggered.connect(lambda: self.theme_select('Windows'))
        self.ui.actionPlastique.triggered.connect(lambda: self.theme_select('Plastique'))
        self.ui.actionMotif.triggered.connect(lambda: self.theme_select('Motif'))
        self.ui.actionCleanlooks.triggered.connect(lambda: self.theme_select('Cleanlooks'))
        self.ui.actionCDE.triggered.connect(lambda: self.theme_select('CDE'))
      
    def button_config(self):
        # =====================================================================
        # Configure Buttons
        # =====================================================================
        
        #Synthesize Button Action
        self.ui.syn_button.pressed.connect(self.synthesize)
        self.ui.syn_button.setEnabled(False)
        
        #Translate Button Action
        self.ui.translate_button.clicked.connect(self.translate)
        self.ui.translate_button.setEnabled(False)
        
        #Play Button Action
        self.ui.play_button.clicked.connect(self.play)
        
        #Stop Button Action
        self.ui.stop_button.clicked.connect(self.stop)
        
        #Reset Button Action
        self.ui.reset_button_1.clicked.connect(lambda : self.ui.kan_input.setPlainText(''))
        self.ui.reset_button_1.setEnabled(False)
        self.ui.reset_button_2.clicked.connect(lambda: self.ui.en_input.setPlainText(''))
        self.ui.reset_button_2.setEnabled(False)
        
        #Signal Configurations
        self.connect(self.ui.kan_input, QtCore.SIGNAL('textChanged()'), self.kan_input_onChange)
        self.connect(self.ui.en_input, QtCore.SIGNAL('textChanged()'), self.en_input_onChange)
        
        #Analysis Button Configuration
        self.analysis_button_config()
        
        #Previous and Next Button
        self.ui.previous_button.clicked.connect(lambda : self.update_media_player(-1))
        self.ui.next_button.clicked.connect(lambda : self.update_media_player(+1))
        self.ui.refresh_button.clicked.connect(lambda : self.update_media_player(0))
        
        #Spinbox When +- buttons are pressed
        self.ui.rating.valueChanged.connect(self.update_rating)
        
        #Text Analysis Config
        self.ui.tanalysis_button.clicked.connect(lambda: self.plot_display(4))
    
    def analysis_button_config(self):
        # =====================================================================
        # Configure Analysis Menu
        # =====================================================================
        menu = QtGui.QMenu(self.ui.analysis_button)
        
        #Create Actions
        action0 = QtGui.QAction(QtGui.QIcon('ui/img/waveform.png'), 'Waveform',self.ui.analysis_button)
        action1 = QtGui.QAction(QtGui.QIcon('ui/img/spectrum.png'), 'Spectrum',self.ui.analysis_button)
        action2 = QtGui.QAction(QtGui.QIcon('ui/img/pitch_icon.png'), 'Pitch Contour',self.ui.analysis_button)
        action3 = QtGui.QAction(QtGui.QIcon('ui/img/spectrogram.png'), 'Spectrogram',self.ui.analysis_button)
        
        #Add Actions to Menu
        menu.addAction(action0)
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)
        
        #Get the action that is clicked
        menu.triggered.connect(self.analysis_menu_click)
        self.ui.analysis_button.setMenu(menu)

    def analysis_menu_click(self,action):
        # =====================================================================
        # Handler for Analysis MenuItem Click
        # =====================================================================
        action_list = ('Waveform', 'Spectrum', 'Pitch Contour', 'Spectrogram')
        self.plot_display(action_list.index(action.text())) 

    def audio_config(self):
        #Defines a Audio Output Device
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory,self)
        
        #Define an Audio Object
        self.audio = Phonon.MediaObject(self)
        self.audio.stateChanged.connect(self.start_progress_bar)
        self.audio.totalTimeChanged.connect(self.update_thread_time)
        
        #Create a Runnable Thread For Play Button
        self.play_thread = PlayThread(seconds = 0)

        #Connect Signal to Update Progress Bar
        self.connect(self.play_thread,QtCore.SIGNAL('bar_percent'), self.update_progress_bar)
        
        #`audio` is the source and `audio_output` is the sink : CREATE PATH
        Phonon.createPath(self.audio,self.audio_output)
        
        #Media Player Configure
        self.update_media_player()

    
    def show_status(self,msg,t = 1000):
        # =====================================================================
        # Implementation of Status Bar (`msg` display for `t` milliseconds)
        # =====================================================================
        self.statusBar.showMessage(msg,t)
        self.ui_update()
    
    @classmethod
    def ui_update(self):
        # =====================================================================
        # UI Updates simultaneously as the backend process runs
        # =====================================================================
        QtGui.qApp.processEvents()

    
    def synthesize(self,reverse = False):
        # =====================================================================
        # Handler Function for Synthesize Button
        # =====================================================================
        
        start_time = time.time()                                                                                
        
        #Disable Synthesize Button
        self.ui.syn_button.setEnabled(False)
        self.ui_update()
        
        #Acquire Text
        kan_txt = self.ui.kan_input.toPlainText()
        
        #Search For Duplicate
        
        wav_id = self.syn_db.search_duplicate(kan_txt)
        
        try:
            if len(wav_id) == 0:
                #If Duplicate Doesnt Exist
                wav_id = 0
                
                #Always-Unique Wave Number
                wavenum = str(time.strftime("%Y%m%d_%H%M%S"))
                
                #Write Kannada Text to temp.txt
                with open(os.environ['PRODIR']+'/etc/temp.txt', 'w') as temp_file:
                    temp_file.write('( kan_{} \" {} \")'.format(wavenum,kan_txt))
                
                self.show_status('Processing...', 0)                                                                    
                
                #DSP option Checked/Unchecked
                dsp = self.ui.dsp.isChecked()
                if dsp:
                    os.system('./FestAPI.sh 1 {}'.format(wavenum))
                else:
                    os.system('./FestAPI.sh 0 {}'.format(wavenum))
                
                #All Done...
                self.show_status('Done... ({}s)'.format('%.3f'%(time.time()-start_time)),2500)                          
                
                #Store all Synthesized Files Database
                if reverse:
                    self.syn_db.add_entry(kan_txt,wavenum,dsp)
                else:
                    self.syn_db.add_entry(kan_txt,wavenum,dsp,-1)
            
            else:
                wav_id = wav_id[0][0]
                self.show_status('Duplicate Text Found..')
        finally:
            #ReEnable Buttons Again
            self.ui.syn_button.setEnabled(True)
            self.ui_update()
            
            #Update Media Player
            self.update_media_player(wav_id)
            
            #Clear Input Text
            self.reset_all()
        
    def revSynthesize(self):
        # =====================================================================
        # Synthesize the reverse of the statement (WORDS ARE NOT REVERSED) !@
        # =====================================================================
        pass

    def translate(self):
        # =====================================================================
        # Handler Function for Translate Button
        # =====================================================================
        
        #Disable Translate Button
        self.ui.translate_button.setEnabled(False)
        self.ui_update()
        
        #Acquire Text
        en_text = self.ui.en_input.toPlainText()
        
        self.show_status('Translating...')
        
        #Call GTranslate Module
        kan_text = Essentials.en2kn(en_text) 
        self.ui.kan_input.setPlainText(kan_text)
        
        self.show_status('Done...')
        
        #Re-Enable Translate Button
        self.ui.translate_button.setEnabled(True)
        self.ui_update()
        
        #Add to Translate Database
        self.tra_db.add_new_translation(en_text, kan_text)
        
    def reset_all(self):
        # =====================================================================
        # Handler Function for Delete Key shortcut
        # =====================================================================
        self.ui.kan_input.setPlainText('')
        self.ui.en_input.setPlainText('')
    
    def kan_input_onChange(self):
        # =====================================================================
        # This function Runs everytime Kannada Text Changes
        # =====================================================================
        
        kan_txt = self.ui.kan_input.toPlainText()
        if kan_txt == '':
            self.ui.syn_button.setEnabled(False)
            self.ui.reset_button_1.setEnabled(False)
        else:
            self.ui.syn_button.setEnabled(True)
            self.ui.reset_button_1.setEnabled(True)
            
            #Allow only Kannada Input
            for x in range(len(kan_txt)):
                if ord(kan_txt[x]) in range(3200,3315) or kan_txt[x]== ' ':
                    pass
                else:
                    self.ui.kan_input.setPlainText(kan_txt[:x]+kan_txt[x+1:])  
    
    def en_input_onChange(self):
        # =====================================================================
        # This function Runs everytime English Text Changes
        # =====================================================================
        en_txt = self.ui.en_input.toPlainText()
        if en_txt == '':
            self.ui.translate_button.setEnabled(False)
            self.ui.reset_button_2.setEnabled(False)
        else:
            self.ui.translate_button.setEnabled(True)
            self.ui.reset_button_2.setEnabled(True)
    
    def play(self):
        # =====================================================================
        # Handler Function for Play Button
        # =====================================================================

        self.audio.play()
    
    def stop(self):
        # =====================================================================
        # Handler Function for Stop Button
        # =====================================================================
        
        #Stop the Audio
        self.audio.stop()
        
        if self.play_thread.isRunning():
            self.play_thread.terminate()
        self.ui.play_progress.setValue(0)
    
    def update_thread_time(self,milliseconds):
        # =====================================================================
        # Update Thread Time every time new file loads
        # =====================================================================
        
        #80 ms lost in other execution (DEPENDS ON CPU)
        error = 100
        
        #Update thread time
        self.play_thread.set_seconds(self.audio.totalTime()/(1000+error))
    
    
    def start_progress_bar(self,new_state,old_state):
        # =====================================================================
        # Start Progress Bar only after wav file loads
        # =====================================================================
        if new_state == 2:
            #Start Progress Bar Thread
            self.play_thread.start()
    
    def update_progress_bar(self,percent):
        # ======================================================================
        # Threaded Progress Bar update
        # Reentrant function runs when play_thread emits SIGNAL : bar_percent
        # ======================================================================
        self.ui.play_progress.setValue(percent)
    
    def update_media_player(self,wav_id = 0):
        # =====================================================================
        # Updates Media Player Text, Audio
        # =====================================================================
        
        try:
            if wav_id == 0:
                #Last Entry : Default and Refresh Button
                self.entry = self.syn_db.get_last_entry()[0]
                copy_entry =  self.entry[:]
            
            elif wav_id == -1:
                #Previous Entry
                copy_entry =  self.entry[:]
                self.entry = self.syn_db.get_prev_entry(self.entry[0])[0]
            
            elif wav_id == +1:
                #Next Entry
                copy_entry =  self.entry[:]
                self.entry = self.syn_db.get_next_entry(self.entry[0])[0]
            else:
                self.entry = self.syn_db.get_entry(wav_id)[0]
                copy_entry =  self.entry[:]
            
            if len(self.entry) == 0:
                #If Database is empty or No Entry is retrieved
                self.entry = copy_entry[:]
                raise Exception()
            else:
                del copy_entry

                #Set Audio File
                if bool(self.entry[3]):
                    self.audio.setCurrentSource(Phonon.MediaSource('/{}/DSP/kan_{}.wav'.format(os.environ['WAVDIR'],self.entry[1])))
                else:
                    self.audio.setCurrentSource(Phonon.MediaSource('/{}/NoDSP/kan_{}.wav'.format(os.environ['WAVDIR'],self.entry[1])))
            
                #Set Text in Text Browser
                self.ui.text_view.setPlainText(self.entry[2])
                
                #Set Rating in Spinbox
                self.ui.rating.setValue(self.entry[5])
                 
        except :#Exception as e:
            pass
        
        
    def update_rating(self,val):
        # =====================================================================
        # Updates Rating Everytime spinbox Changes
        # =====================================================================
        self.syn_db.update_rating(self.entry[0],val)
        
        #Retrive Changed Entry
        self.entry = self.syn_db.get_entry(self.entry[1])[0]
    
    def theme_select(self,theme):
        # =====================================================================
        # Handler function to select theme
        # =====================================================================
        theme_list = {
                'GTK+': self.ui.actionGTK, 
                'Windows' : self.ui.actionWindows, 
                'Plastique': self.ui.actionPlastique, 
                'Motif' : self.ui.actionMotif,
                'Cleanlooks' : self.ui.actionCleanlooks,
                'CDE' : self.ui.actionCDE
                      }
        
        for (k,v) in theme_list.items():
            if theme == k:
                self.app.setStyle(k)
                v.setChecked(True)
            else:
                v.setChecked(False)    
    
    def about(self,index):
        # =====================================================================
        # Opens About Window after setting it to correct focus
        # =====================================================================
        about_page = AboutDialog(parent = self)
        
        # Delete Object On Closing
        about_page.setAttribute(55)
        
        #Set Focus to correct Tab
        about_page.set_focus(index)
        
        #Show as Modal Dialog
        about_page.exec()
        
        #Memory Management
        del about_page
        gc.collect()
        
    def show_table(self, table):
        # =====================================================================
        # Show Table of All Synthesized Text
        # =====================================================================
        if table == 1:
            table_view = SynTableView(parent = self)
        elif table == -1:
            table_view = TraTableView(parent = self)
        # Delete Object On Closing
        table_view.setAttribute(55)
        
        #Show as Modal Dialog
        table_view.exec()
        
        #Memory Management
        del table_view
        gc.collect()
    
    def plot_display(self,index):
        # =====================================================================
        # Display Audio Analysis Window
        # =====================================================================
        plot_view = PlotView(parent = self)
        
        plot_view.set_focus(index)
        
        # Delete Object On Closing
        plot_view.setAttribute(55)
        
        #Show as Modal Dialog
        plot_view.exec()
        
        #Memory Management
        del plot_view
        gc.collect()
        

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
    
    #Application Directory
    os.environ['APP'] = os.getcwd()
    
    #Wave Files Directory
    os.environ['WAVDIR'] = os.environ['APP'] + '/../WavFiles'

#Main Function        
if __name__ == "__main__":
    
    
    #Set Permissions and Env Variables
    setEnv()
    os.system('chmod 755 FestAPI.sh')
    
    #Create and Start Application
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp(app = app)
    myapp.show()
    
    print('Application Running...')
    
    #Remove __pycache__ Folder once execution is complete
    shutil.rmtree('./__pycache__',ignore_errors=True)
    sys.exit(app.exec_())