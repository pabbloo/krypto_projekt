from tkinter import Tk, Label, Button, StringVar, Entry, Text, END


class Szyfrowanie:
    def __init__(self, master):
        self.master = master
        master.title("Szyfrowanie")

        self.a = Label(master, text="Tekst jawny")
        self.a1 = Text(master, height=8, width=35)
        self.b = Label(master, text="Tekst zaszyfrowany")
        self.b1 = Text(master, height=8, width=35)

        self.c = Label(master, text="Klucz:")
        v = StringVar(root, value='Tajny12345')
        self.c1 = Entry(master, textvariable=v)
        self.d = Label(master)
        self.btn1 = Button(master, text="Zaszyfruj tekst", width=20, command=self.btn1pressed)
        self.btn2 = Button(master, text="Odszyfruj tekst", width=20, command=self.btn2pressed)

        self.a.grid(row=0, column=0)
        self.a1.grid(row=1, column=0, padx=5, pady=5)
        self.b.grid(row=2, column=0)
        self.b1.grid(row=3, column=0)
        self.c.grid(row=4, column=0)
        self.c1.grid(row=5, column=0)
        self.d.grid(row=6, column=0)
        self.btn1.grid(row=7, column=0)
        self.btn2.grid(row=8, column=0, padx=2, pady=2)

        self.jawny = StringVar()
        self.klucz = StringVar()
        self.crypted = StringVar()

    def btn1pressed(self):
        self.jawny = self.a1.get("1.0", 'end-1c')

        sprawdzanko = str(self.jawny).upper()
        alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        suma = 0

        for i in range(len(sprawdzanko)):
            bylo = 0

            for j in range(len(alfabet)):
                if sprawdzanko[i] == alfabet[j]:
                    bylo = 1

            if bylo == 1:
                suma += 1

        if suma == len(sprawdzanko):
            self.klucz = self.c1.get()
            self.a1.delete(1.0, END)
            self.b1.delete(1.0, END)
            self.crypted = self.szyfrowanie(wej=self.jawny, klucz=self.klucz)
            self.b1.insert("1.0", self.crypted)
        else:
            self.a1.delete(1.0, END)
            self.jawny = "Uzyto nieobslugiwane znaki"
            self.a1.insert("1.0", self.jawny)

    def btn2pressed(self):
        self.crypted = self.b1.get("1.0", 'end-1c')

        sprawdzanko = str(self.crypted).upper()
        alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        suma = 0

        for i in range(len(sprawdzanko)):
            bylo = 0

            for j in range(len(alfabet)):
                if sprawdzanko[i] == alfabet[j]:
                    bylo = 1

            if bylo == 1:
                suma += 1

        if suma == len(sprawdzanko):
            self.crypted = self.b1.get("1.0", 'end-1c')
            self.klucz = self.c1.get()
            self.a1.delete(1.0, END)
            self.b1.delete(1.0, END)
            self.jawny = self.deszyfrowanie(wej=self.crypted, klucz=self.klucz)
            self.a1.insert("1.0", self.jawny)
        else:
            self.b1.delete(1.0, END)
            self.crypted = "Uzyto nieobslugiwane znaki"
            self.b1.insert("1.0", self.crypted)

    def szyfrowanie(self, wej, klucz):

        tekst = wej.upper()
        wyj = ""
        klucz_l = self.tlumaczenie_klucza(klucz=klucz)

        if len(klucz_l) < len(tekst):
            i = 0
            while len(klucz_l) < len(tekst):
                if i == len(klucz_l):
                    i = 0
                else:
                    klucz_l.append(klucz_l[i])

                i += 1
        elif len(klucz_l) > len(tekst):
            while len(klucz_l) > len(tekst):
                klucz_l.pop(len(klucz_l) - 1)

        for i in range(len(tekst)):
            wyj = wyj + self.cezar(znak=tekst[i], przesu=klucz_l[i])

        return wyj

    def deszyfrowanie(self, wej, klucz):
        tekst = wej.upper()
        wyj = ""
        klucz_l = self.tlumaczenie_klucza(klucz=klucz)

        if len(klucz_l) < len(tekst):
            i = 0
            while len(klucz_l) < len(tekst):
                if i == len(klucz_l):
                    i = 0
                else:
                    klucz_l.append(klucz_l[i])

                i += 1
        elif len(klucz_l) > len(tekst):
            while len(klucz_l) > len(tekst):
                klucz_l.pop(len(klucz_l) - 1)

        for i in range(len(tekst)):
            wyj = wyj + self.decezar(znak=tekst[i], przesu=klucz_l[i])

        return wyj

    def tlumaczenie_klucza(self, klucz):
        key = klucz.upper()
        lista = []
        lista.append(0)
        suma = 0

        i = 0
        while i < len(key):
            if 48 <= ord(key[i]) <= 57:
                if i + 1 == len(key):
                    lista.append(int(key[i]))
                    suma += (int(key[i]))
                    i += 1
                elif 48 <= ord(key[i + 1]) <= 57:
                    element = int((key[i] + key[i + 1])) % 37
                    lista.append(int(element))
                    suma += (int(element))
                    i += 2
                else:
                    lista.append(int(key[i]))
                    suma += (int(key[i]))
                    i += 1
            elif ord(key[i]) == 32:
                lista.append(6)
                suma += 6
                i += 1
            elif 65 <= ord(key[i]) <= 90:
                lista.append(self.pozycja_w_alfabecie(key[i]))
                suma += self.pozycja_w_alfabecie(key[i])
                i += 1

        lista[0] = suma % 37
        return lista

    def cezar(self, znak, przesu):
        alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        key = int(przesu)
        poz = self.pozycja_w_alfabecie(litera=znak)

        if poz + key > 36:
            wyjs = str(alfabet[poz + key - 37])
        else:
            wyjs = str(alfabet[poz + key])

        return wyjs

    def decezar(self, znak, przesu):
        alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        key = int(przesu)
        poz = self.pozycja_w_alfabecie(litera=znak)

        if poz - key < 0:
            wyjs = str(alfabet[37 + poz - key])
        else:
            wyjs = str(alfabet[poz - key])

        return wyjs

    def pozycja_w_alfabecie(self, litera):
        alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        pozycja = -1
        for i in range(len(alfabet)):
            if alfabet[i] == litera:
                pozycja = i

        return pozycja


root = Tk()
main = Szyfrowanie(root)
# root.geometry("290x460")
root.mainloop()
