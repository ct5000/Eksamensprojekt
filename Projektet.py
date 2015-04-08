# -*- coding: cp1252 -*-
'''
Dette program er designet til at kunne beregne forskellige udregninger,
dog er det indtil videre kun muligt at beregne bevægelse i 1 dimension.
Der er ikke ret mange loops i koden, men dette skyldes, at der er blevet
anvendt event-driven programming, hvor en knap kan kalde en funktion flere
gange, så det er ikke på samme måde nødvendigt at bruge loops til at få
funktionaliteten til at kunne gentages med flere forskellige input.
Forløbet i programmet er, at man trykker på en knap, hvor man vælger, hvad
man vil beregne. Herefter kommer man indtil det emne, som man har valgt, og her
kan man vælge blandt forskellige regnemuligheder inden for dette emne. Så kommer
man indtil det man har valgt, og her kan man vælge, hvad man allerede ved og
hvad man vil finde. Så, hvis det er muligt at beregne, kommer man til et nyt
vindue, hvor man skal indtaste det information man har. Det beregnes så, men
først så tjekkes der om det er et ordentligt input, der er blevet givet.
'''
from Tkinter import *
import math, re, operator

#Opretter 
class MainApp():
    #Initialisere MainApp klassen, hvor den starter med at oprette en frame
    #her efter opretter den en knap, der kalder funktionen fysik
    def __init__(self, parent):
        self.frame = Frame(parent, padx = 6, pady = 6)
        self.frame.pack()
        intro_label = Label(self.frame, text = "Hvilket emne vil du have?")
        intro_label.grid(row = 0) 
        self.button_fysik = Button(self.frame,text = "Fysik",
                                   command = self.fysik, width = 20, height = 2)
        self.button_fysik.grid(row = 1)
        self.button_matematik = Button(self.frame, text = "Matematik",
                                       command = self.matematik, width = 20,
                                       height = 2)
        self.button_matematik.grid(row = 2)
        self.button_skrivning = Button(self.frame, text = "Skrivning",
                                       command = self.skrivning, width = 20,
                                       height = 2)
        self.button_skrivning.grid(row = 3)
        
        menubar = Menu(self.frame)
        menubar.add_command(label = "Quit", command = parent.destroy)
        parent.config(menu = menubar)

    #Opretter et nyt vindue via Fysik klassen
    def fysik(self):
        fys = Fysik(self.frame)

    def matematik(self):
        mat = Matematik(self.frame)

    def skrivning(self):
        skriv = Skrivning(self.frame)
    
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
        matchObj = re.findall(r'^-?[0-9]+\.?[0-9]?$', value)
        return matchObj

