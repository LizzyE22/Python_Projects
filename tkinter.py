
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg="lightgray")


        self.varFName = StringVar()
        self.varLName = StringVar()

        #Padx is horizontal padding and Pady is vertical padding 
        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        # Invoking Label widget- presented after user enters first and last name 
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
        
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightyellow')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightyellow')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        # Invoking Button class
        # Sticky tell it where you want it to "stick"
        # NE indicates top right hand side for Submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    # Defining method "submit" button, "self" is part of the class.
    def submit(self):
        #fn is FirstName variable
        fn = self.varFName.get()
        ln = self.varLName.get()
        # config() allows something to change dynamically in program while its running
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        # Self.master is name of window, 'destroy' command closes the window
        self.master.destroy()
















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()






