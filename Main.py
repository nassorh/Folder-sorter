from Classes.FolderSorter import *
import tkinter as tk
from tkinter import filedialog

class GUI():
    def __init__(self,root):
        self.master = root
        self.master.geometry("550x100")
        self.master.title("Folder Sorter")
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self.master.grid_columnconfigure(0, weight=1)

    def mainScreen(self):
        mainTitle = tk.Label(self.frame, text = "Welcome To The Folder Sorter 2.0")
        mainTitle.config(font=("Courier","20"))
        mainTitle.grid(row = 2,column = 3)
        directoryText = tk.Button(self.frame, text = "Select Folder",command=self.sortAlgorithm)
        directoryText.config(font=("Courier","10"))
        directoryText.grid(row=5,column=3)
        
    def sortAlgorithm(self):
        folder_selected_dir = filedialog.askdirectory()
        files = Folder_Sorter.get_all_files(folder_selected_dir) 
        Folder_Sorter.move_files(folder_selected_dir,files)
        self.successful()

    def successful(self):
        top = tk.Toplevel()
        top.title("Successful")
        msg = tk.Label(top, text ="If any errors were present please send the log file to the admin\nEmail: nassorh.dev@gmail.com")
        msg.pack()
        top.mainloop()


root = tk.Tk()
gui = GUI(root)
gui.mainScreen()
root.mainloop()