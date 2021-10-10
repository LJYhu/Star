# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox

total_H = 0
total_He = 0
total_C = 0
total_O = 0
total_Ne = 0
total_Mg = 0
total_Al = 0
total_Si = 0
total_Ca = 0
total_N = 0
total_S = 0
total_Ar = 0
total_Fe = 0

is_H = False
is_He = False
is_C = False
is_O = False
is_Ne = False
is_Mg = False
is_Al = False
is_Si = False
is_Ca = False
is_N = False
is_S = False
is_Ar = False
is_Fe = False


window = tk.Tk()
window.title('StarSCreator')
window.geometry('500x300')
canvas = tk.Canvas(window, height=300, width=500, bg='black')

varH = tk.StringVar()
varHe = tk.StringVar()
varC = tk.StringVar()
varO = tk.StringVar()
varNe = tk.StringVar()
varMg = tk.StringVar()
varAl = tk.StringVar()
varSi = tk.StringVar()
varCa = tk.StringVar()
varN = tk.StringVar()
varS = tk.StringVar()
varAr = tk.StringVar()
varFe = tk.StringVar()


inputRecordH = tk.Label(window, textvariable=varH, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordH.grid(row=0, column=0)
inputRecordHe = tk.Label(window, textvariable=varHe, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordHe.grid(row=0, column=1)
inputRecordC = tk.Label(window, textvariable=varC, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordC.grid(row=0, column=2)
inputRecordO = tk.Label(window, textvariable=varO, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordO.grid(row=2, column=0)
inputRecordNe = tk.Label(window, textvariable=varNe, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordNe.grid(row=2, column=1)
inputRecordMg = tk.Label(window, textvariable=varMg, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordMg.grid(row=2, column=2)
inputRecordAl = tk.Label(window, textvariable=varAl, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordAl.grid(row=4, column=0)
inputRecordSi = tk.Label(window, textvariable=varSi, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordSi.grid(row=4, column=1)
inputRecordCa = tk.Label(window, textvariable=varCa, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordCa.grid(row=4, column=2)
inputRecordN = tk.Label(window, textvariable=varN, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordN.grid(row=6, column=0)
inputRecordS = tk.Label(window, textvariable=varS, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordS.grid(row=6, column=1)
inputRecordAr = tk.Label(window, textvariable=varAr, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordAr.grid(row=6, column=2)
inputRecordFe = tk.Label(window, textvariable=varFe, bg='black', fg='white', font=('Arial', 12), width=10, height=2)
inputRecordFe.grid(row=8, column=0)

on_hit_H = False
on_hit_He = False
on_hit_C = False
on_hit_O = False
on_hit_Ne = False
on_hit_Mg = False
on_hit_Al = False
on_hit_Si = False
on_hit_Ca = False
on_hit_N = False
on_hit_S = False
on_hit_Ar = False
on_hit_Fe = False


def add_H():
    global on_hit_H
    if not on_hit_H:
        on_hit_H = True
        global total_H
        total_H = total_H + 5
        varH.set('H:' + str(total_H))
        global is_H
        is_H = True
    else:
        on_hit_H = False
        varH.set('')


def add_He():
    global on_hit_He
    if not on_hit_He:
        on_hit_He = True
        global total_He
        total_He = total_He + 5
        varHe.set('He:' + str(total_He))
        global is_He
        is_He = True
    else:
        on_hit_He = False
        varHe.set('')


def add_C():
    global on_hit_C
    if not on_hit_C:
        on_hit_C = True
        global total_C
        total_C = total_C + 5
        varC.set('C:' + str(total_C))
        global is_C
        is_C = True
    else:
        on_hit_C = False
        varC.set('')


def add_O():
    global on_hit_O
    if not on_hit_O:
        on_hit_O = True
        global total_O
        total_O = total_O + 5
        varO.set('O:' + str(total_O))
        global is_O
        is_O = True
    else:
        on_hit_O = False
        varO.set('')


def add_Ne():
    global on_hit_Ne
    if not on_hit_Ne:
        on_hit_Ne = True
        global total_Ne
        total_Ne = total_Ne + 5
        varNe.set('Ne:' + str(total_Ne))
        global is_Ne
        is_Ne = True
    else:
        on_hit_Ne = False
        varNe.set('')


def add_Mg():
    global on_hit_Mg
    if not on_hit_Mg:
        on_hit_Mg = True
        global total_Mg
        total_Mg = total_Mg + 5
        varMg.set('Mg:' + str(total_Mg))
        global is_Mg
        is_Mg = True
    else:
        on_hit_Mg = False
        varMg.set('')


def add_Al():
    global on_hit_Al
    if not on_hit_Al:
        on_hit_Al = True
        global total_Al
        total_Al = total_Al + 5
        varAl.set('Al:' + str(total_Al))
        global is_Al
        is_Al = True
    else:
        on_hit_Al = False
        varAl.set('')


def add_Si():
    global on_hit_Si
    if not on_hit_Si:
        on_hit_Si = True
        global total_Si
        total_Si = total_Si + 5
        varSi.set('Si:' + str(total_Si))
        global is_Si
        is_Si = True
    else:
        on_hit_Si = False
        varSi.set('')


def add_Ca():
    global on_hit_Ca
    if not on_hit_Ca:
        on_hit_Ca = True
        global total_Ca
        total_Ca = total_Ca + 5
        varCa.set('Ca:' + str(total_Ca))
        global is_Ca
        is_Ca = True
    else:
        on_hit_Ca = False
        varCa.set('')


def add_N():
    global on_hit_N
    if not on_hit_N:
        on_hit_N = True
        global total_N
        total_N = total_N + 5
        varN.set('N:' + str(total_N))
        global is_N
        is_N = True
    else:
        on_hit_N = False
        varN.set('')


def add_S():
    global on_hit_S
    if not on_hit_S:
        on_hit_S = True
        global total_S
        total_S = total_S + 5
        varS.set('S:' + str(total_S))
        global is_S
        is_S = True
    else:
        on_hit_S = False
        varS.set('')


def add_Ar():
    global on_hit_Ar
    if not on_hit_Ar:
        on_hit_Ar = True
        global total_Ar
        total_Ar = total_Ar + 5
        varAr.set('Ar:' + str(total_Ar))
        global is_Ar
        is_Ar = True
    else:
        on_hit_Ar = False
        varAr.set('')


def add_Fe():
    global on_hit_Fe
    if not on_hit_Fe:
        on_hit_Fe = True
        global total_Fe
        total_Fe = total_Fe + 5
        varFe.set('Fe:' + str(total_Fe))
        global is_Fe
        is_Fe = True
    else:
        on_hit_Fe = False
        varFe.set('')


bofH = tk.Button(window, text='add H', font=('Arial', 12), width=10, height=1, command=add_H)
bofH.grid(row=1, column=0)
bofHe = tk.Button(window, text='add He', font=('Arial', 12), width=10, height=1, command=add_He)
bofHe.grid(row=1, column=1)
bofC = tk.Button(window, text='add C', font=('Arial', 12), width=10, height=1, command=add_C)
bofC.grid(row=1, column=2)
bofO = tk.Button(window, text='add O', font=('Arial', 12), width=10, height=1, command=add_O)
bofO.grid(row=3, column=0)
bofNe = tk.Button(window, text='add Ne', font=('Arial', 12), width=10, height=1, command=add_Ne)
bofNe.grid(row=3, column=1)
bofMg = tk.Button(window, text='add Mg', font=('Arial', 12), width=10, height=1, command=add_Mg)
bofMg.grid(row=3, column=2)
bofAl = tk.Button(window, text='add Al', font=('Arial', 12), width=10, height=1, command=add_Al)
bofAl.grid(row=5, column=0)
bofSi = tk.Button(window, text='add Si', font=('Arial', 12), width=10, height=1, command=add_Si)
bofSi.grid(row=5, column=1)
bofCa = tk.Button(window, text='add Ca', font=('Arial', 12), width=10, height=1, command=add_Ca)
bofCa.grid(row=5, column=2)
bofN = tk.Button(window, text='add N', font=('Arial', 12), width=10, height=1, command=add_N)
bofN.grid(row=7, column=0)
bofS = tk.Button(window, text='add S', font=('Arial', 12), width=10, height=1, command=add_S)
bofS.grid(row=7, column=1)
bofAr = tk.Button(window, text='add Ar', font=('Arial', 12), width=10, height=1, command=add_Ar)
bofAr.grid(row=7, column=2)
bofFe = tk.Button(window, text='add Fe', font=('Arial', 12), width=10, height=1, command=add_Fe)
bofFe.grid(row=9, column=0)

total = total_H + total_He + total_C + total_O + total_Ne + total_Mg + total_Al + total_Si + total_Ca + total_N + \
        total_S + total_Ar + total_Fe

on_hit_final = False
varFinal = tk.StringVar()
inputRecordFe = tk.Label(window, textvariable=varFinal, bg='black', fg='white', font=('Arial', 12), width=50, height=2)
inputRecordFe.grid(row=9, column=5)


def finalButton():
    global on_hit_final
    if not on_hit_final:
        on_hit_final = True
        if total > 100:
            tk.messagebox.showerror(title='ERROR', message='The total number must be less than 100')
        if total_H >= 70:
            if total_H <= 75 and total_He >= 20:
                varFinal.set('Gas Giant: Your planet might be Sun')
            elif total_H <= 80 and total_O >= 10:
                varFinal.set('Gas Giant: Your planet might be Neptune')
            elif total_H <= 85 and total_He >= 10:
                varFinal.set('Gas Giant: Your planet might be Uranus')
            elif total_H >= 90:
                varFinal.set('Gas Giant: Your planet might be Saturn or Jupiter')
            else:
                varFinal.set('None')
        elif total_O >= 40:
            if total_Si >= 30:
                varFinal.set('Terrestrial Planet: Your planet might be Earth')
            elif total_Fe >= 10:
                if total_C >= 20:
                    varFinal.set('Terrestrial Planet: Your planet might be Ceres')
                if total_Fe > total_Si and total_C <= 20:
                    varFinal.set('Terrestrial Planet: Your planet might be Pluto')
                elif is_Ca:
                    varFinal.set('Terrestrial Planet: Your planet might be Moon')
                else:
                    varFinal.set('Terrestrial Planet: Your planet might be Mars')
            elif total_Mg >= 10:
                varFinal.set('Terrestrial Planet: Your planet might be Mercury')
            elif total_O >= 60:
                varFinal.set('Terrestrial Planet: Your planet might be Venus')
            else:
                varFinal.set('None')
        else:
            varFinal.set('None')
    else:
        on_hit_final = False
        varFinal.set('')


bofFinal = tk.Button(window, text='Final', font=('Arial', 12), width=10, height=1, command=finalButton)
bofFinal.grid(row=10, column=5)


window.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
