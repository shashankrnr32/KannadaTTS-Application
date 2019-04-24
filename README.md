# Documentation

## Kannada Speech Synthesis Application (GUI)

	v2.31

## Kannada Speech Synthesis project (Core)
Kannada Speech Synthesis is submitted as the final year project which is a part of the curriculum specified by the Department of Electronics and Communication of M S Ramaiah Institute of Technology, Bangalore. All the dependencies and frameworks which are used in the core project are mentioned in the About page of the application. Contact Developer to obtain the source and trained model of the core project.

## Developers 
<details>
<summary>Shashank Sharma (Click to Expand)</summary>

[MAIL](mailto:shashankrnr32@gmail.com)

	Core Project 
	- Preprocessing
	- Training
	- Pitch Shift using soundtretch
	- Testing on 
		- Ubuntu 18.04 on Windows Subsystem for Linux(WSL)  [Operational as Expected]
		- Ubuntu 18.04 on Google Cloud [Operational as Expected]
		- CentOS7 on Google Cloud [Not Operational due to Missing Libraries]
	
	Application
	- Complete User Interface (Main, About, Table and Analysis Window)
	- Plots (Wave, Spectrum, Spectrogram, MFCC) and Text analysis
	- Kannada Version Build
	- SQLite Database Implementation ( Synthesis and Translation)
	- Media Player Devt.
	- Database Search (With Autocomplete)
	- Production Code and Documentation
	- Application Themes
	- Testset Integration with App

</details>

<details>
<summary>Varun S S</summary>

[MAIL](mailto:varunsridhar614@gmail.com)
	
	Core Project 
	- Testing
	- Testing on Fedora [Not Operational due to Missing Libraries]

	Application
	- Synthesis Handler
	- Festival API

</details>
<details>
<summary>Srinivas N M</summary>

[MAIL](mailto:srinivasnm471@gmail.com) 

	Core Project 
	- Noise Removal using SOX
	
	Application
	- SOX integration

</details>

## Recent Updates

### Recent Updates on Core Project
1. The core project is now tested on [Ubuntu18.04 WSL (Windows Subsystem for Linux)](https://www.microsoft.com/en-in/p/ubuntu-1804-lts/9n9tngvndl3q)
2. Noise removal using SOX
3. Pitch Shifting using soundstretch

### Recent Updates on GUI Application (Added by SBS)
1. Added MFCC colormap plot
2. **The application is now available in Kannada Version** (`./run.sh -kan` or Change language within the application)
3. The audio if in testset can now be played in the misc. menu. 
4. Search option is available in Database view with autocomplete feature(Synthesis and Translation)

## Features of GUI Application
1. SQLite Based Database 
2. In-App Media Player
3. Easy to use UI
4. Database View for easy selection with search feature (Synthesis and Translation)
5. Audio Analysis for Speech Enthusiasts
6. Themes that you can choose

## Screenshots
Check the Application Screenshots in the Screenshots Directory.

## Logo

<img src="https://github.com/shashankrnr32/KannadaTTS_APP/blob/master/Screenshots/icon.svg" width=50 height=50>

Designed by Shashank Sharma on [Canva](https://www.canva.com/design/DADUBs2Lr40/GAuk1CHq5jTVj26BpkOTqw/view?utm_content=DADUBs2Lr40&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

## Building and Starting the Application

### Request for Trained Model.
Request Developer for the trained model of synthesizing Kannada Text. Setup Backend for your machine. The backend will be hosted on Web Server in future releases. Check the file `Core/README.md` for installation instructions.

### Building the Application 

1. Open `App/Main.py` and checkout `setEnv()` function. Change the directory path as per your project. 
2. Run the command below

		chmod 755 ./run.sh

### Start the Application by running run.sh

	./run.sh

## License
GNU GPL v3.0

## WaveCLI 

A collection of Wave Plot, Process and Manipulating utilities available in command line interface scripts and is developed by Shashank Sharma for this project. Have a look at the project [here](https://github.com/shashankrnr32/WaveCLI). The same project in modular version is used for analysis window in Kannada TTS Application.

