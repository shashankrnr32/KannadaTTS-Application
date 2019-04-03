# Documentation

## Kannada Speech Synthesis Application (GUI)

**Application now available in Kannada Version** (`./run.sh -kan` or Change language within the application)

	v2.01 Beta 

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
	- Testing on Windows Subsystem for Linux (Ubuntu 18.04)
	
	Application
	- Complete User Interface (Main, About, Table and Analysis Window)
	- Kannada Version Build
	- SQLite Database Implementation ( Synthesis and Translation)
	- Media Player Integration
	- Production Code and Documentation
	- Application Themes

</details>

<details>
<summary>Varun S S</summary>

[MAIL](mailto:varunsridhar614@gmail.com)
	
	Core Project 
	- Testing

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
1. **The application is now available in Kannada Version** (`./run.sh -kan` or Change language within the application)
2. Added Desktop File to run the app on double click (Provide Suitable Permissions and Change icon if needed)
3. Application now opens in Full Screen Mode
4. Added Table of details
5. Added Utterance and Label Files under Text Analysis
6. Added Translation Database and Translation Table View
7. Now, Experience the application in 6 different themes (GTK, Windows, Motif, CDE, CleanLooks, Plastique)
8. Fixed Memory Leak due to Plots
9. Save Synthesis and Translation List as CSV or Image

## Features of GUI Application
1. SQLite Based Database 
2. In-App Media Player
3. Easy to use UI
4. Database View for easy selection (Synthesis and Translation)
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