class Skrivning():
    def __init__(self, parent):
        self.top = Toplevel(parent)
        msg = Message(self.top, text = "Hvad vil du vide inden for skrivning")
        msg.grid(row = 0)
        button_count = Button(self.top, text = "Mest brugte ord",
                              command = self.most_used_words, width = 20,
                              height = 2)
        button_count.grid(row = 1)

    def most_used_words(self):
        global sti_entry, most_words, word_graph
        self.word_count = Toplevel(self.top)
        text_msg = """Indtast stien til den txt fil, du vil have tjekket, på følgende
form c:/mappe/mappe/fil"""
        word_count_msg = Message(self.word_count, text = text_msg, width = 250)
        word_count_msg.grid(row = 0, column = 0, columnspan = 2)
        sti_label = Label(self.word_count, text = "Sti")
        sti_label.grid(row = 1)
        sti_entry = Entry(self.word_count, width = 40)
        sti_entry.grid(row = 1, column = 1)
        count_words_button = Button(self.word_count, text = "Tæl",
                                    command = self.count_words)
        count_words_button.grid(row = 2, column = 1)
        used_words_label = Label(self.word_count, text = "5 mest brugte ord og antal gange brugt")
        used_words_label.grid(row = 3)
        most_words = StringVar()
        most_words_text = Label(self.word_count, textvariable = most_words)
        most_words_text.grid(row = 3, column = 1)
        word_graph = Canvas(self.word_count, width = 600, height = 400, bg="gray")
        word_graph.grid(row = 4, columnspan = 2)
        word_graph.create_line((35, 25), (35, 375), fill = "black")
        word_graph.create_line((35,375), (585, 375), fill = "black")

    def count_words(self):
        global most_words, word_graph
        try:
            stien = sti_entry.get()
            count_file = open(stien, "r")
            count_text = count_file.read()
            count_text = count_text.lower()
            words = re.split(r'[ ^|^,|^.]+', count_text)
            wordcount = {}
            for w in words:
                if not (w in wordcount.keys()):
                    wordcount[w] = 1
                else:
                    wordcount[w] += 1
            sorted_wordcount = sorted(wordcount.items(), key = operator.itemgetter(1))
            sorted_wordcount.reverse()
            most_words.set(sorted_wordcount[0][0] + ": " +
                           str(sorted_wordcount[0][1]) + ", " +
                           sorted_wordcount[1][0] + ": " +
                           str(sorted_wordcount[1][1]) + ", " +
                           sorted_wordcount[2][0] + ": " +
                           str(sorted_wordcount[2][1]) + ", " +
                           sorted_wordcount[3][0] + ": " +
                           str(sorted_wordcount[3][1]) + " og " +
                           sorted_wordcount[4][0] + ": " +
                           str(sorted_wordcount[4][1])) 
            y_axistal = sorted_wordcount[0][1] / 4.0
            pillar_num = 275.0 / sorted_wordcount[0][1]
            word_graph.create_text((18, 325), text = str(y_axistal))
            word_graph.create_text((18, 250), text = str(y_axistal * 2))
            word_graph.create_text((18, 175), text = str(y_axistal * 3))
            word_graph.create_text((18, 100), text = str(y_axistal * 4))
            word_graph.create_text((60, 388), text = sorted_wordcount[0][0])
            word_graph.create_text((110, 388), text = sorted_wordcount[1][0])
            word_graph.create_text((160, 388), text = sorted_wordcount[2][0])
            word_graph.create_text((210, 388), text = sorted_wordcount[3][0])
            word_graph.create_text((260, 388), text = sorted_wordcount[4][0])
            word_graph.create_text((310, 388), text = sorted_wordcount[5][0])
            word_graph.create_text((360, 388), text = sorted_wordcount[6][0])
            word_graph.create_text((410, 388), text = sorted_wordcount[7][0])
            word_graph.create_text((460, 388), text = sorted_wordcount[8][0])
            word_graph.create_text((510, 388), text = sorted_wordcount[9][0])
            word_graph.create_text((560, 388), text = sorted_wordcount[10][0])
            for i in range(11):
                word_graph.create_rectangle((55 + i * 50, 375),
                                            (65 + i * 50, 375 -
                                             sorted_wordcount[i][1]* pillar_num),
                                            fill = "red")
            count_file.close()
            
        except:
            most_words.set("Kan ikke finde stien")            
       
