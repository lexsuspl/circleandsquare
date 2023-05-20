# -*- coding: utf-8 -*-
import random
list=["papier","nozyce","kamien"]
wygra=""
punkty=0
pierwszaR=1
while True:
    if pierwszaR==1:
        print("Pierwsza runda")
        pierwszaR+=1
    else:
        print("Kolejna runda")
        pierwszaR+=1

    wylosowany = random.choice(list)
    print( "Wybierz za pomocą literki swoją broń: ")
    print("1: ", list[0]," 2: ",list[1]," 3: ",list[2])
    wybor =input('')
    wybor=int(wybor)

    if wybor == 1 and wylosowany== "papier":
        wygra ="Remis"
        punkty+=0

    if wybor == 2 and wylosowany== "papier":
        wygra ="Wygrana"
        punkty+=1
        
    if wybor == 3 and wylosowany== "papier":
        wygra ="Przegrana"
        punkty-=1

    if wybor == 1 and wylosowany== "nozyce":
        wygra ="Przegrana"
        punkty-=1

    if wybor == 2 and wylosowany== "nozyce":
        wygra ="Wygrana"
        punkty+=1

    if wybor == 3 and wylosowany== "nozyce":
        wygra ="Remis"
        punkty+=0

    if wybor == 1 and wylosowany== "kamien":
        wygra ="Wygrana"
        punkty=+1

    if wybor == 2 and wylosowany== "kamien":
        wygra ="Remis"
        punkty=+0
        
    if wybor == 3 and wylosowany== "kamien":
        wygra ="Przegrana"
        punkty=+1
    
    if wybor==1:
        print('Twój wybór:  Papier')
    elif wybor ==2:
        print('Twój wybór:  Kamień')
    elif wybor ==3:
        print('Twój wybór Nożyce')
    print("Wybór bota: ",wylosowany.capitalize()) #.capitalize() https://flexiple.com/python/python-capitalize-first-letter/
    print('Wynik pojedynku:',wygra)
    if punkty>0:

        print('Masz Punktów: ',punkty)
    elif punkty<0:
        print('Masz Punktów: ',punkty,' <-- Postaraj się bardziej')
    else:
        print('Masz Punktów: ',punkty)

    
    print('')
    print("Grasz dalej --> Y  / Skończ Grę -->Q")
    gracDalej=input()

    if gracDalej =="Y" or gracDalej =="y":
        wygra=""
    else:
        break


        



# Twórca Filip Bokwa 2T(e)P
