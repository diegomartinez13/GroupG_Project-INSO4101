# INSO4101 Group G Project | Educational Recycling Platform 
Final project of the Group G of INSO4101


This repository contains the files required to run the backend using Flask, to start the frontend using ReactJS and a docker-compose file that starts a PostgreSQL database. The database is initially created with the following database tables:

- Users
- Events
- Posts
- RecyclingEfforts
- RecyclingCenters
- HasReaction

They are populated with mock testing data. The contents can be seen in /backend/db/init.sql.

## Setting up the development environment
To setup the development environment ensure you have the following software installed on your machine:
- Python 3.10.6 or later version - [Windows](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe) / [Mac](https://www.python.org/ftp/python/3.10.6/python-3.10.6-macos11.pkg)
- Node.js - [Windows](https://nodejs.org/dist/v18.14.2/node-v18.14.2-x64.msi) / [Mac](https://nodejs.org/dist/v18.14.2/node-v18.14.2.pkg)
- Docker Desktop - [Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module) / [Mac](https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module) (Intel Chip) / [Mac](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module) (Apple Chip)
- Git - [Windows](https://git-scm.com/download/win) / [Mac](https://git-scm.com/download/mac)

### Visual Studio Code

#### Cloning the project
1. Open a new Visual Studio Code Window
2. Select *Clone Git Repository* and follow the steps to connect your GitHub account
3. Provide the repository URL (https://github.com/diegomartinez13/GroupG_Project-INSO4101.git)

#### Backend

1. Open a new terminal in Visual Studio Code
2. Create a python environment with `python3 -m venv venv`
3. Activate/enter the python environment

| Platform  | Command to activate virtual environment |
| ------------- |--| 
| Windows (cmd.exe) |`C:\> .\venv\Scripts\activate.bat` |
| Windows (PowerShell) | `PS C:\> .\venv\Scripts\Activate.ps1` |
| POSIX (bash/zsh)  | `$ source venv/bin/activate`    |
| POSIX (fish)      | `$ source venv/bin/activate.fish`    | 
| POSIX (csh/tcsh)      | `$ source venv/bin/activate.csh`     | 
| POSIX (PowerShell | `$ venv/bin/Activate.ps1` |


4. Install python requirements `pip install -r requirements.txt`
5. Start the Flask backend `flask --app app run --debug`
6. If everything was successful you should see the following
```* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ###-###-###
```

#### Frontend
1. Open a new terminal in Visual Studio Code
2. Navigate to the frontend folder `cd frontend`
3. Run `npm start`
4. If everything was successful you should see the following
```
Compiled successfully!
You can now view frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://172.17.0.2:3000
  
Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
```

#### Database
1. Open a new terminal in Visual Studio Code
2. Run `docker-compose up -d`
