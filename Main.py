import os,shutil

downloadDir = "C:\\Users\\Hamad Nassor\\Downloads"

def printFileName(fileName):
    try:
        print(fileName)
    except:
        for c in fileName:
            try:
                print(c,end="")
            except:
                print("?",end="")

def fetchExtension(folderDir):
    #Define all the extension array
    extensions = []

    #Status whether to add to the array or not
    status = True

    #All files in the folders
    arrayOfFiles = os.listdir(folderDir)

    #Fetches all the extension
    for file in arrayOfFiles:
        if "." in file:
            extension = file.split(".")
            extensions.append((file,extension[-1]))
    #Returns an array of extensions
    return extensions

def sortCatergory(extensionArray):

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

    for file in extensionArray:

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


    print("--Send these details to an admin--\nThese extension need to be added:\n",extensionError,"\n")
    return fileCatergory #Returns an array of the filename and the catergory

def foldersToCreate(fileCatergoryArray,Directory):
    folders  = []
    for catergory in fileCatergoryArray:
        folderName = catergory[1]
        if folderName not in folders:
            folders.append(folderName)

    return folders #returns the array of folders to create

def createFolders(foldersName,Directory):
    for folder in folderNames:
        FileDirectory = Directory + "\\" + folder
        try:
            # Create target Directory
            os.mkdir(FileDirectory)
            print("Directory " , FileDirectory ,  " Created ")
        except FileExistsError:
            print("Directory " , FileDirectory ,  " already exists")

def moveFiles(filesCatergory,Directory):
    for files in filesCatergory:
        filename = files[0]
        FolderName = files[1]
        sourceDirectory = Directory + "\\" + filename
        destinationFolder = Directory + "\\" + FolderName + "\\" + filename
        try:
            os.rename(sourceDirectory,destinationFolder)
        except:
            print(filename, "Error contact an admin")


fileExtension = fetchExtension(downloadDir)
printFileName(fileExtension)
fileCatergory = sortCatergory(fileExtension)
folderNames = foldersToCreate(fileCatergory,downloadDir)
createFolders(folderNames,downloadDir)
moveFiles(fileCatergory,downloadDir)
