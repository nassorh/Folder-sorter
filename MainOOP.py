import os, shutil
import tkinter as tk
from tkinter import filedialog

class folderSorter():
    def __init__(self,downloadDir):
        self.downloadDir = downloadDir
        self.extensions = []
        self.fileCatergory = []
        self.folderNames = []

    def fetchExtension(self):
        #Vaild directory
        if os.path.isdir(self.downloadDir):
            #Define all the extension array
            extensions = []

            #All files in the folders
            arrayOfFiles = os.listdir(self.downloadDir)

            #Fetches all the extension
            for file in arrayOfFiles:
                if "." in file:
                    extension = file.split(".")
                    extensions.append((file,extension[-1]))
            #Returns an array of extensions
            self.extensions = extensions
        else:
            raise Exception("File Directory is not valid")

    def sortCatergory(self):
        #Database
        catergorys = [
        ["audioFiles","aif","cda","mid","midi","mp3","mpa","ogg","wav","wma","wpl"],#a,c,m,o,w
        ["compressedFiles","7z","arj","deb","pkg","rar","rpm","tar.gz","z","zip"],#7,a,d,p,r,t,z
        ["discMediaFiles","bin","dmg","iso","toast","vcd"],#b,d,i,t,v
        ["dataDatabaseFiles","csv","dat","db","dbf","log","mdb","sav","sql","tar","xml"],#c,d,l,m,s,t,x
        ["executable","apk","bat","bin","cgi","pl","com","exe","gadget","jar","py","wsf","lnk"],#a,b,c,p,l,e,g,j,w
        ["fontFile","fnt","fon","otf","ttf"],#f,f,o,t
        ["imageFile","ai","bmp","gif","ico","jpeg","jpg","png","ps","psd","svg","tif","tiff"],#a,b,g,i,j,p,s,t
        ["internetRelatedFiles","asp","aspx","cer","cfm","cgi","pl","css","htm","html","js","jsp","part","php","py","rss","xhtml","url"],#a,c,p,h,j,p,r,x
        ["presentationFiles","key","odp","pss","ppt","pptx"],#k,o,p
        ["programmingFiles","c","class","cpp","cs","h","java","sh","swift","vb"],#c,h,j,s,v
        ["spreadsheetFiles","ods","xlr","xls","xlsx"],#o,x
        ["systemRelatedFiles","bak","cab","cfg","cpl","cur","dll","dmp","drv","icns","ico","ini","ink","msi","sys","tmp"],#b,c,d,i,m.s,y
        ["videoFiles","3g2","2gp","avi","flv","h264","m4v","mkv","mov","mp4","mpg","mpeg","rm","swf","vob","wmv"],#2,3,a,f,h,m,r,s,v,w
        ["wordFiles","doc","docx","odt","pdf","rtf","tex","txt","wks","wpks","wpd"]#d,o,p,r,t,w
        ]

        #files and thier catergory
        fileCatergory =[]

        #extension that are not recognised
        extensionError=[]

        for file in self.extensions:

            #Makes the code more readable
            filename = file[0]
            extension = file[1]

            count = 0
            for catergory in catergorys:
                catergoryName = catergory[0]
                if extension in catergory:
                    fileCatergory.append((filename,catergoryName)) #If the file catergory is found the file name and catergory name is stored in the array
                else:
                    count += 1
                    if count > 13: #After checking through the 13 catergorys its add the extension to list of extension which are not listed
                        if extension not in extensionError:
                            extensionError.append(extension)

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

class GUI():
    def __init__(self,root):
        self.master = root
        self.master.geometry("550x100")
        self.master.title("Folder Sorter")
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self.master.grid_columnconfigure(0, weight=1)
        #folder_selected = filedialog.askdirectory()
        #print(folder_selected)

    def mainScreen(self):
        mainTitle = tk.Label(self.frame, text = "Welcome To The Folder Sorter 2.0")
        mainTitle.config(font=("Courier","20"))
        mainTitle.grid(row = 2,column = 3)
        directoryText = tk.Button(self.frame, text = "Select Folder",command=self.sortAlgorithm)
        directoryText.config(font=("Courier","10"))
        directoryText.grid(row=5,column=3)

    def sortAlgorithm(self):
        folder_selected = filedialog.askdirectory()
        sort = folderSorter(folder_selected) #Classes the folder sort class
        sort.fetchExtension()#Fetches all extension from files
        sort.sortCatergory()#Fetches all catergory
        sort.foldersToCreate()#Fetches all folders that need to be created
        sort.createFolders()#Creates all the folders
        sort.moveFiles()#Moves all the files into folders
        self.successful()

    def successful(self):
        top = tk.Toplevel()
        top.title("Successful")
        msg = tk.Label(top, text ="Folders sorted please check the log fils for any errors\nIf any errors were present please send the log file to the admin\nEmail: nassorh.dev@gmail.com")
        msg.pack()
        top.mainloop()

root = tk.Tk()
gui = GUI(root)
gui.mainScreen()
root.mainloop()
