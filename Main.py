
import os

downloadDir = "C:\\Users\\Hamad Nassor\\Downloads"

#Database
audioFiles = ["aif","cda","mid","midi","mp3","mpa","ogg","wav","wma","wpl"]#a,c,m,o,w,w
compressedFiles = ["7z","arj","deb","pkg","rar","rpm","tar.gz","z","zip"]#7,a,d,p,r,t,z
discMediaFiles = ["bin","dmg","iso","toast","vcd"]#b,d,i,t,v
dataDatabaseFiles=["csv","dat","db","dbf","log","mdb","sav","sql","tar","xml"]#c,d,l,m,s,t,x
executable = ["apk","bat","bin","cgi","pl","com","exe","gadget","jar","py","wsf"]#a,b,c,p,l,c,e,g,j,p,w
fontFile =["fnt","fon","otf","ttf"]#f,f,o,t
imageFile = ["ai","bmp","gif","ico","jpeg","jpg","png","ps","psd","svg","tif","tiff"]#a,b,g,i,j,p,s,t
internetRelatedFiles = ["asp","aspx","cer","cfm","cgi","pl","css","htm","html","js","jsp","part","php","py","rss","xhtml"]#a,c,p,c,h,j,p,r,x
presentationFiles = ["key","odp","pss","ppt","pptx"]#k,o,p
programmingFiles = ["c","class","cpp","cs","h","java","sh","swift","vb"]#c,h,j,s,v
spreadsheetFiles=["ods","xlr","xls","xlsx"]#o,x
systemRelatedFiles=["bak","cab","cfg","cpl","cur","dll","dmp","drv","icns","ico","ini","ink","msi","sys","tmp"]#b,c,d,i,m.s,y
videoFiles=["3g2","2gp","avi","flv","h264","m4v","mkv","mov","mp4","mpg","mpeg","rm","swf","vob","wmv"]#2,3,a,f,h,m,r,s,v,w
wordFiles=["doc","docx","odt","pdf","rtf","tex","txt","wks","wpks","wpd"]#d,o,p,r,t,w

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

            #If it not able to print it doesn't append to the extension list
            try:
                print(file,extension[-1])
                status = True
            except:
                pass
                status = False
            if status:
                extensions.append((file,extension[1]))

    #Returns an array of extensions
    return extensions


fileExtension = fetchExtension(downloadDir)
print(fileExtension)