class Matematik():
    def __init__(self, parent):
        self.top = Toplevel(parent)
        msg = Message(self.top, text = "Hvad vil de beregne inden for matematik?")
        msg.grid(row = 0)
        button_parabel = Button(self.top, text = "Parabel", command =
                                self.parabel_vindue, width = 20, height = 2)
        button_parabel.grid(row = 1)
        matmenu = Menu(self.top)

    def parabel_vindue(self):
        global ap_entry, b_entry, c_entry, top_result, rod_result
        self.top_beregn = Toplevel(self.top)
        msg_parabel = Message(self.top_beregn, text = "Indtast værdier, når din\
                                funktion er på formen ax^2+bx+c=0", width = 250)
        msg_parabel.grid(row = 0, column= 0, columnspan = 2)
        a_besked = Label(self.top_beregn, text = "a", width = 20)
        ap_entry = Entry(self.top_beregn)
        a_besked.grid(row = 1)
        ap_entry.grid(row = 1, column = 1)
        b_besked = Label(self.top_beregn, text = "b", width = 20)
        b_entry = Entry(self.top_beregn)
        b_besked.grid(row = 2)
        b_entry.grid(row = 2, column = 1)
        c_besked = Label(self.top_beregn, text = "c", width = 20)
        c_entry = Entry(self.top_beregn)
        c_besked.grid(row = 3)
        c_entry.grid(row = 3, column = 1)
        button_beregn_para = Button(self.top_beregn, text = "Beregn", command =
                                    self.parabel_beregner)
        button_beregn_para.grid(row = 4, column = 1)
        rod_text = Label(self.top_beregn, text = "Rødder")
        top_text = Label(self.top_beregn, text = "Toppunkt")
        rod_result = StringVar()
        top_result = StringVar()
        roedder = Label(self.top_beregn, textvariable = rod_result)
        toppunkt = Label(self.top_beregn, textvariable = top_result)
        rod_text.grid(row = 5)
        roedder.grid(row = 5, column = 1)
        top_text.grid(row = 6)
        toppunkt.grid(row = 6, column = 1)
          
    def parabel_beregner(self):
        if (app.float_vali(ap_entry.get()) and app.float_vali(b_entry.get()) and
            app.float_vali(c_entry.get())):
            a = float(ap_entry.get())
            b = float(b_entry.get())
            c = float(c_entry.get())
            rod = app.andengrad_loeser(a, b, c)
            if len(rod) > 0:
                if len(rod) == 1:
                    rod_result.set("x = " + str(rod[0]))
                else:
                    rod_result.set("x = " + str(rod[0]) + "og x = " + str(rod[1]))
            else:
                rod_result.set("Ingen rødder")
            toppunkt = self.toppunkt_beregn(a, b, c)
            top_result.set(str(toppunkt))

            
        else:
            top_result.set("Dårligt input")

    def toppunkt_beregn(self, a, b, c):
        determinant = app.determinant(a, b, c)
        return ((-b) / (2 * a), ((-determinant) / (4 * a)))
        
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
        button_energi = Button(self.top, text = "Energi", command = self.energi,
                               width = 20, height = 2)
        button_energi.grid(row = 2)

    def energi(self):
        global error_message_energi, find_list_energi, har_list_energi
        self.top_energi = Toplevel(self.top)
        msg_findenergi = Message(self.top_energi, text = "Vælg hvad du vil finde")
        msg_harenergi = Message(self.top_energi, text = "Vælg hvad du har")
        msg_findenergi.grid(row = 0)
        msg_harenergi.grid(row = 0, column = 1)
        muligheder_energi = ["Energi, E [J]", "Varmeenergi, Q [J]", "Arbejde, A [J]",
                             "Masse, m [kg]", "Specifik varmekapacitet, c [J/(kg * K)]",
                             "Temperaturstigning, deltaT [K]", "Hastighed, v [m/s]",
                             "Højde, h [m]", "Energi kinetisk, Ekin [J]",
                             "Energi potetiel, Epot [J]", "Energi mekanisk, Emek [J]",
                             "Kraft, F [N]", "Fjedrekonstant, k [N/m]", 
                             "Fjedre forlængelse, x [m]", "Strømstyrke, I [A]",
                             "Spændingsfald, U [V]", "Modstand, R [Ohm]",
                             "Effekt, P [W]", "Tid, t [s]", "Vinkel, alpha [Grader]",
                             "Strækning, s[m]"]
        find_list_energi = Listbox(self.top_energi, exportselection = 0,
                                   height = 22, width = 35)
        har_list_energi = Listbox(self.top_energi, selectmode = MULTIPLE,
                                  exportselection = 0, height = 22, width = 35)
        find_list_energi.grid(row = 1)
        har_list_energi.grid(row = 1, column = 1)
        for item in muligheder_energi:
            find_list_energi.insert(END, item)
            har_list_energi.insert(END, item)
        beregn_energi_button = Button(self.top_energi, text = "Beregn",
                                      command = self.energi_beregningen)
        beregn_energi_button.grid(row = 2, column = 1, sticky = E)
        error_message_energi = StringVar()
        error_energi_label = Label(self.top_energi,
                                   textvariable = error_message_energi)
        error_energi_label.grid(row = 3)

    def energi_beregningen(self):
        find_valgt = map(int, find_list_energi.curselection())[0]
        har_valgt = map(int, har_list_energi.curselection())
        self.entry_top_energi = Toplevel(self.top_energi)
        #Check for beregninger indenfor E = A + Q
        if (0 == find_valgt and 1 in har_valgt and 2 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.energi_arbejde_varme)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (1 == find_valgt and 2 in har_valgt and 0 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.varme_energi_arbejde)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (2 == find_valgt and 0 in har_valgt and 1 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.arbejde_energi_varme)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #Check for beregninger indenfor A = F * s * cos(alpha)
        elif (2 == find_valgt and 11 in har_valgt and 19 in har_valgt
              and 20 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.arbejde_kraft_straek_vinkel)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (11 == find_valgt and 2 in har_valgt and 19 in har_valgt
              and 20 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.kraft_arbejde_straek_vinkel)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (19 == find_valgt and 2 in har_valgt and 11 in har_valgt
              and 20 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.vinkel_arbejde_straek_kraft)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (20 == find_valgt and 2 in har_valgt and 11 in har_valgt
              and 19 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.straek_arbejde_vinkel_kraft)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #Check for beregning indenfor A = -0.5 * k * x^2
        elif (2 == find_valgt and 12 in har_valgt and 13 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.arbejde_fjederk_presset)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (12 == find_valgt and 2 in har_valgt and 13 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.fjederk_arbejde_presset)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (13 == find_valgt and 2 in har_valgt and 12 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.presset_fjederk_arbejde)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #Check for beregning indenfor E = P * t
        elif (0 == find_valgt and 17 in har_valgt and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.energi_effekt_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (17 == find_valgt and 0 in har_valgt and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.effekt_energi_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (18 == find_valgt and 0 in har_valgt and 17 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.tid_effekt_energi)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #Check for beregning indenfor E = U * I * t
        elif (0 == find_valgt and 14 in har_valgt and 15 in har_valgt
              and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.energi_styrke_spaending_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (14 == find_valgt and 0 in har_valgt and 15 in har_valgt
              and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.styrke_energi_spaending_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (15 == find_valgt and 0 in har_valgt and 14 in har_valgt
              and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.spaending_energi_styrke_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (18 == find_valgt and 0 in har_valgt and 14 in har_valgt
              and 15 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.tid_spaending_energi_styrke)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #Check for beregning indenfor E = R * I^2 * t
        elif (0 == find_valgt and 14 in har_valgt and 16 in har_valgt
              and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.energi_modstand_styrke_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (14 == find_valgt and 0 in har_valgt and 16 in har_valgt
              and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.styrke_modstand_energi_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (16 == find_valgt and 0 in har_valgt and 14 in har_valgt
              and 18 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.modstand_styrke_energi_tid)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (18 == find_valgt and 0 in har_valgt and 14 in har_valgt
              and 16 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.tid_modstand_styrke_energi)
            beregn_knap.grid(row = len(har_valgt) + 1)
        #Check for beregning indenfor Ekin = 0.5 * m * v^2
        elif (8 == find_valgt and 6 in har_valgt and 3 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.kinenergi_masse_hastighed)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (6 == find_valgt and 8 in har_valgt and 3 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.hastighed_kinenergi_masse)
            beregn_knap.grid(row = len(har_valgt) + 1)
        elif (3 == find_valgt and 8 in har_valgt and 6 in har_valgt):
            beregn_knap = Button(self.entry_top_energi, text = "Beregn",
                                 command = self.masse_hastighed_kinenergi)
            beregn_knap.grid(row = len(har_valgt) + 1)
        else:
            error_message_energi.set("Ikke muligt at beregne")
            self.entry_top_energi.destroy()      
            return
        entry_top_message = Label(self.entry_top_energi,
                                  text = "Indtast tal som decimaltal")
        entry_top_message.grid(row = 0)
        self.energi_entry_op(0 in har_valgt, 1 in har_valgt, 2 in har_valgt,
                             3 in har_valgt, 4 in har_valgt, 5 in har_valgt,
                             6 in har_valgt, 7 in har_valgt, 8 in har_valgt,
                             9 in har_valgt, 10 in har_valgt, 11 in har_valgt,
                             12 in har_valgt, 13 in har_valgt, 14 in har_valgt,
                             15 in har_valgt, 16 in har_valgt, 17 in har_valgt,
                             18 in har_valgt, 19 in har_valgt, 20 in har_valgt)
        
        

    def energi_entry_op(self, E, Q, A, m, c, deltaT, v, h, Ekin, Epot, Emek, F, k,
                        x, I, U, R, P, t, alpha, s):
        global E_entry, Q_entry, A_entry, m_entry, F_entry, energi_result_text
        global c_entry, deltaT_entry, v_entry, h_entry, Ekin_entry, Epot_entry
        global Emek_entry, k_entry, x_entry, I_entry, U_entry, R_entry, P_entry
        global t_entry, alpha_entry, s_entry
        row_variable = 1
        if E:
            E_besked = Label(self.entry_top_energi, text = "Energi: E")
            E_entry = Entry(self.entry_top_energi)
            E_entry.grid(row = row_variable, column = 1)
            E_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if Q:
            Q_besked = Label(self.entry_top_energi, text = "Varmeenergi: Q")
            Q_entry = Entry(self.entry_top_energi)
            Q_entry.grid(row = row_variable, column = 1)
            Q_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if A:
            A_besked = Label(self.entry_top_energi, text = "Arbejde: A")
            A_entry = Entry(self.entry_top_energi)
            A_entry.grid(row = row_variable, column = 1)
            A_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if m:
            m_besked = Label(self.entry_top_energi, text = "Masse: m")
            m_entry = Entry(self.entry_top_energi)
            m_entry.grid(row = row_variable, column = 1)
            m_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if c:
            c_besked = Label(self.entry_top_energi, text = "Specifikvarmekapacitet: c")
            c_entry = Entry(self.entry_top_energi)
            c_entry.grid(row = row_variable, column = 1)
            c_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if deltaT:
            deltaT_besked = Label(self.entry_top_energi, text = "Temperatur ændring: deltaT")
            deltaT_entry = Entry(self.entry_top_energi)
            deltaT_entry.grid(row = row_variable, column = 1)
            deltaT_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if v:
            v_besked = Label(self.entry_top_energi, text = "Hastighed: v")
            v_entry = Entry(self.entry_top_energi)
            v_entry.grid(row = row_variable, column = 1)
            v_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if h:
            h_besked = Label(self.entry_top_energi, text = "Højde: h")
            h_entry = Entry(self.entry_top_energi)
            h_entry.grid(row = row_variable, column = 1)
            h_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if Ekin:
            Ekin_besked = Label(self.entry_top_energi, text = "Kinetisk energi: Ekin")
            Ekin_entry = Entry(self.entry_top_energi)
            Ekin_entry.grid(row = row_variable, column = 1)
            Ekin_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if Epot:
            Epot_besked = Label(self.entry_top_energi, text = "Potentiel energi: Epot")
            Epot_entry = Entry(self.entry_top_energi)
            Epot_entry.grid(row = row_variable, column = 1)
            Epot_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if Emek:
            Emek_besked = Label(self.entry_top_energi, text = "Mekanisk energi: Emek")
            Emek_entry = Entry(self.entry_top_energi)
            Emek_entry.grid(row = row_variable, column = 1)
            Emek_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if F:
            F_besked = Label(self.entry_top_energi, text = "Kraft: F")
            F_entry = Entry(self.entry_top_energi)
            F_entry.grid(row = row_variable, column = 1)
            F_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if k:
            k_besked = Label(self.entry_top_energi, text = "Fjederkonstant: k")
            k_entry = Entry(self.entry_top_energi)
            k_entry.grid(row = row_variable, column = 1)
            k_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if x:
            x_besked = Label(self.entry_top_energi, text = "Fjedre forlængelse: x")
            x_entry = Entry(self.entry_top_energi)
            x_entry.grid(row = row_variable, column = 1)
            x_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if I:
            I_besked = Label(self.entry_top_energi, text = "Strømstyrke: I")
            I_entry = Entry(self.entry_top_energi)
            I_entry.grid(row = row_variable, column = 1)
            I_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if U:
            U_besked = Label(self.entry_top_energi, text = "Spændingsfald: U")
            U_entry = Entry(self.entry_top_energi)
            U_entry.grid(row = row_variable, column = 1)
            U_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if R:
            R_besked = Label(self.entry_top_energi, text = "Modstand: R")
            R_entry = Entry(self.entry_top_energi)
            R_entry.grid(row = row_variable, column = 1)
            R_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if P:
            P_besked = Label(self.entry_top_energi, text = "Effekt: P")
            P_entry = Entry(self.entry_top_energi)
            P_entry.grid(row = row_variable, column = 1)
            P_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if t:
            t_besked = Label(self.entry_top_energi, text = "Tid: t")
            t_entry = Entry(self.entry_top_energi)
            t_entry.grid(row = row_variable, column = 1)
            t_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if alpha:
            alpha_besked = Label(self.entry_top_energi, text = "Vinkel: alpha")
            alpha_entry = Entry(self.entry_top_energi)
            alpha_entry.grid(row = row_variable, column = 1)
            alpha_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        if s:
            s_besked = Label(self.entry_top_energi, text = "Strækning: s")
            s_entry = Entry(self.entry_top_energi)
            s_entry.grid(row = row_variable, column = 1)
            s_besked.grid(row = row_variable, column = 0)
            row_variable += 1
        energi_result_text = StringVar()
        energi_result = Label(self.entry_top_energi,
                              textvariable = energi_result_text)
        energi_result.grid(row = row_variable, column = 1)

    #Beregner resultat ud fra formel E = A + Q    
    def energi_arbejde_varme(self):
        if (app.float_vali(A_entry.get()) and app.float_vali(Q_entry.get())):
            Q = float(Q_entry.get())
            A = float(A_entry.get())
            result = Q + A
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel A = E - Q
    def arbejde_energi_varme(self):
        if (app.float_vali(E_entry.get()) and app.float_vali(Q_entry.get())):
            Q = float(Q_entry.get())
            E = float(E_entry.get())
            result = E - Q
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel Q = E - A
    def varme_energi_arbejde(self):
        if (app.float_vali(E_entry.get()) and app.float_vali(A_entry.get())):
            E = float(E_entry.get())
            A = float(A_entry.get())
            result = E - A
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel A = F * s * cos(alpha)
    def arbejde_kraft_straek_vinkel(self):
        if (app.float_vali(F_entry.get()) and app.float_vali(s_entry.get())
            and app.float_vali(alpha_entry.get())):
            F = float(F_entry.get())
            s = float(s_entry.get())
            alpha = math.radians(float(alpha_entry.get()))
            result = F * s * math.cos(alpha)
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel F = A / (s * cos(alpha))
    def kraft_arbejde_straek_vinkel(self):
        if (app.float_vali(A_entry.get()) and app.float_vali(s_entry.get())
            and app.float_vali(alpha_entry.get())):
            A = float(A_entry.get())
            s = float(s_entry.get())
            alpha = math.radians(float(alpha_entry.get()))
            result = A / (s * math.cos(alpha))
            energi_result_text.set(str(result) + " N")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel alpha = acos(A / (F * s))
    def vinkel_arbejde_straek_kraft(self):
        try:
            if (app.float_vali(A_entry.get()) and app.float_vali(s_entry.get())
                and app.float_vali(F_entry.get())):
                A = float(A_entry.get())
                s = float(s_entry.get())
                F = float(F_entry.get())
                result = math.degrees(math.acos(A / (s * F)))
                energi_result_text.set(str(result))
            else:
                energi_result_text.set("Dårligt input")
        except ValueError:
            energi_result_text.set("Udenfor Dm af acos")

    #Beregner resultat ud fra formel s = A / (F * cos(alpha))
    def straek_arbejde_vinkel_kraft(self):
        if (app.float_vali(A_entry.get()) and app.float_vali(F_entry.get())
            and app.float_vali(alpha_entry.get())):
            A = float(A_entry.get())
            F = float(F_entry.get())
            alpha = math.radians(float(alpha_entry.get()))
            result = A / (F * math.cos(alpha))
            energi_result_text.set(str(result) + " m")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel A = -0.5 * k * x^2
    def arbejde_fjederk_presset(self):
        if (app.float_vali(k_entry.get()) and app.float_vali(x_entry.get())):
            k = float(k_entry.get())
            x = float(x_entry.get())
            result = 0.5 * k * x**2
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel k = A / (-0.5 * x^2)
    def fjederk_arbejde_presset(self):
        if (app.float_vali(A_entry.get()) and app.float_vali(x_entry.get())):
            A = float(A_entry.get())
            x = float(x_entry.get())
            result = A / (0.5 * x**2)
            energi_result_text.set(str(result) + " N/m")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel x = sqrt(A / (-0.5 * k))
    def presset_fjederk_arbejde(self):
        if (app.float_vali(A_entry.get()) and app.float_vali(k_entry.get())):
            A = float(A_entry.get())
            k = float(k_entry.get())
            result = math.sqrt(A / (0.5 * k))
            energi_result_text.set(str(result) + " m")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel E = P * t
    def energi_effekt_tid(self):
        if (app.float_vali(P_entry.get()) and app.float_vali(t_entry.get())):
            P = float(P_entry.get())
            t = float(t_entry.get())
            result = P * t
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel P = E / t
    def effekt_energi_tid(self):
        if (app.float_vali(E_entry.get()) and app.float_vali(t_entry.get())):
            E = float(E_entry.get())
            t = float(t_entry.get())
            result = E / t
            energi_result_text.set(str(result) + " W")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel t = E / P
    def tid_effekt_energi(self):
        if (app.float_vali(E_entry.get()) and app.float_vali(P_entry.get())):
            E = float(E_entry.get())
            P = float(P_entry.get())
            result = E / P
            energi_result_text.set(str(result) + " s")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel E = U * I * t
    def energi_styrke_spaending_tid(self):
        if (app.float_vali(U_entry.get()) and app.float_vali(t_entry.get())
            and app.float_vali(I_entry.get())):
            U = float(U_entry.get())
            I = float(I_entry.get())
            t = float(t_entry.get())
            result = U * I * t
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel I = E / (U * t)
    def styrke_energi_spaending_tid(self):
        if (app.float_vali(U_entry.get()) and app.float_vali(t_entry.get())
            and app.float_vali(E_entry.get())):
            U = float(U_entry.get())
            E = float(E_entry.get())
            t = float(t_entry.get())
            result = E / (U * t)
            energi_result_text.set(str(result) + " A")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel U = E / (I * t)
    def spaending_energi_styrke_tid(self):
        if (app.float_vali(I_entry.get()) and app.float_vali(t_entry.get())
            and app.float_vali(E_entry.get())):
            I = float(I_entry.get())
            E = float(E_entry.get())
            t = float(t_entry.get())
            result = E / (I * t)
            energi_result_text.set(str(result) + " V")
        else:
            energi_result_text.set("Dårligt input")
            
    #Beregner resultat ud fra formel t = E / (U * I)
    def tid_spaending_energi_styrke(self):
        if (app.float_vali(I_entry.get()) and app.float_vali(U_entry.get())
            and app.float_vali(E_entry.get())):
            I = float(I_entry.get())
            E = float(E_entry.get())
            U = float(U_entry.get())
            result = E / (I * U)
            energi_result_text.set(str(result) + " s")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel E = R * I^2 * t
    def energi_modstand_styrke_tid(self):
        if (app.float_vali(R_entry.get()) and app.float_vali(t_entry.get())
            and app.float_vali(I_entry.get())):
            R = float(R_entry.get())
            I = float(I_entry.get())
            t = float(t_entry.get())
            result = R * I**2 * t
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel I = sqrt(E / (R * t))
    def styrke_modstand_energi_tid(self):
        if (app.float_vali(R_entry.get()) and app.float_vali(t_entry.get())
            and app.float_vali(E_entry.get())):
            R = float(R_entry.get())
            E = float(E_entry.get())
            t = float(t_entry.get())
            result = math.sqrt(E / (R * t))
            energi_result_text.set(str(result) + " A")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel R = E / (I^2 * t)
    def modstand_styrke_energi_tid(self):
        if (app.float_vali(I_entry.get()) and app.float_vali(t_entry.get())
            and app.float_vali(E_entry.get())):
            I = float(I_entry.get())
            E = float(E_entry.get())
            t = float(t_entry.get())
            result = E / (I**2 * t)
            energi_result_text.set(str(result) + " Ohm")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel t = E / (I^2 * R)
    def tid_modstand_styrke_energi(self):
        if (app.float_vali(I_entry.get()) and app.float_vali(R_entry.get())
            and app.float_vali(E_entry.get())):
            I = float(I_entry.get())
            E = float(E_entry.get())
            R = float(R_entry.get())
            result = E / (I**2 * R)
            energi_result_text.set(str(result) + " s")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel Ekin = 0.5 * m * v^2
    def kinenergi_masse_hastighed(self):
        if (app.float_vali(m_entry.get()) and app.float_vali(v_entry.get())):
            m = float(m_entry.get())
            v = float(v_entry.get())
            result = 0.5 * m * v**2
            energi_result_text.set(str(result) + " J")
        else:
            energi_result_text.set("Dårligt input")

    #Beregner resultat ud fra formel v = sqrt(Ekin / (0.5 * m))
    def hastighed_kinenergi_masse(self):
        if (app.float_vali(m_entry.get()) and app.float_vali(Ekin_entry.get())):
            m = float(m_entry.get())
            Ekin = float(Ekin_entry.get())
            result = math.sqrt(Ekin /  (0.5 * m))
            energi_result_text.set(str(result) + " m/s")
        else:
            energi_result_text.set("Dårligt input")
    #Beregner resultat ud fra formel m = Ekin / (0.5 * v^2)
    def masse_hastighed_kinenergi(self):
        if (app.float_vali(v_entry.get()) and app.float_vali(Ekin_entry.get())):
            v = float(v_entry.get())
            Ekin = float(Ekin_entry.get())
            result = Ekin /  (0.5 * v**2)
            energi_result_text.set(str(result) + " kg")
        else:
            energi_result_text.set("Dårligt input")

    #Opretter to multi choice skemaer, hvor man kan vælge hvad information
    #man har og man ønsker at finde. Opretter så knap, så beregningen
    #kan begynde via proceduren kin_beregning
    def movement_1d(self):
        global find_list, har_list, error_message
        self.top_beregn = Toplevel(self.top)
        msg_find = Message(self.top_beregn, text = "Vælg hvad du vil finde")
        msg_find.grid(row = 0)
        find_list = Listbox(self.top_beregn, exportselection = 0)
        find_list.grid(row = 1)
        msg_har = Message(self.top_beregn, text = "Hvad information har du?")
        msg_har.grid(row = 0, column = 1)
        har_list = Listbox(self.top_beregn, selectmode = MULTIPLE,
                           exportselection = 0)
        har_list.grid(row = 1, column = 1)
        muligheder = ["Starhastighed: v0 [m/s]", "Strækning: s [m]", "Tid: t [s]",
                      "Accelration: a [m/s^2]", 'Startrækning: s0 [m]',
                      'Hastighed: v [m/s]']
        for item in muligheder:
            find_list.insert(END, item)
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
