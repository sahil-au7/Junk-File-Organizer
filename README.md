
# JUNK FILES ORGANIZER


Imp.NOTE - I am also uploading the python file because I have explained the whole code indepth in the python file itself, so if you want to consider or give a look at it, its present there.


# NEED :
I made this Project to simplify my file Organization in a specific folder , it takes a lot of time to organize the different files in my system.


# LIBRARIES USED :
import os         -  to get all the files from the directories,to create directories  
import sys        -  to achieve the list of command line arguments passed to a Python script
import shutil     -  to move the files from one directory to another
import ntpath     -  to get the exact path of the file 
import time       -  to get the time the files are deployed in that directory
from datetime import date,datetime


# APPROACH USED : 
1. For SIZE based organization -  I have used a variable(size) to store the size of the file and then checking the file size by using the if and elif conditions and then arranging the files into their specific folders by creating new directories as per the size of the files. All the files are first moved into (Organized Directory) then inside this folder all the other directories are created accordingly. The files which are in Bytes are stored inside a new directory called BYTES and just like that all the different files are arranged in the subsequent folders(BYTES,KB,MB,GB)

2. For EXT based organization - For the Extension based organization we have created a dictionary and saved all the possible extensions I can think of to access the extensions and afterwords moving the files to their specified directories. Checking the extension of the file in the computer directory and then compairing it with the dictionary values of extensions if matched then creating the new directory named Organized and inside it moving the different files according to the specified new directories. 

3. For Time based organization - Fetching the time for the files stored inside the directories. After finding out the days it is bin stored, the files are then moved to different directories according to the no of days by comparing it using the condition statements. All the files are stored inside a single directory named Organized.  

4. For Alphabet based organization - First the no of files are accessed from the directory and then according to the starting letter the files are arranged into their subsequent directories named according to the first name of the files.
All the files are stored in a single directory named as Organized.


# HOW TO RUN :

Organized by :-
1. "size"      - to organize the files by size(BYTES,KB,MB(100MB,500MB),GB)
2. "alpha"     - to organize the files by alphabetical order
3. "ext"       - to organize the files by their specific extensions(like .py for python, .txt for plaintext) 
4. "time"      - to organize the files by their last used time (like today,this week,etc) 

 The executable file in the command line for arranging the files according to size
    Project2.exe size

