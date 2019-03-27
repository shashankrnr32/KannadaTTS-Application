# Documentation

## Developers 
[Shashank Sharma](shashankrnr32@gmail.com)

	- User Interface (Main, About, Table and Analysis Window)
	- Translation (en - kan)
	- SQLite Database Implementation ( Synthesis and Translation)
	- Media Player Integration
	- Production Code and Documentation
	- Application Themes

[Varun S S](varunsridhar614@gmail.com)

	- Festival API

[Srinivas N M](srinivasnm471@gmail.com)

	- Noise Removal using sox

## Recent Updates
1. Added Keyboard Shortcut (`./run.sh -s` to view shortcuts)
2. Added Translation Database and Translation Table View
3. Now, Experience the application in 6 different themes (GTK, Windows, Motif, CDE, CleanLooks, Plastique)
4. Added Spectrogram to Audio Analysis
5. Fixed Memory Leak due to Plots
6. The synthesize handler now checks for duplicate text in database
7. Audio analysis plots is added now.
8. Added Context Menu to increase responsiveness

## Features
1. SQLite Based Database 
2. In-App Media Player
3. Easy to use UI
4. Database View for easy selection (Synthesis and Translation)
5. Audio Analysis for Speech Enthusiasts
6. Themes that you can choose

## Screenshots
Check the Application Screenshots in the Screenshots Directory.

## Logo

<img source="https://github.com/shashankrnr32/KannadaTTS_APP/blob/master/App/ui/img/Icon_PNG.png" width=50 height=50>

## Building and Starting the Application

### Request for Trained Model.
Request Developer for the trained model of synthesizing Kannada Text. Setup Backend for your machine. The backend will be hosted on Web Server in future releases.

### Building the Application 

1. Open `App/Main.py` and checkout `setEnv()` function. Change the directory path as per your project. 
2. Run the command below

		chmod 755 ./run.sh

### Start the Application by running run.sh

	./run.sh

## License
GNU GPL v3.0
