# -*- coding: cp1252 -*-
from Tkinter import *
import math, re

#Opretter 
class MainApp():
    #Initialisere MainApp klassen, hvor den starter med at oprette en frame
    #her efter opretter den en knap, der kalder funktionen fysik
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.frame.pack()
        intro_label = Label(self.frame, text = "Hvilket emne vil du have?")
        intro_label.grid(row = 0) 
        
        self.button_fysik = Button(self.frame,text = "Fysik",
                                   command = self.fysik, width = 20, height = 2)
        self.button_fysik.grid(row = 1)

    #Opretter et nyt vindue via Fysik klassen
    def fysik(self):
        fys = Fysik(self.frame)

    #Beregner løsning på en andengradsligning på form a x^2 + b x + c = 0
    #Param a: float
    #Param b: float
    #Param c: float
    def andengrad_loeser(self, a, b, c):
        d = self.determinant(a, b, c)
        if d < 0:
            return []
        elif d == 0:
            results = [(-b) / (2 * a)]
            return results
        else:
            results = []
            results.append((-b + math.sqrt(d)) / (2 * a))
            results.append((-b - math.sqrt(d)) / (2 * a))
            return results

    #Beregner determinanten
    #Param a: float
    #Param b: float
    #Param c: float
    def determinant(self, a, b, c):
        return b**2 - 4 * a * c

    #Validerer input om det er en float
    #Param value: string
    def float_vali(self, value):
        matchObj = re.match( r'[a-z]*[A-Z]*', value, re.M|re.I)
        return not matchObj
            
        
