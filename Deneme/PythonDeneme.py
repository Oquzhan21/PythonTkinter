
from tkinter import *
class sinifismi:
    def __init__(self, master):
        self.giris = StringVar()
        Entry(textvariable=self.giris).pack()
        self.liste = Listbox()
        self.liste.pack()
        Button(text="Ekle", command=self.eklesene).pack()
        Button(text="Sil", command=self.silsene).pack()

    def eklesene(self):
        self.liste.insert(END, self.giris.get())

    def silsene(self):
        self.liste.delete(ACTIVE)


ana = Tk()
yeni = sinifismi(ana)
mainloop()