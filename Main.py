from FolderSorter import *

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