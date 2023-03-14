from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import os.path

uWeight = 0
uHeight = 0
uAge = 0
rresults = []
info = ["Broc'a ", "Lorentz'a ", "Harris'a-Benedict'a", "Mifflina ", "Potton'a ", "BMI "]


def data():
    gui.withdraw()
    try:
        global uAge
        global uWeight
        global uHeight
        uAge = int(box.get())
        uWeight = int(box1.get())
        uHeight = int(box2.get())
        selection = var.get()
    except ValueError:
        messagebox.showerror("Error", "Podaj poprawne dane")
    if selection == 0:
        messagebox.showerror("Error", "Podaj płeć")
    if selection == 1:
        forMen()
        
    if selection == 2:
        forWomen()


def broc_m():
    weight = (uHeight-100)*0.9
    result = str(weight) + ' ' + "Kg"
    messagebox.showinfo("Wynik Broca", result)


def lorentz_m():
    weight = uHeight-100-(uHeight-150)/4
    result = str(weight) + ' ' + "Kg"
    messagebox.showinfo("Wynik Lorentza", result)


def hb_m():
    swe = 66.5+(13.75*uWeight)+(5.003*uHeight)-(6.775*uAge)
    result = str(swe) + '\n' + "Podstawowa Przemiana Materii"
    messagebox.showinfo("Wynik Harrisa-Benedicta", result)


def mifflin_m():
    swe = (10*uWeight)+(6.25*uHeight)-(5*uAge)+5
    result = str(swe) + '\n' + "Podstawowa Przemiana Materii"
    messagebox.showinfo("Wynik Mifflina", result)
    

def potton_m():
    weight = uHeight-100-(uHeight-100)/20
    result = str(weight) + ' ' + "Należna Masa Ciała"
    messagebox.showinfo("Wynik Pottona", result)


def broc_f():
    weight = (uHeight-100)*0.85
    result = str(weight) + ' ' + "Kg"
    messagebox.showinfo("Wynik Broca", result)


def lorenz_f():
    weight = uHeight-100-(uHeight-150)/2
    result = str(weight) + ' ' + "Kg"
    messagebox.showinfo("Wynik Lorentza", result)


def potton_f():
    weight = uHeight-100-(uHeight-100)/10
    result = str(weight) + ' ' + "Należna Masa Ciała"
    messagebox.showinfo("Wynik Pottona", result)


def mifflin_f():
    swe = (10*uWeight)+(6.25*uHeight)-(5*uAge)-161
    result = str(swe) + '\n' + "Podstawowa Przemiana Materii"
    messagebox.showinfo("Wynik Mifflina", result)
 

def hb_f():
    swe = 655.1+(9.563*uWeight)+(1.85*uHeight)-(4.676*uAge)
    result = str(swe) + '\n' + "Podstawowa Przemiana Materii"
    messagebox.showinfo("Wynik Harrisa-Benedicta", result)


def BMI():
    wynik = uWeight/(uHeight**2)*10000
    result = str(wynik) 
    messagebox.showinfo("Wynik BMI", result)


def allM():
    global male
    male.withdraw()
    global rresults
    one = (uHeight-100)*0.9
    two = uHeight-100-(uHeight-150)/4
    three = 66.5+(13.75*uWeight)+(5.003*uHeight)-(6.775*uAge)
    four = (10*uWeight)+(6.25*uHeight)-(5*uAge)+5
    five = uHeight-100-(uHeight-100)/20
    six = uWeight/(uHeight**2)*10000
    rresults = [one, two, three, four, five, six]
    resultinfo()


def allF():
    global female
    female.withdraw()
    global rresults
    one = (uHeight-100)*0.85
    two = uHeight-100-(uHeight-150)/2
    three = 655.1+(9.563*uWeight)+(1.85*uHeight)-(4.676*uAge)
    four = (10*uWeight)+(6.25*uHeight)-(5*uAge)-161
    five = uHeight-100-(uHeight-100)/10
    six = uWeight/(uHeight**2)*10000
    rresults = [one, two, three, four, five, six]
    resultinfo()


