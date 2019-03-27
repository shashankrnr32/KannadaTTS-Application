# Documentation

## Kannada Speech Synthesis project (Core)
Kannada Speech Synthesis is submitted as the final year project which is a part of the curriculum specified by the Department of Electronics and Communication of M S Ramaiah Institute of Technology, Bangalore. All the dependencies and frameworks which are used in the core project are mentioned in the About page of the application. Contact Developer to obtain the source and trained model of the core project.

## Developers 
<details>
<summary>[Shashank Sharma](shashankrnr32@gmail.com) (Click to Expand)</summary>

	Core Project 
	- Preprocessing
	- Training
	- Pitch Shift using soundtretch
	
	Application
	- User Interface (Main, About, Table and Analysis Window)
	- SQLite Database Implementation ( Synthesis and Translation)
	- Media Player Integration
	- Production Code and Documentation
	- Application Themes

</details>

<details>
<summary>[Varun S S](varunsridhar614@gmail.com) (Click to Expand)</summary>

	Core Project 
	- Testing

	Application
	- Synthesis Handler
	- Festival API

</details>
<details>
<summary>[Srinivas N M](srinivasnm471@gmail.com) (Click to Expand)</summary>

	Core Project 
	- Noise Removal using SOX
	
	Application
	- SOX integration

</details>
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

<img src="https://github.com/shashankrnr32/KannadaTTS_APP/blob/master/App/ui/img/Icon_PNG.png" width=50 height=50>

Designed by Shashank Sharma on [Canva](https://www.canva.com/design/DADUBs2Lr40/GAuk1CHq5jTVj26BpkOTqw/view?utm_content=DADUBs2Lr40&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

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
