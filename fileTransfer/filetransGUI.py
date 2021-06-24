import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import fileTransfer_shutil

class guiWindow( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.master.geometry("600x200")
        #title explains program
        self.master.title("Check Files Modified Last 24H")
        #setting variables
        self.text1=tk.StringVar()
        self.text2=tk.StringVar()
        #button 1 select what folder to scan from
        self.btn_1 = tk.Button(self.master, text='Browse...',command=self.browsers, width=12,height=1)
        self.btn_1.grid(row=1,column=1,padx=(10,0),pady=(40,10))
        #button 2 select where to paste copies from button 1 select
        self.btn_2 = tk.Button(self.master, text='Browse...',command=self.browsers2, width=12,height=1)
        self.btn_2.grid(row=2,column=1,padx=(10,0),pady=(0,10))
        #func for checking what folders have been modified in the last 24h
        self.btn_3 = tk.Button(self.master, text='Check for files...', width=12,height=2, command= lambda:fileTransfer_shutil.Transfile(self))
        self.btn_3.grid(row=3,column=1,padx=(10,0),pady=(10,10))
        #Label for directories select and copy to
        self.entry_1 = tk.Label(self.master, width=58, text='Select a folder to scan', background='white')
        self.entry_1.grid(row=1, column=3, columnspan=5,padx=(25,0),pady=(40,10))
        self.entry_2 = tk.Label(self.master, width=58, text='Select a folder to copy to', background='white')
        self.entry_2.grid(row=2, column=3, columnspan=5,padx=(25,0),pady=(0,10))
        
    #funcs for finding directory and giving it to the labels text variable
    # label 1 func
    def browsers(self):
        self.name= fd.askdirectory()
        
        self.dir1 = self.name
        self.text1='{}/'.format(self.dir1)
        self.entry_1.config(text='{}/'.format(self.dir1))
        
    # label 2 func
    def browsers2(self):
        self.name= fd.askdirectory()
        self.dir2 = self.name
        self.text2='{}/'.format(self.dir2)
        self.entry_2.config(text='{}/'.format(self.dir2))
        
        


def main(): 
    guiWindow().mainloop()
if __name__ == '__main__':
    main()