def forMen():
    global male
    male = Toplevel(gui)
    male.title("Kalkulatory dla mężczyzn")
    male.geometry("400x400")

    my_menu = Menu(male)
    male.config(menu=my_menu)
    file_menu = Menu(my_menu)

    my_menu.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Nowe dane", command=newDataM)

    header = Label(male, text="Wybierz Kalkulator:")
    header.pack(pady=25)
    text1 = Label(male, text="Obliczający należną masę ciała:")
    text1.pack(pady=10)
    broc = Button(male, text="Broc", command=broc_m)
    broc.pack()
    lorentz = Button(male, text="Lorentz", command=lorentz_m)
    lorentz.pack()
    potton = Button(male, text="Potton", command=potton_m)
    potton.pack()
    text2 = Label(male, text="Obliczający podtawową przemianę materii:")
    text2.pack()
    mifflin = Button(male, text="Mifflin", command=mifflin_m)
    mifflin.pack()
    harris = Button(male, text="Harris-Benedict", command=hb_m)
    harris.pack()
    text3 = Label(male, text="Obliczający indeks masy ciała:")
    text3.pack(pady=10)
    bmi = Button(male, text="BMI", command=BMI)
    bmi.pack()
    text4 = Label(male, text="Wykonaj wszystkie obliczenia i zapisz do pliku:")
    text4.pack(pady=10)
    everything = Button(male, text="Oblicz i zapisz", command=allM)
    everything.pack()

    male.mainloop()


def newDataK():
    female.withdraw()
    gui.deiconify()


def newDataM():
    male.withdraw()
    gui.deiconify()


def forWomen():
    global female
    female = Toplevel(gui)
    female.title("Kalkukalory dla kobiet")
    female.geometry("400x400")

    my_menu = Menu(female)
    female.config(menu=my_menu)
    file_menu = Menu(my_menu)

    my_menu.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Nowe dane", command=newDataK)

    header = Label(female, text="Wybierz kalkulator:")
    header.pack(pady=25)
    text1 = Label(female, text="Obliczający należną masę ciała")
    text1.pack(pady=10)
    broc = Button(female, text="Broc", command=broc_f)
    broc.pack()
    lorentz = Button(female, text="Lorentz", command=lorenz_f)
    lorentz.pack()
    potton = Button(female, text="Potton", command=potton_f)
    potton.pack()
    text2 = Label(female, text="Obliczający podstawową przemianę materii")
    text2.pack()
    mifflin = Button(female, text="Mifflin", command=mifflin_f)
    mifflin.pack()
    harris = Button(female, text="Harris-Benedict", command=hb_f)
    harris.pack()
    text3 = Label(female, text="Obliczający index masy ciała")
    text3.pack(pady=10)
    bmi = Button(female, text="BMI", command=BMI)
    bmi.pack()
    text4 = Label(female, text="Wykonaj wszystkie obliczenia i zapisz do pliku:")
    text4.pack(pady=10)
    everything = Button(female, text="Oblicz i zapisz", command=allF)
    everything.pack()
    female.mainloop()


def saveInfo():
    try:
        f = open("results.txt", "w")
        for x in range(len(rresults)):
            f.write(str(info[x])+" "+str(rresults[x])+"\n")
    except IOError:
        messagebox.showerror("Błąd")
    finally:
        f.close()
        if os.path.exists('results.txt'):
            messagebox.showinfo(":)", "Udało się")
            resultWindow.withdraw()
            data()


def resultinfo():
    global resultWindow
    resultWindow = Toplevel(gui)
    resultWindow.title("results")
    resultWindow.geometry("300x300")
    text3 = Label(resultWindow, text="Prawidłowo wykonano obliczenia")
    text3.pack(pady=10)
    save = Button(resultWindow, text="Zapisz do pliku", command=saveInfo)
    save.pack(pady=5)
    resultWindow.mainloop()


global gui
gui = Tk()
 
var = IntVar()
 
gui.title("Kalkulatory dietetyczne")
gui.geometry("400x400")
 
label1 = Label(gui, text="Podaj wiek")
label1.pack(pady=5)
box = Entry(gui)
box.pack(pady=5)
 
label2 = Label(gui, text="Podaj wagę")
label2.pack(pady=5)
box1 = Entry(gui)
box1.pack(pady=5)
 
label3 = Label(gui, text="Podaj wzrost")
label3.pack(pady=5)
box2 = Entry(gui)
box2.pack(pady=5)
 
R1 = Radiobutton(gui, text="Mężczyzna", variable=var, value=1)
R1.pack(pady=5)
R2 = Radiobutton(gui, text="Kobieta", variable=var, value=2)
R2.pack(pady=5)
 
b = Button(gui, text="Wprowadź", command=data)
b.pack(pady=5)
 
gui.mainloop() 
