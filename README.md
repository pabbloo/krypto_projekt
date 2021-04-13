# Program szyfrujacy tekst na podstawie algorytmu Vigenere’a

Kryptografia 2 Projekt, W4, PWr 2021

# Cel Projektu
Zadanie projektowe polega na stworzeniu własnego systemu kryptograficznego do szyfrowania tekstów, maili, SMSów i innych danych. Projekt powinien sie składac z szyfratora i deszyfratora w formie programu w dowolnym jezyku programowania. Działanie programu ma byc nastepujace: wpisujemy tekst i dyspozycje ”szyfruj” . Po zaszyfrowaniu mozemy wpisac tresc zaszyfrowana i dyspozycje ”deszyfruj”. System kryptograficzny powinien byc w miare prosty - dotyczy nie wojska lecz zastosowaniom prywatnym. System nie moze byc implementacja wprost powszechnie znanych metod kryptograficznych, chociaz nie jest wykluczone stosowanie pewnych ich elementów. Dopuszczalne sa wszelkie, nawet najbardziej zwariowane metody szyfrowania.

# Opis
Program został napisany w jezyku Python wersja 3. Do stworzenia interfejsu graczinego została uzyta bilioteka Tkinter.
Program umozliwia zaszyrowowanie oraz odszyfrowanie wiadomosci tekstowej wybranym kluczem na podstawie algorytmu
Vigenere’a.

# Zasada Działania
Program działa na alfabiecie 37 elementowym. Dostepne sa wielkie litery, cyfry i spacja. Znaki takie jak kropki lub przecinki sa nieobsługiwane.

ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_

Uzytkowinik moze wybrac klucz, który okresli o ile nalezy przesunac litere w alfabecie (szyfr cezara). Po kliknieciu
przycisku Zaszyfruj tekst program przetwarza podany klucz na tablice z liczbami całkowitymi. Literom przypisuje sie ich
pozycje w alfabecie, cyfrom gdy sa obok siebie łaczy sie i dzieli modulo 37, a cyfrom które nie maja sasiada przypisywana
jest im ich wartosc. Dodatkowo obliczana jest suma kontrolna która dodawana jest na poczatek wygenerowanej tablicy
klucza. Suma kontrolna obliczana jest poprzez zsumowania wszystkich elementów i podzielona przez modulo 37.

![title](/tabela.png)

Gdy klucz jest dłuzszy niz tekst, klucz zostaje skrócony do długosci tekstu. Jezeli tekst jest dłuzszy, klucz jest
wydłuzany poprzez powtarzenie liter klucza do osiagniecia długosci tekstu.

![title](/1.png)
![title](/2.png)
![title](/3.png)
