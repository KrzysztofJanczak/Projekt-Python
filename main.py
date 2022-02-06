# -*- coding: utf-8 -*-

import sys
from statystyka import Statystyka

valid = [i for i in range(9)]

while True:
    print("------------------------------------")
    print("1. Srednia arytmetyczna ")
    print("2. Srednia geometryczna ")
    print("3. Oblicz mediane ")
    print("4. Oblicz mode")
    print("5. Oblicz odchylenie standardowe")
    print("6. Oblicz współczynnik korelacji")
    print("7. Oblicz wspolczynnik regresji liniowej")
    print("8. to exit ")
    print("------------------------------------")
    
    try:
        x = int(input("""Co chcesz zrobić ? Podaj liczbę od 1-8 -> """))
    except:
        print("Podaj dobry input")
        continue

    if x not in valid:
        print("Podaj dobry input")

    if x == 8:
        sys.exit()
    elif x == 1:
        Statystyka.srednia_arytmetyczna()
    elif x == 2:
        Statystyka.srednia_geometryczna()
    elif x == 3:
        Statystyka.mediana()
    elif x == 4:
        Statystyka.moda()
    elif x == 5:
        Statystyka.odchylenie_standardowe()
    elif x == 6:
        Statystyka.wspolczynnik_korelacji()
    elif x == 7:
        Statystyka.wspolczynnik_regresji_liniowej()
