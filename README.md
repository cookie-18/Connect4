# Connect4

This is a computer game based on the 2-Player Connection Board Game 'Connect4', created using Python, Pygame and Pyautogui.


## How to install and Run
Firstly setup a Virtual Environment by following the below steps:
1. Open Windows Powershell with Run as Administrator, and enter command ``` Set-ExecutionPolicy RemoteSigned ```.
2. Then install virtualenv, by using command ``` pip install virtualenv ```.
3. Go to the folder, where you want to create the folder for your website. (Let it be named as 'VirtualEnv' (You can choose any name!)).
4. Open Windows Powershell in that folder and run command ``` virtualenv <folder_name> ``` (Let <folder_name> be 'venv_folder').
5. Go inside the new folder created (venv_folder) by running command ``` cd <folder_name> ```.
6. Then run command ``` ./Scripts/activate ```. This will allow you to enter a functional virtual environment.
7. Then download the zip file of the code, and extract the zip inside this folder (<folder_name>, here 'venv_folder').


Then run the below commands:

```
pip install -r requirements.txt

```



## How to use
1. After you run the above mentioned commands, run the ```main.py``` file.
2. A home-page window will open on the screen, where you can enter the names of Players (by default, ther are Player 1 (red color) and PLayer 2 (yellow color)).
3. Once you enter the corresponding names (not mandatory to change the default names), you are all set to play the game.
4. You can start the game by clicking on the ```PLAY``` button.
5. Now you will be presented with the main game-play region, a screen representing the 6x7 board of acutal board-game.
6. Both the players can move as per the rules of the game as mentioned here: .
7. Now enjoy the game!


## Libraries Used

* pygame == 2.1.2
* numpy == 1.22.3
* pyautogui == 0.9.53
* Python==3.9.0


## Screen Shots

__Home Page__
![Home Page](project_assets/homepage.jpg)

__Names Entered__
![Names Entered](project_assets/NamesEntered.jpg)

__Game Board__
![Game Board](project_assets/GameBoard.jpg)

__Winning Situation__
![Winning Situation](project_assets/WinningSituation.jpg)