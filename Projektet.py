# -*- coding: cp1252 -*-
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

        button_kinematik = Button(self.top, text = "Bevægelse i 1D",
                                  command = self.movement_1d)
        button_kinematik.pack()

    def movement_1d(self):
        global find_list, har_list
        top_beregn = Toplevel(self.top)
        msg_find = Message(top_beregn, text = "Vælg hvad du vil finde?")
        msg_find.grid(row = 0)
        find_list = Listbox(top_beregn, exportselection = 0)
        find_list.grid(row = 1)
        muligheder = ["Starhastighed: v0", "Strækning: s", "Tid: t",
                      "Accelration: a", 'Startrækning: s0', 'Hastighed: v']
        for item in muligheder:
            find_list.insert(END, item)

        msg_har = Message(top_beregn, text = "Hvad information har du?")
        msg_har.grid(row = 0, column = 1)
        har_list = Listbox(top_beregn, selectmode = MULTIPLE, exportselection = 0)
        har_list.grid(row = 1, column = 1)
        for item in muligheder:
            har_list.insert(END, item)
        kin_beregning_knap = Button(top_beregn, text = "Test",
                                    command = self.kin_beregning)
        kin_beregning_knap.grid(row = 2)
        
        
     
    def kin_beregning(self):
        find_valgt = map(int, find_list.curselection())[0]
        har_valgt = map(int, har_list.curselection())
        #For at tjekke for formel s=0.5*a*t^2+v0*t+s0
        if (1 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            0 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (0 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            1 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (2 == find_valgt and 3 in har_valgt and 0 in har_valgt and
            1 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (3 == find_valgt and 0 in har_valgt and 2 in har_valgt and
            1 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (4 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            1 in har_valgt and 0 in har_valgt):
            print "Good job"
        elif (1 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            0 in har_valgt):
            print "Good job"
        elif (0 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            1 in har_valgt):
            print "Good job"
        elif (2 == find_valgt and 3 in har_valgt and 0 in har_valgt and
            1 in har_valgt):
            print "Good job"
        elif (3 == find_valgt and 0 in har_valgt and 2 in har_valgt and
            1 in har_valgt):
            print "Good job"
        # For at tjekke for formel v^2=v0^2+2*a*(s-s0)
        elif (5 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            3 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (0 == find_valgt and 5 in har_valgt and 1 in har_valgt and
            3 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (1 == find_valgt and 0 in har_valgt and 5 in har_valgt and
            3 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (3 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            5 in har_valgt and 4 in har_valgt):
            print "Good job"
        elif (4 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            3 in har_valgt and 5 in har_valgt):
            print "Good job"
        elif (5 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            3 in har_valgt):
            print "Good job"
        elif (0 == find_valgt and 5 in har_valgt and 1 in har_valgt and
            3 in har_valgt):
            print "Good job"
        elif (1 == find_valgt and 0 in har_valgt and 5 in har_valgt and
            3 in har_valgt):
            print "Good job"
        elif (3 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            5 in har_valgt):
            print "Good job"
        #For at tjekke for formal v=a*t
        elif (5 == find_valgt and 0 in har_valgt and 2 in har_valgt and
              3 in har_valgt):
            print "Good job"
        elif (0 == find_valgt and 5 in har_valgt and 2 in har_valgt and
              3 in har_valgt):
            print "Good job"
        elif (2 == find_valgt and 0 in har_valgt and 5 in har_valgt and
              3 in har_valgt):
            print "Good job"
        elif (3 == find_valgt and 0 in har_valgt and 2 in har_valgt and
              5 in har_valgt):
            print "Good job"
        elif (5 == find_valgt and 2 in har_valgt and 3 in har_valgt):
            print "Good job"
        elif (2 == find_valgt and 5 in har_valgt and 3 in har_valgt):
            print "Good job"
        elif (3 == find_valgt and 2 in har_valgt and 5 in har_valgt):
            print "Good job"
        #For at for formel s=t*v+s0
        elif (1 == find_valgt and 2 in har_valgt and 5 in har_valgt
              and 4 in har_valgt):
            print "Good job"
        elif (2 == find_valgt and 1 in har_valgt and 5 in har_valgt
              and 4 in har_valgt):
            print "Good job"
        elif (5 == find_valgt and 2 in har_valgt and 1 in har_valgt
              and 4 in har_valgt):
            print "Good job"
        elif (4 == find_valgt and 2 in har_valgt and 5 in har_valgt
              and 1 in har_valgt):
            print "Good job"
        elif (1 == find_valgt and 2 in har_valgt and 5 in har_valgt):
            print "Good job"
        elif (2 == find_valgt and 1 in har_valgt and 5 in har_valgt):
            print "Good job"
        elif (5 == find_valgt and 2 in har_valgt and 1 in har_valgt):
            print "Good job"
        else:
            print "Ikke muligt at regne"

    

root = Tk()
app = MainApp(root)

root.mainloop()

