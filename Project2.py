#Python project on arrangements of files in a specific order.
#Created by - Sahil student of AttainU Robin Batch
#Also added some Comments to make the code a little more understandable.

# Libraries used in the Project
import os 
import sys
import shutil
import ntpath
import time
from datetime import date,datetime

#Dictionary to specify different types of extensions we are using to distribute the files accordingly. 
DIRECTORIES = { 
    "HTML": [".html5", ".html", ".htm", ".xhtml"], 
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd"], 
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp"], 
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  "pptx"], 
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                 ".dmg", ".rar", ".xar", ".zip"], 
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
    "PLAINTEXT": [".txt", ".in", ".out"], 
    "PDF": [".pdf"], 
    "PYTHON": [".py"], 
    "XML": [".xml"], 
    "EXE": [".exe"], 
    "SHELL": [".sh"]  
} 


FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats}


#Function which organizes the files according to the extension.
def Organize_by_extension():
    # To give the path of the present Directory to the variable inputFilePath
    inputFilePath = os.getcwd()
    #applying for loop for each file inside the present directory
    for eachFile in os.scandir(): 
        if not eachFile.is_dir():
            filePath = os.path.abspath(eachFile)
            #storing the extension of file inside a variable
            fileExtension = os.path.splitext(filePath)[1].lower()
            #checking the extension with the File_Formats
            if fileExtension in FILE_FORMATS:
                destParentFolder = os.path.join(inputFilePath,"Organized")
                #checking if the directory is present if not then creating the directory named as Organized
                if not os.path.exists(destParentFolder):
                    os.mkdir(destParentFolder)
                #creating the new folders as naming inside the dictionary above    
                destFolder = os.path.join(destParentFolder,FILE_FORMATS[fileExtension])
                #checking if already present
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                #moving the file to the created directory    
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                #removing the older path of file
                if os.path.exists(Destination):
                    os.remove(filePath)


#Function which organizes the files according to the alphabetical order.
def Organize_by_alphabet():
    #gets the present directory path
    inputFilePath = os.getcwd()
    for eachFile in os.scandir():
        if not eachFile.is_dir():
            # gets the path of each file inside the directory
            filePath = os.path.abspath(eachFile)
            #creating a new directory named Organized
            destParentFolder = os.path.join(inputFilePath,"Organized")
            #checking if the directory already exists if not then create the directory named as Organized
            if not os.path.exists(destParentFolder):
                os.mkdir(destParentFolder)
            #code for checking each file by the alphabets
            #pylint: disable=unused-argument
            head,tail = ntpath.split(filePath)
            head = head+1
            alp = tail[0].upper()
            destFolder = os.path.join(destParentFolder,alp)
            #making new directory according to the alphabet
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            # moving the files to the new directory created     
            shutil.copy2(filePath,destFolder)
            Destination = os.path.join(destFolder,eachFile)
            #removing the old file path 
            if os.path.exists(Destination):
                os.remove(filePath)


# rest all the functions are same as the above with little changes in the code according to the needs so
# not explaining the rest of the code                    

#Function which organizes the files according to the last used.
def Organize_by_time():
    inputFilePath = os.getcwd()
    date_format = "%m/%d/%Y"
    today = date.today().strftime('%m/%d/%Y')
    start = datetime.strptime(today, date_format)
    for eachFile in os.scandir():
        if not eachFile.is_dir():
            filePath = os.path.abspath(eachFile)
        destParentFolder = os.path.join(inputFilePath,"Organized")
        if not os.path.exists(destParentFolder):
            os.mkdir(destParentFolder)
        file_date = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(filePath)))
        end = datetime.strptime(file_date, date_format)
        days = (start-end).days
        if days==0:
            destFolder = os.path.join(destParentFolder,"Today")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        elif days == 1:
            destFolder = os.path.join(destParentFolder,"Yesterday")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        elif 1<days<=7:
            destFolder = os.path.join(destParentFolder,"This_Week")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        elif 7<days<=31:
            destFolder = os.path.join(destParentFolder,"This_Month")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        elif 31<days<=62:
            destFolder = os.path.join(destParentFolder,"Last_Month")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        elif 62<days<=365:
            destFolder = os.path.join(destParentFolder,"This_Year")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        elif 365<days:
            destFolder = os.path.join(destParentFolder,"Long_Time")
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            shutil.copy2(filePath,destFolder)
        Destination = os.path.join(destFolder,eachFile)
        if os.path.exists(Destination):
            os.remove(filePath)


#Function which organizes the files according to the Size of the files (mentioned in if conditions accordingly).
def Organize_by_size():
    inputFilePath = os.getcwd()
    for eachFile in os.scandir():
        if not eachFile.is_dir():
            filePath = os.path.abspath(eachFile)
            size = os.stat(eachFile).st_size
            destParentFolder = os.path.join(inputFilePath,"Organized")
            if not os.path.exists(destParentFolder):
                os.mkdir(destParentFolder)                
            #For the files sized in Bytes    
            if 0<=size<1000 :
                destFolder = os.path.join(destParentFolder,"BYTES")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)                
            #For the files sized in KB's only
            elif 1000<size<1000000:
                destFolder = os.path.join(destParentFolder,"KB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)                
            #For the files size uptil 100 MB         
            elif 1000000<size<100000000:
                destFolder = os.path.join(destParentFolder,"100MB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)                
            #For files size uptil 500 MB
            elif 100000000<size<500000000:
                destFolder = os.path.join(destParentFolder,"500MB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)                
            #For files more than a GB
            elif size>1000000000:
                destFolder = os.path.join(destParentFolder,"GB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)

#Main function/Source
if __name__=='__main__':
    #Taking the input from Command line using Command line parsing.
    Organize = sys.argv[1]
    # Checking for Different Conditions of the input from the Command line.
    # 1.  "ext"    =   for Extensions
    # 2.  "alpha"  =   for Alphabetical order
    # 3.  "size"   =   for Size of file
    # 4.  "time"   =   for Time

    if Organize == "ext":
        Organize_by_extension()
    elif Organize == "size":
        Organize_by_size()
    elif Organize == "alpha":
        Organize_by_alphabet() 
    elif Organize == "time":
        Organize_by_time()           