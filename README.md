# Info
## Table of contents
- Requirements
- Setup
- Credits
- Additional Info

## Requirements
- EV3 Bricks
- Wifi dongle
- Legos (especially Lego Technic)
- Laptop/PC (No matter the OS, preferably a UNIX based system)
- [VSCode](https://code.visualstudio.com)
- [NodeJS](https://nodejs.org/en/)

## Setup
### Presetup
Clone the project to your device</br>
Change directory to the folder</br>
and open the folder in VS Code
```bash
git clone https://github.com/NewDawn0/EV3-sudoku-solver
cd EV3-sudoku-solver
code .
```
Install the [EV3 VS Code](https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython) extension and connect to your EV3 device</br>
Plug in the Wi-Fi dongle into the EV3 Brick and check for internet</br>
by opening an SSH terminal and using the following command in the ssh terminal</br>
```bash
# Opening an SSH terminal
ssh robot@ev3dev.local

# Checking for internet in the ssh session
ping google.com
```
### Change the IP in the main.py on line 34 to your Ip
Get your Ip using:
On Linux:
```bash
hostname -I
```
On MacOs:
```bash
ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}'
```
On Windows (not tested)
```Powershell
Get-NetIPAddress -AddressFamily IPv4 -InterfaceIndex $(Get-NetConnectionProfile | Select-Object -ExpandProperty InterfaceIndex) | Select-Object -ExpandProperty IPAddress
```
Replace the current IP with your IP using the following syntax:</br>
```python
# main.py line 34
Board = os.system('curl -s <YourIP>:3000/api/boardOut | grep -o "[0-9]*" > io.txt')
```
### Starting the Web server for the Website on your Laptop/PC (The Device with the IP you just entered)</br>
Open a new terminal, cd into the site directory and start the server
```bash
cd site
npm start
```
If you see an output similar to below, means your server is running, and you are good to go
```javascript
> site@1.0.0 start
> node server.js

0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
Server is running on port 3000
```
You should now be able to open a browser tab on any device in the same Wi-Fi Network and open the site using the following link:
```javascript
<YourIP>:3000
```
### Finally, Check if it all works
Download and run on the EV3 Brick by <br>
pressing *<span style="color:coral">fn </span> + <span style="color:coral">f5 </span>* on your Laptop/PC in VS Code
If everything went successfully, the bot will take the board from the website and solve it

## Credits and Sources
Here is a list of external code sources that I've used in this project
- Code from [this video](https://www.youtube.com/watch?v=S4uRtTb8U-U) was used to create most of the frontend for the website
- Code from [this blog](https://levelup.gitconnected.com/sudoku-solver-python-using-backtracking-1aff17a3340) and [this blog](https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/) were used to create parts of the solving algorithm
- The rest is all original code

## Additional Info
### Project structure
```
EV3-Sudoku-Solver
├── .vscode
│  ├── extensions.json
│  ├── launch.json
│  ├── settings.json
│  └── tasks.json
├── old
│  └── testing
│     └── //Old test files
├── site
│  ├── node_modules
│  │  └── //NodeJS libraries
│  ├── public
│  │  ├── comfyWaves.jpg
│  │  ├── index.html
│  │  ├── script.js
│  │  └── style.css
│  ├── package-lock.json
│  ├── package.json
│  └── server.js
├── .gitignore
├── io.txt
├── main.py
└── README.md
```
### site folder
In the site folder are all the required components for the website

### "old" folder
The old folder is a folder containing all the older versions and test files for the project like the optimized C++ version and other unused files. None of the files in the old folder are required, meaning you can delete this folder to save disk space and the project will still run

### Important Files
- The main.py file is the file that will be executed on the EV3 Brick
- The io.txt file is a temporary file that can be deleted, but will be restored by the programme when running it again
It temporarily saves the data from the web server

