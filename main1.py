# -*- coding: utf-8 -*-

import math

class Statystyka:

    def srednia_arytmetyczna():
        liczby = []
        wynik = oblicz_srednia_arytmetyczna(liczby)
        print("Wynik:",wynik)

    def srednia_geometryczna():
        liczby = []
        dodaj_liczby_do_tablicy(liczby)

        suma = 1
        dlugosc = len(liczby)

        for element in liczby:
            suma *= element
        
        wynik = (suma ** (1/dlugosc))

        print("Wynik:",wynik)

    def mediana():
        liczby = []
        dodaj_liczby_do_tablicy(liczby)
        
        liczby.sort()

        dlugosc = len(liczby)

        if dlugosc % 2 != 0:
            res = liczby[round(dlugosc/2)-1]
            print("Wynik:",res)
        else:
            tmp = int((dlugosc/2) -1)
            tmp2 = int((dlugosc/2))

            liczba_1 = liczby[tmp]
            liczba_2 = liczby[tmp2]
            result = (liczba_1 + liczba_2) / 2

            print("Wynik:",result)

    def moda():
        liczby = []
        dodaj_liczby_do_tablicy(liczby)
        
        licznik = 0
        num = liczby[0]

        for i in liczby:
            f = liczby.count(i)
            if(f > licznik):
                licznik = f
                num = i
        
        print("Wynik:",num)

    def odchylenie_standardowe():
        liczby = []
        dodaj_liczby_do_tablicy(liczby)

        wynik = oblicz_odchylenie_standardowe(liczby)

        print("Wynik:", wynik)

    def wspolczynnik_korelacji():
        x = []
        y = []
        iloczyn = []
        cov = 0

        pary = int(input("Podaj ilość par: "))
        print("Liczby oddziel spacją np. x1 y1")
        for i in range(pary):
            tmp = list(map(int,input().split()))
            x.append(tmp[0])
            y.append(tmp[1])
            iloczyn.append(tmp[0] * tmp[1])
        
        x_srednia = policz_srednia_z_listy(x)
        y_srednia = policz_srednia_z_listy(y)
        iloczyn_srednia = policz_srednia_z_listy(iloczyn)

        cov = iloczyn_srednia - (x_srednia * y_srednia)
        odchylenie = oblicz_odchylenie_standardowe(x) * oblicz_odchylenie_standardowe(y)

        wynik = cov / odchylenie

        print("Wynik:", wynik)

    def wspolczynnik_regresji_liniowej():
        ilosc = int(input("Podaj ilość par liczb:"))
        x = []
        y = []
        roznica = []
        pierwsze = []
        drugie = []

        print("Podaj liczby po spacji np: x1 y1")
        for i in range(ilosc):
            tmp = list(map(int,input().split()))
            x.append(tmp[0])
            y.append(tmp[1])
            
        avgx = sum(x)/ilosc

        for j in range(ilosc):
            roznica.append(x[j] - avgx)
            pierwsze.append(y[j] * (x[j] - avgx)) 
            drugie.append((x[j] - avgx) ** 2 ) 
            
        suma1 = sum(pierwsze)
        suma2 = sum(drugie)

        wynik = suma1 / suma2
        print(wynik)

#Funkcje pomocnicze

def dodaj_liczby_do_tablicy(tab):
	x = int(input("Podaj ilość liczb: "))

	while x > 0:
		liczba = int(input())
		tab.append(liczba)	
		x -= 1

def oblicz_odchylenie_standardowe(tab):
    dlugosc = len(tab)
	#liczenie sredniej arytmetycznej
    tmp = oblicz_srednia_arytmetyczna(tab)

	#liczenie wariancji
    tmp2 = 0
    for element in tab:
        tmp2 += (element - tmp) ** 2

    wariancja = tmp2 / dlugosc
	
    wynik = math.sqrt(wariancja)

    return wynik

def oblicz_srednia_arytmetyczna(tab):
	dodaj_liczby_do_tablicy(tab)
		
	suma = 0
	dlugosc = len(tab)

	for element in tab:
		suma += element

	wynik = suma / dlugosc
	
	return wynik

def policz_srednia_z_listy(tab):
	y = len(tab)
	x = sum(tab)
	res = x/y
	
	return res
