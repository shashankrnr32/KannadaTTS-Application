#!/bin/sh

# =============================================================================
# Copyright (C) 2019  Shashank Sharma
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
#Description : Executable File for GUI Application
# =============================================================================
VERSION="v0.17"

clear
echo ==========================================
echo Kannada Speech Synthesis $VERSION
echo ==========================================
echo "Copyright (C) 2019  Shashank Sharma
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome 
to redistribute it under certain conditions.

(https://github.com/shashankrnr32/KannadaTTS_APP)

-i : Project Information        -v : Project Version"
echo ==========================================
if [ "$1" = "-help" ];
then
	echo -i \: Project Information
	echo -v \: Project Version
fi
if [ "$1" = "-i" ];
then
	echo "Kannada Speech Synthesis is submitted as a part of final year project by
	1. Shashank Sharma (shashankrnr32@gmail.com)		2. Srinivas N M (srinivasnm471@gmail.com)
	3. Thilak M (reddythilak13@gmail.com)			4. Varun S S (varunsridhar614@gmail.com)"
	echo
	echo "Under the guidance of Sadashiva V Chakrasali, Asst. Prof., Dept. of E&C, MSRIT, Bangalore"	
	echo ==========================================
	echo "List of Open Source Frameworks and Libraries Used"
	echo "1. Festival Speech Synthesis System (http://www.cstr.ed.ac.uk/projects/festival/)"
	echo "2. Festvox (http://festvox.org/)"
	echo "3. Edinburgh Speech Tools (http://www.cstr.ed.ac.uk/projects/speech_tools/)"
	echo "4. Speech Processing Toolkit (http://sp-tk.sourceforge.net/)"
	echo "5. Soundtouch Audio Processing Library (http://surina.net/soundtouch/)"
	echo ==========================================
	echo "This Application is a Graphical User Interface for Kannada Speech Synthesis (TTS) protected by GNU's GPL v3.0"
	echo "To obtain trained model of Kannada TTS contact any of the developers"
	echo ===========================================
fi

if [ "$1" = "-v" ];
then
	echo "$VERSION"
fi

cd App/
echo Installing Required Packages

# Soundstretch for Pitch Shift
if [ $(dpkg-query -W -f='${Status}' soundstretch 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt-get install soundstretch;
fi


#pip3 for installing Python Packages
if [ $(dpkg-query -W -f='${Status}' python3-pip 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
   sudo apt-get install -y python3-pip
fi

#Google Translate Package
python3 -c "import google.cloud.translate"
if [ $? -eq 1 ];
then
	pip3 install google-cloud-translate
fi

python3 -c "import pysptk"
if [ $? -eq 1 ];
then
	pip3 install pysptk
fi

#python-qt4 For User Interface
if [ $(dpkg-query -W -f='${Status}' python-qt4 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
   sudo apt-get install -y python-qt4 pyqt4-dev-tools python-qt4 qt4-designer python3-pyqt4.phonon
fi

#Sox Installation
if [ $(dpkg-query -W -f='${Status}' sox 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
   sudo apt-get install -y sox
fi


echo Building User Interface
pyuic4 ui/Application.ui -o Application.py
pyuic4 ui/AboutWindow.ui -o AboutWindow.py
pyuic4 ui/SynDB.ui -o SynDB.py
pyuic4 ui/Plot.ui -o Plot.py

echo Building Resources
pyrcc4 ui/AppResources.qrc  -o AppResources_rc.py -py3

echo Starting Application...
python3 Main.py

echo Exiting Application...
rm AppResources_rc.py
rm Application.py
rm AboutWindow.py
rm SynDB.py
rm Plot.py

cd ..

