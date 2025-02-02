# APP CRASHER
## Main Purpose
A project that prevents the user from using an application when it is open

## How to use this project
First, download the <ins>'secret_folder'</ins> from the repository to your computer. 
This folder contains a JSON file necessary for the app to start and another folder with files that block the user from using their computer.
To start the app, write the file path of this folder into the <ins>'path'</ins> variable in the <ins>'main'</ins> code file.
Then, write the name of the application that is being used on your computer in the <ins>'app_name'</ins> section inside the main file. If the application is not running, you must make sure that the name you wrote is correct.
Also, to make the software work, enter <ins>'yes'</ins> in the <ins>'key'</ins> section of the JSON file.

## Where can I use this project
I turned this project into an executable file using the **pyinstaller** module so that it runs in the background on my computer without anyone noticing.
I made this exe file a startup application on the computer.
This way, if someone opens applications like Outlook on the computer without my knowledge, it blocks them.
Or, you can prank your friend if you want.

### NOTICE
Depending on your computer's power, you can adjust the control time or the application startup time from within the application
