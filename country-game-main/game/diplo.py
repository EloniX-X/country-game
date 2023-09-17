import sys
import os
clear = "\033c"
path = os.path.abspath("/Users/elon/Documents/programming/countrygame/")
sys.path.append(path)
#from game.turn import *
from turn import *

def attack(country):
        print('---attacking Veristan--')

        verpower = getstats('power', country)
        vercities = getstats('cities', country)
        mypower = getstats('power', 'Destan')
        mycities = getstats('cities', 'Destan')
        if mypower > verpower:
            print("you won")
            mynewcities = mycities + vercities
            mynewpower = mypower - verpower

            #updateint('alive', 'no', 'Veristan')

            print("you got ",mynewcities," cities")
            updateint('cities', mynewcities, 'Destan') 

            print("you now have ",mynewpower,'power')
            updateint('power',mynewpower, 'Destan')
            diplo_menu()

def war():
    clear
    print("your Destan")
    print("Destan | power ",getstats('power','Destan'))
    print("Veristan | power", getstats('power', 'Veristan'), " | alive ",gettxt('alive', 'Veristan'))
    print("NorthMontoro | power", getstats('power', 'NorthMontoro'), " | alive ",gettxt('alive', 'NorthMontoro'))
    print("WestMontoro | power", getstats('power', 'WestMontoro'), " | alive ",gettxt('alive', 'WestMontoro'))
    print("type attack (countryname) to go to war with them")
    you = input("President: ")

    if you == "attack veristan":
        attack(veristan)

               
    else:
        print("you lost")
        diplo_menu()


    #updateint('wars','Veristan','Destan')
#we have wars so if i go to war with someone do i needa set wars or just get
#power then if power > power I win and main = Destan(me) then merge them
def map():
    clear
    print("---local map---")
    print("--regions--")
    print("elden")
    print("Landan")
    print("Embark")

    print("-Destan-")
    
    print("Destan | bal ",getstats('bal','Destan')," | cities ",getstats('cities','Destan'), " | power ",getstats('power', 'Destan'))
    print("Veristan | bal ",getstats('bal','Veristan')," | cities ",getstats('cities','Veristan'), " | power ",getstats('power', 'Veristan'))
    diplo_menu()


def diplo_menu():
    clear
    from game.main import menu
    print("to view map -- 'map'")
    print("to view allies -- 'allies'")
    print("to view wars -- 'war'")
    you = input("President: ")
    if you == 'map':
        map()
    if you == 'war':
        war()
    if you == '':
        menu()