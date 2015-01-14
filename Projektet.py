from Tkinter import *

class MainApp():
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.frame.pack()
        
        self.button_fysik = Button(self.frame,text = "Fysik",
                                   command = self.fysik)
        self.button_fysik.pack()

    def fysik(self):
        fys = Fysik(self.frame)
        

class Fysik():
    def __init__(self, parent):
        self.top = Toplevel(parent)
        msg = Message(self.top, text = "Test")
        msg.pack()

        button_kinematik = Button(self.top, text = "Kinematik",
                                  command = self.kinematik)
        button_kinematik.pack()

    def kinematik(self):
        print "Hello"



root = Tk()
app = MainApp(root)

root.mainloop()

