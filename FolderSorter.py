import os, shutil
import tkinter as tk
from tkinter import filedialog

class folderSorter():
    # def __init__(self,downloadDir):
    #     # self.downloadDir = downloadDir
    #     # self.extensions = []
    #     # self.fileCatergory = []
    #     # self.folderNames = []

    def fetchExtension(self,downloadDir):
        #Vaild directory
        if os.path.isdir(downloadDir):
            extensions = []
            allFiles = os.listdir(downloadDir)

            #Fetches all the extension
            for file in allFiles:
                if "." in file:
                    extension = file.split(".")
                    extensions.append((file,extension[-1].lower()))
            
            return extensions
        else:
            raise Exception("File Directory is not valid")

    def sortCatergory(self):
        #Database
        catergory = ["audioFiles","compressedFiles","discMediaFiles","dataDatabaseFiles","executable","fontFile","imageFile","internetRelatedFiles","presentationFiles""programmingFiles","systemRelatedFiles","videoFiles","wordFiles"]
        extensions = {
            "aif":0,"cda":0,"mid":0,"midi":0,"mp3":0,"mpa":0,"ogg":0,"wav":0,"wma":0,"wpl":0,
            "7z":1,"arj":1,"deb":1,"pkg":1,"rar":1,"rpm":1,"tar.gz":1,"z":1,"zip":1,
            "bin":2,"dmg":2,"iso":2,"toast":2,"vcd":2,
            "csv":3,"dat":3,"db":3,"dbf":3,"log":3,"mdb":3,"sav":3,"sql":3,"tar":3,"xml":3,
            "apk":4,"bat":4,"bin":4,"cgi":4,"pl":4,"com":4,"exe":4,"gadget":4,"jar":4,"py":4,"wsf":4,"lnk":4,
            "fnt":5,"fon":5,"otf":5,"ttf":5,
            "ai":6,"bmp":6,"gif":6,"ico":6,"jpeg":6,"jpg":6,"png":6,"ps":6,"psd":6,"svg":6,"tif":6,"tiff":6,
            "asp":7,"aspx":7,"cer":7,"cfm":7,"cgi":7,"pl":7,"css":7,"htm":7,"html":7,"js":7,"jsp":7,"part":7,"php":7,"py":7,"rss":7,"xhtml":7,"url":7,
            "key":8,"odp":8,"pss":8,"ppt":8,"pptx":8,
            "c":9,"class":9,"cpp":9,"cs":9,"h":9,"java":9,"sh":9,"swift":9,"vb":9,
            "ods":10,"xlr":10,"xls":10,"xlsx":10,
            "bak":11,"cab":11,"cfg":11,"cpl":11,"cur":11,"dll":11,"dmp":11,"drv":11,"icns":11,"ico":11,"ini":11,"ink":11,"msi":11,"sys":11,"tmp":11,
            "3g2":12,"2gp":12,"avi":12,"flv":12,"h264":12,"m4v":12,"mkv":12,"mov":12,"mp4":12,"mpg":12,"mpeg":12,"rm":12,"swf":12,"vob":12,"wmv":12,
            "doc":13,"docx":13,"odt":13,"pdf":13,"rtf":13,"tex":13,"txt":13,"wks":13,"wpks":13,"wpd":13
        }

        #files and thier catergory
        fileCatergory =[]

        #extension that are not recognised
        extensionError=[]

        for file in self.extensions:

            #Makes the code more readable
            filename = file[0]
            extension = file[1]

            if extensions.get(extension):
                catergoryName = catergory[extensions.get(extension)]
                fileCatergory.append((filename,catergoryName))
            else:
                extensionError.append(extension)

            # count = 0
            # for catergory in catergorys:
            #     catergoryName = catergory[0]
            #     if extension in catergory:
            #         fileCatergory.append((filename,catergoryName)) #If the file catergory is found the file name and catergory name is stored in the array
            #     else:
            #         count += 1
            #         if count > 13: #After checking through the 13 catergorys its add the extension to list of extension which are not listed
            #             if extension not in extensionError:
            #                 extensionError.append(extension)

        self.log(("extension that needed to be added: ",extensionError,"\n"))
        self.fileCatergory = fileCatergory #Returns an array of the filename and the catergory

    def foldersToCreate(self):
        folders  = []
        for catergory in self.fileCatergory:
            folderName = catergory[1]
            if folderName not in folders:
                folders.append(folderName)

        self.folderNames = folders #returns the array of folders to create

    def createFolders(self):
        for folder in self.folderNames:
            FileDirectory = self.downloadDir + "\\" + folder
            try:
                # Create target Directory
                os.mkdir(FileDirectory)
                self.log(("Directory " , FileDirectory ,  " Created\n"))
            except FileExistsError:
                self.log(("Directory " , FileDirectory ,  " already exists\n"))

    def moveFiles(self):
        for files in self.fileCatergory:
            filename = files[0]
            FolderName = files[1]
            sourceDirectory = self.downloadDir + "\\" + filename
            destinationFolder = self.downloadDir + "\\" + FolderName + "\\" + filename
            try:
                os.rename(sourceDirectory,destinationFolder)
            except:
                self.log((filename, "Error: Coudln't move the file\n"))

    def log(self,data):
        file = open("Log.txt","w+")
        for x in data:
            file.writelines(x)
        file.close()

test = folderSorter()
test.fetchExtension("")