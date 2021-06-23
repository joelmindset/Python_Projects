import tkinter as tk
from tkinter import *
import webgenerator

class guiWebGenerator( Frame ):
    def __init__(self):
        tk.Frame.__init__(self)
        #main window
        self.master.geometry("600x200")
        self.master.title("Web Page Generator")
        self.lbl_1 = tk.Label(self.master, text='Body content: ')
        self.lbl_1.grid(row=1,column=0)
        #body entry        
        self.entry = tk.Entry(self.master, text='')    
        self.entry.grid(row=1,column=1,padx=10,pady=(10,10),ipady=60,ipadx=140)
        #btn for rewrite
        self.btn_sub = tk.Button(self.master, text='Submit', command= lambda:webgenerator.webpageWrite(self))
        self.btn_sub.grid(row=2,column=1)
        #btn for open page
        self.btn_page = tk.Button(self.master, text='Open Webpage', command= lambda:webgenerator.Webpage(self))
        self.btn_page.grid(row=2,column=0,padx=(10,0))
        




def main(): 
    guiWebGenerator().mainloop()
if __name__ == '__main__':
    main()