#Klasse med beregner, der indeholder fysik
class Fysik():
    #Intialiserer Fysik klasse ved at oprette en Toplevet og en knap
    #der kalder proceduren movement_1d
    def __init__(self, parent):
        self.top = Toplevel(parent)
        msg = Message(self.top, text = "Hvad vil du beregne inden for fysik?")
        msg.grid(row = 0)

        button_kinematik = Button(self.top, text = "Bevægelse i 1D",
                                  command = self.movement_1d, width = 20,
                                  height = 2)
        button_kinematik.grid(row = 1)

    #Opretter to multi choice skemaer, hvor man kan vælge hvad information
    #man har og man ønsker at finde. Opretter så knap, så beregningen
    #kan begynde via proceduren kin_beregning
    def movement_1d(self):
        global find_list, har_list, error_message
        self.top_beregn = Toplevel(self.top)
        msg_find = Message(self.top_beregn, text = "Vælg hvad du vil finde?")
        msg_find.grid(row = 0)
        find_list = Listbox(self.top_beregn, exportselection = 0)
        find_list.grid(row = 1)
        muligheder = ["Starhastighed: v0", "Strækning: s", "Tid: t",
                      "Accelration: a", 'Startrækning: s0', 'Hastighed: v']
        for item in muligheder:
            find_list.insert(END, item)

        msg_har = Message(self.top_beregn, text = "Hvad information har du?")
        msg_har.grid(row = 0, column = 1)
        har_list = Listbox(self.top_beregn, selectmode = MULTIPLE, exportselection = 0)
        har_list.grid(row = 1, column = 1)
        for item in muligheder:
            har_list.insert(END, item)
        kin_beregning_knap = Button(self.top_beregn, text = "Test",
                                    command = self.kin_beregning)
        kin_beregning_knap.grid(row = 2)
        error_message = StringVar()
        error_message_label = Label(self.top_beregn, textvariable = error_message)
        error_message_label.grid(row = 2, column = 1)
        
        
    #Tjekker først og fremmest for om det er muligt at beregne det.
    #Er det det, så oprettes der det nødvendige antal inputfelter og knappen
    #der kalder den pågældende procedurer, der beregner svaret.
    def kin_beregning(self):
        find_valgt = map(int, find_list.curselection())[0]
        har_valgt = map(int, har_list.curselection())
        self.entry_top = Toplevel(self.top_beregn)

        #For at tjekke for formel s=0.5*a*t^2+v0*t+s0
        if (1 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            0 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.straekning_acceleration_starthastighed_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (0 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            1 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.starthastighed_acceleration_tidsq_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 3 in har_valgt and 0 in har_valgt and
            1 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.tid_acceleration_starthastighed_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 0 in har_valgt and 2 in har_valgt and
            1 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.acceleration_starthastighed_tidsq_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (4 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            1 in har_valgt and 0 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.startstraekning_acceleration_starthastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (1 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            0 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.straekning_acceleration_starthastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (0 == find_valgt and 3 in har_valgt and 2 in har_valgt and
            1 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.starthastighed_acceleration_tidsq_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 3 in har_valgt and 0 in har_valgt and
            1 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.tid_acceleration_starthastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 0 in har_valgt and 2 in har_valgt and
            1 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.acceleration_starthastighed_tidsq_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        # For at tjekke for formel v^2=v0^2+2*a*(s-s0)
        elif (5 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            3 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.hastighed_uden_tid_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (0 == find_valgt and 5 in har_valgt and 1 in har_valgt and
            3 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.starthastighed_uden_tid_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (1 == find_valgt and 0 in har_valgt and 5 in har_valgt and
            3 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.straekning_uden_tid_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            5 in har_valgt and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.acceleration_uden_tid_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (4 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            3 in har_valgt and 5 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.startstraekning_uden_tid_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (5 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.hastighed_uden_tid_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (0 == find_valgt and 5 in har_valgt and 1 in har_valgt and
            3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.starthastighed_uden_tid_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (1 == find_valgt and 0 in har_valgt and 5 in har_valgt and
            3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.straekning_uden_tid_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 0 in har_valgt and 1 in har_valgt and
            5 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.acceleration_uden_tid_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #For at tjekke for formal v = a * t + v0 i forskellige variationer
        elif (5 == find_valgt and 0 in har_valgt and 2 in har_valgt and
              3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.hastighed_acceleration_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (0 == find_valgt and 5 in har_valgt and 2 in har_valgt and
              3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.starthastighed_acceleration_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 0 in har_valgt and 5 in har_valgt and
              3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.tid_hastighed_acceleration_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 0 in har_valgt and 2 in har_valgt and
              5 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.acceleration_hastighed_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (5 == find_valgt and 2 in har_valgt and 3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.hastighed_acceleration_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 5 in har_valgt and 3 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.tid_hastighed_acceleration_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 2 in har_valgt and 5 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.acceleration_hastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #For at for formel s=t*v+s0
        elif (1 == find_valgt and 2 in har_valgt and 5 in har_valgt
              and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.straekning_hastighed_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 1 in har_valgt and 5 in har_valgt
              and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.tid_straekning_hastighed_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)           
        elif (5 == find_valgt and 2 in har_valgt and 1 in har_valgt
              and 4 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.hastighed_straekning_start_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1) 
        elif (4 == find_valgt and 2 in har_valgt and 5 in har_valgt
              and 1 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.startstraekning_hastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (1 == find_valgt and 2 in har_valgt and 5 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.straekning_hastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 1 in har_valgt and 5 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.tid_straekning_hastighed_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1) 
        elif (5 == find_valgt and 2 in har_valgt and 1 in har_valgt):
            beregn_knap = Button(self.entry_top, text = "Beregn",
                                 command = self.hastighed_straekning_beregn)
            beregn_knap.grid(row = len(har_valgt) + 1) 
        else:
            error_message.set("Ikke muligt at beregne")
            self.entry_top.destroy()
            return
            
            
        self.top_entry_op(0 in har_valgt, 1 in har_valgt, 2 in har_valgt,
                          3 in har_valgt, 4 in har_valgt, 5 in har_valgt)

    #Opretter de nødvendige input felter
    #Parem v0: boolean
    #Parem s: boolean
    #Param t: boolean
    #Parem a: boolean
    #Parem s0: boolean
    #Parem v: boolean
    def top_entry_op(self, v0, s, t, a, s0, v):
        global v0_entry, s_entry, t_entry, a_entry, s0_entry, v_entry, result_text
        row_variable = 1
        if v0:
            v0_besked = Label(self.entry_top, text = "Starthastighed: v0")
            v0_entry = Entry(self.entry_top)
            v0_entry.grid(row = row_variable, column = 1)
            v0_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if s:
            s_besked = Label(self.entry_top, text = "Strækning: s")
            s_entry = Entry(self.entry_top)
            s_entry.grid(row = row_variable, column = 1)
            s_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if t:
            t_besked = Label(self.entry_top, text = "Tid: t")
            t_entry = Entry(self.entry_top)
            t_entry.grid(row = row_variable, column = 1)
            t_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if a:
            a_besked = Label(self.entry_top, text = "Acceleration: a")
            a_entry = Entry(self.entry_top)
            a_entry.grid(row = row_variable, column = 1)
            a_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if s0:
            s0_besked = Label(self.entry_top, text = "Startstrækning: s0")
            s0_entry = Entry(self.entry_top)
            s0_entry.grid(row = row_variable, column = 1)
            s0_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if v:
            v_besked = Label(self.entry_top, text = "Hastighed: v")
            v_entry = Entry(self.entry_top)
            v_entry.grid(row = row_variable, column = 1)
            v_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        result_text = StringVar()
        result = Label(self.entry_top, textvariable = result_text)
        result.grid(row = row_variable, column = 1)
            
    #Beregner resultat ud fra input med formel s = v * t + s0
    def straekning_hastighed_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(t_entry.get()) and
            app.s0_entry.get()):
            hast = float(v_entry.get())
            tid = float(t_entry.get())
            str_nul = float(s0_entry.get())
            tal_result = hast * tid + str_nul
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel t = (s - s0) / v
    def tid_straekning_hastighed_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(s0_entry.get()) and
            app.float_vali(s_entry.get())):
            hast = float(v_entry.get())
            str_nul = float(s0_entry.get())
            stra = float(s_entry.get())
            tal_result = (stra - str_nul) / hast
            result_text.set(str(tal_result) + " s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v = (s - s0) / v
    def hastighed_straekning_start_beregn(self):
        if (app.float_vali(t_entry.get()) and app.float_vali(s0_entry.get()) and
            app.float_vali(s_entry.get())):
            tid = float(t_entry.get())
            str_nuk = float(s0_entry.get())
            stra = float(s_entry.get())
            tal_result = (stra - str_nul) / tid
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s0 = s - v * t
    def startstraekning_hastighed_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(t_entry.get()) and
            app.flaot_vali(s_entry.get())):
            hast = float(v_entry.get())
            tid = float(t_entry.get())
            stra = float(s_entry.get())
            tal_result = stra - hast * tid
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s = v * t
    def straekning_hastighed_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(t_entry.get())):
            hast = float(v_entry.get())
            tid = float(t_entry.get())
            tal_result = hast * tid
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel t = s / v
    def tid_straekning_hastighed_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(s_entry.get())):
            hast = float(v_entry.get())
            stra = float(s_entry.get())
            tal_result = (stra) / hast
            result_text.set(str(tal_result) + " s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v = s / t
    def hastighed_straekning_beregn(self):
        if (app.float_vali(t_entry.get()) and app.float_vali(s_entry.get())):
            tid = float(t_entry.get())
            stra = float(s_entry.get())
            tal_result = (stra) / tid
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v = a * t + v0
    def hastighed_acceleration_start_beregn(self):
        if (app.float_vali(t_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(hast_nul.get())):
            tid = float(t_entry.get())
            acc = float(a_entry.get())
            hast_nul = float(v0_entry.get())
            tal_result = acc * tid + hast_nul
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v0 = v - a * t
    def starthastighed_acceleration_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(t_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            tid = float(t_entry.get())
            tal_result = hast - acc * tid
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel t = (v - v0) / a
    def tid_hastighed_acceleration_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(v0_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            hast_nul = float(v0_entry.get())
            tal_result = (hast - hast_nul) / acc
            result_text.set(str(tal_result) + " s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel a = (v - v0) / t
    def acceleration_hastighed_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(t_entry.get()) and
            app.float_vali(v0_entry.get())):
            hast = float(v_entry.get())
            tid = float(t_entry.get())
            hast_nul = float(v0_entry.get())
            tal_result = (hast - hast_nul) / tid
            result_text.set(str(tal_result) + " m/s^2")
        else:
            result_text.set("Dårligt input")
        
     #Beregner resultat ud fra input med formel v = a * t
    def hastighed_acceleration_beregn(self):
        if (app.float_vali(t_entry.get()) and app.float_vali(a_entry.get())):
            tid = float(t_entry.get())
            acc = float(a_entry.get())
            tal_result = acc * tid
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel t = v / a
    def tid_hastighed_acceleration_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            tal_result = hast / acc
            result_text.set(str(tal_result) + " s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel a = v / t
    def acceleration_hastighed_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(t_entry.get())):
            hast = float(v_entry.get())
            tid = float(t_entry.get())
            tal_result = hast / tid
            result_text.set(str(tal_result) + " m/s^2")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v = sqrt(v0^2 + 2 * a * (s - s0))
    def hastighed_uden_tid_start_beregn(self):
        if (app.float_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(s_entry.get()) and app.float_vali(s0_entry.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            stra = float(s_entry.get())
            stra_nul = float(s0_entry.get())
            tal_result = math.sqrt(abs(hast_nul**2 + 2 * acc * (stra - stra_nul)))
            if hast_nul**2 + 2 * acc * (stra - stra_nul) < 0:
                result_text.set("-" + str(tal_result) + " m/s")
            else:
                result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v0 = sqrt(v^2 - 2 * a * (s - s0))
    def starthastighed_uden_tid_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.flaot_vali(a_entry.get()) and
            app.float_vali(s_entry.get()) and app.flaot_vali(s0_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            stra = float(s_entry.get())
            stra_nul = float(s0_entry.get())
            tal_result = math.sqrt(abs(hast**2 - 2 * acc * (stra - stra_nul)))
            if hast**2 - 2 * acc * (stra - stra_nul) < 0:
                result_text.set("-" + str(tal_result) + " m/s")
            else:
                result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s = ((v^2 - v0^2) / (2 * a)) + s0
    def straekning_uden_tid_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(v0_entry.get()) and app.float_vali(s0_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            hast_nul = float(v0_entry.get())
            stra_nul = float(s0_entry.get())
            tal_result = ((hast**2 - hast_nul**2) / 2 * acc) + stra_nul
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel a = (v^2 - v0^2) / (2 * (s - s0))
    def acceleration_uden_tid_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(s_entry.get()) and
            app.float_vali(v0_entry.get()) and app.float_vali(s0_entry.get())):
            hast = float(v_entry.get())
            stra = float(s_entry.get())
            hast_nul = float(v0_entry.get())
            stra_nul = float(s0_entry.get())
            if stra - stra_nul == 0:
                result_text.set(str(0) + " m/s^2")
            else:
                tal_result = (hast**2 - hast_nul**2) / (2 * (stra - stra_nul))
                result_text.set(str(tal_result) + " m/s^2")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s0 = s - ((v^2 - v0^2) / (2 * a))
    def startstraekning_uden_tid_start_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(v0_entry.get()) and app.flaot_vali(s_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            hast_nul = float(v0_entry.get())
            stra = float(s_entry.get())
            tal_result = stra - ((hast**2 - hast_nul**2) / 2 * acc)
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v = sqrt(v0^2 + 2 * a * s)
    def hastighed_uden_tid_beregn(self):
        if (app.flaot_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(s_entry.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            stra = float(s_entry.get())
            tal_result = math.sqrt(abs(hast_nul**2 + 2 * acc * stra))
            if hast_nul**2 + 2 * acc * stra < 0:
                result_text.set("-" + str(tal_result) + " m/s")
            else:
                result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v0 = sqrt(v^2 - 2 * a * s)
    def starthastighed_uden_tid_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(s_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            stra = float(s_entry.get())
            tal_result = math.sqrt(abs(hast**2 - 2 * acc * stra))
            if hast**2 - 2 * acc * stra < 0:
                result_text.set("-" + str(tal_result) + " m/s")
            else:
                result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s = ((v^2 - v0^2) / (2 * a))
    def straekning_uden_tid_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(v0_entry.get())):
            hast = float(v_entry.get())
            acc = float(a_entry.get())
            hast_nul = float(v0_entry.get())
            tal_result = ((hast**2 - hast_nul**2) / 2 * acc)
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel a = (v^2 - v0^2) / (2 * s)
    def acceleration_uden_tid_beregn(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(s_entry.get()) and
            app_float_vali(v0_entry.get())):
            hast = float(v_entry.get())
            stra = float(s_entry.get())
            hast_nul = float(v0_entry.get())
            tal_result = (hast**2 - hast_nul**2) / (2 * (stra))
            result_text.set(str(tal_result) + " m/s^2")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med andengradsløsning for t i formel
    #a * t^2 + v0 * t + (s0 - s) = 0
    def tid_acceleration_starthastighed_start_beregn(self):
        if (app.float_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(s_entry.get()) and app.float_vali(s0_entry.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            stra = float(s_entry.get())
            stra_nul = float(s0_entry.get())
            list_result = app.andengrad_loeser(acc, hast_nul, stra_nul - stra)
            if len(list_result) > 0:
                if len(list_result) == 1:
                    result_text.set(str(list_result[0]) + " s")
                else:
                    if list_result[0] > list_result[1]:
                        result_text.set(str(list_result[0]) + " s")
                    else:
                        result_text.set(str(list_result[1]) + " s")
            else:
                result_text.set("Ikke muligt at regne")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med andengradsløsning for t i formel
    #a * t^2 + v0 * t - s = 0
    def tid_acceleration_starthastighed_beregn(self):
        if (app.float_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(s_entre.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            stra = float(s_entry.get())
            list_result = app.andengrad_loeser(acc, hast_nul, - stra)
            if len(list_result) > 0:
                if len(list_result) == 1:
                    result_text.set(str(list_result[0]) + " s")
                else:
                    if list_result[0] > list_result[1]:
                        result_text.set(str(list_result[0]) + " s")
                    else:
                        result_text.set(str(list_result[1]) + " s")
            else:
                result_text.set("Ikke muligt at regne")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s = 0.5 * a * t^2 + v0 * t + s0
    def straekning_acceleration_starthastighed_start_beregn(self):
        if (app.float_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(t_entry.get()) and app.float_vali(s0_entry.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            tid = float(t_entry.get())
            stra_nul = float(s0_entry.get())
            tal_result = 0.5 * acc * tid**2 + hast_nul * tid + stra_nul
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")
        
    #Beregner resultat ud fra input med formel s = 0.5 * a * t^2 + v0 * t
    def straekning_acceleration_starthastighed_beregn(self):
        if (app.float_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(t_entry.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            tid = float(t_entry.get())
            tal_result = 0.5 * acc * tid**2 + hast_nul * tid
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v0 = (s - s0 - a * t^2) / t
    def starthastighed_acceleration_tidsq_start_beregn(self):
        if (app.float_vali(s_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(t_entry.get()) and app.float_vali(s0_entry.get())):
            stra = float(s_entry.get())
            acc = float(a_entry.get())
            tid = float(t_entry.get())
            stra_nul = float(s0_entry.get())
            tal_result = (stra - stra_nul - acc * tid**2) / tid
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel v0 = (s - a * t^2) / t
    def starthastighed_acceleration_tidsq_beregn(self):
        if (app.float_vali(s_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(t_entry.get())):
            stra = float(s_entry.get())
            acc = float(a_entry.get())
            tid = float(t_entry.get())
            tal_result = (stra - acc * tid**2) / tid
            result_text.set(str(tal_result) + " m/s")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel a = (s - s0 - v0 * t) / t^2
    def acceleration_starthastighed_tidsq_start_beregn(self):
        if (app.float_vali(s_entry.get()) and app.float_vali(v0_entry.get()) and
            app.float_vali(t_entry.get()) and app.float_vali(s0_entry.get())):
            stra = float(s_entry.get())
            hast_nul = float(v0_entry.get())
            tid = float(t_entry.get())
            stra_nul = float(s0_entry.get())
            tal_result = (stra - stra_nul - hast_nul * tid) / tid**2
            result_text.set(str(tal_result) + " m/s^2")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel a = (s - v0 * t) / t^2
    def acceleration_starthastighed_tidsq_beregn(self):
        if (app.float_vali(s_entry.get()) and app.float_vali(v0_entry.get()) and
            app.float_vali(t_entry.get())):
            stra = float(s_entry.get())
            hast_nul = float(v0_entry.get())
            tid = float(t_entry.get())
            tal_result = (stra - hast_nul * tid) / tid**2
            result_text.set(str(tal_result) + " m/s^2")
        else:
            result_text.set("Dårligt input")

    #Beregner resultat ud fra input med formel s0 = s - 0.5 * a * t^2 + v0 * t
    def startstraekning_acceleration_starthastighed_beregn(self):
        if (app.float_vali(v0_entry.get()) and app.float_vali(a_entry.get()) and
            app.float_vali(t_entry.get()) and app.float_vali(s_entry.get())):
            hast_nul = float(v0_entry.get())
            acc = float(a_entry.get())
            tid = float(t_entry.get())
            stra = float(s_entry.get())
            tal_result = stra - 0.5 * acc * tid**2 - hast_nul * tid
            result_text.set(str(tal_result) + " m")
        else:
            result_text.set("Dårligt input")
        
 
root = Tk()
app = MainApp(root)
root.mainloop()
