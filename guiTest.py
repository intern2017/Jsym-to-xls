from tkinter import *
import tkinter.filedialog
import getpass
from jsymToxlsParser_fork2 import FileParse

#user = getpass.getuser()

class Window(Frame):
    
    

    def __init__(self, master= None):
        Frame.__init__(self, master)
        
        self.master=master

        self.init_window()
        
        global var
        var = IntVar()
        c = Checkbutton(self, text="Compare jsymref.jsym file", variable=var)
        c.place(x=25,y=225)

    def init_window(self):

        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        self.excelRefFile=Text(self, height=1, width=60)
        self.excelRefFile.place(x=120,y=52)
        self.excelRefFile.insert(END, "Just a text Widget\nin two lines\n")
        #self.excelRefFile.delete("1.0", END)

        #self.excelRefFile.insert(END, "test \n")
        

        loadJsymButton = Button(self, text="select .jsym file", command= self.file_select)
        loadJsymButton.place(x=25,y=50)

        outputDirectory = Button(self, text="select output directory", command= self.file_save_path)
        outputDirectory.place(x=25,y=90)
        #var = IntVar()
        #c = Checkbutton(self, text="Compare jsymref.jsym file", variable=var)
        #c.place(x=50,y=50)        
        
    def file_select(self):
    
        user = getpass.getuser()
        
        #global file
        file = tkinter.filedialog.askopenfilename(initialdir='C:/Users/%s' % user)
        self.file=file
        self.excelRefFile.delete("1.0", END)

        self.excelRefFile.insert(END, file)

        parseFile=FileParse(file)
        # Split the filepath to get the directory
        #directory = os.path.split(file)[0]
        #print(filePath.get('file'))
    
        #print(directory)
        if var.get()==1:
            
            loadJsymRefButton = Button(self, text="select .jsym file", command= self.file_select)

            loadJsymRefButton.place(x=150,y=200)

    def file_save_path(self):
        FileParse(self.file)
        self.excelRefFile.insert(END, "test \n")
        

    

root = Tk()
root.geometry("700x400")

app = Window(root)
CA= Label(root,text="jsym parser")
CA.pack()

root.mainloop()

