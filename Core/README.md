
# Kannada Speech Synthesis - WSL

Compiled by [Shashank Sharma](https://www.linkedin.com/in/shashank-sharma-932701108/)

## Ubuntu 18.04 on WSL <sup><sub>(Windows Subsystem for Linux)</sup></sub>

Given Below are the steps to install and run Kannada Speech synthesis on `Ubuntu -18.04  WSL`

References in the following tutorial, 

	Application/App : Ubuntu Terminal Application
	

### Step 1 : Installing Ubuntu WSL
1. Install [**Ubuntu 18.04 LTS**](https://www.microsoft.com/en-in/p/ubuntu-1804-lts/9n9tngvndl3q) from Microsoft Store.
2. Launch `Ubuntu 18.04` Windows Application.
3. The application possibly pops up with the error below

		The WSL optional component is not enabled. Please enable it and try again.

4. Close the application.
5.  Open up `Windows Powershell` and type in the command below
			
		Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
		
	This command above enables Windows Subsystem so that you can run Linux on your machine.
6. Restart the machine on prompt
7. Launch the application after system startup.
8. Ubuntu subsystem will now be installed on your machine. This process will take a few minutes to complete.
9. Enter your username and password when prompted
10.  Installation is complete. Typing in `echo Hello World` will check the installation.

### Step 2 : Copying the Project to Ubuntu SubSys

Once the installation of Ubuntu is complete, the project folder has to be copied from Windows to Ubuntu. To do so, follow the steps as given below.

1. Copy the folder with project zip file to `C:/` drive. (Say `Project/Main.zip`)
2. Open the application and change the directory as below 

		cd /mnt/c
3. Copy/Move the Zip File to your home directory with the command 

		cp Project/Main.zip /home/<USERNAME>/Main.zip

4. Change your directory to home by typing

		cd ~
5. Extract the Main.zip file to your directory by

		mkdir Project
		sudo apt install unzip
		unzip Main.zip -d Project
6. A directory named `Project/Main` will be created after unzip. 
7.  Change your directory to Main

		cd Project/Main
8. Typing `ls` will list all your folders and files in the Main folder

### Step 3 : Setting up libraries

1. Install the compilers and Ubuntu Packages below

		sudo apt-get gcc
		sudo apt-get install gcc-4.8
		sudo apt-get install libncurses5-dev

### Step 4 : Setup a Input-Output Folder

Create a folder tree on a drive as given below. The choice of  drive is left to the user.
		
	F:/
	|
	|----- IO_Kan_Syn
	       |
	       |-----Input
	       |-----Output

- `Input` serves the project to feed input
- The obtained TTS output can be copied to `Output` Directory'

### Step 5 : Synthesizing a Kannada Text
1. Copy the Kannada text to a .txt file in your Input Folder. (say `kan.txt`)

		( kan_file_name " ಈ ಕೃತಿಗೆ ಕೇಂದ್ರ ಸಾಹಿತ್ಯ ಅಕಾಡೆಮಿ ಪ್ರಶಸ್ತಿ ಲಭಿಸಿದೆ ")

	*kan_file_name* : The .wav file name stored after synthesis
2.  Open Ubuntu Application. Change your directory to `Project/Main`.
3. Set Environment Variables by running
	
		source ./env.sh
4. Execute the command below by changing the directory to `cmu_indic_kan_female`

		./bin/do_clustergen cg_test tts tts /mnt/f/IO_Kan_Syn/Input/kan.txt

5. The output is stored in `test/tts/` directory. Copy / Move the file to Output folder

		cp test/tts/kan_file_name.wav /mnt/f/IO_Kan_Syn/Output/
6. Play the audio from the Output directory.


Note : The following steps are mentioned for Ubuntu WSL. The same applies for any Ubuntu OS machine.
