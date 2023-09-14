from diplo.diplo import diplo_menu
from game.turn import *
import time

clear = "\033c"



#getstats('column(ex: name, bal )')
makestats()
bal = getstats('bal', 'Destan')
cities = getstats('cities', 'Destan')
mats = getstats('mats', 'Destan')
power = getstats('power', 'Destan')
#man_power = getstats('man_power')



def citimenu():
    clear
    print('---cities---')
    print("to build city -- 100 mats, 500$")
    print("build to build city")
    you = input("President: ")
    if you == 'build':
            
        print("previous bal = ",bal)  # Should print the balance as an integer
        new_bal = bal - 500
        print("new bal = ", new_bal)  # Should print the new balance after subtracting 3
        updateint('bal', new_bal)

        print("--city count--")
        citycount = getstats('cities')
        print("previous city count = ",citycount)
        cityfin = citycount + 1
        print("new city count = ", cityfin)

        updateint('cities', cityfin)
    if you == '':
        menu()






def mystats():
    clear
    print("---current stats---")
    print("Balance: ",bal)
    print("Power: ",power)
    print("Materials: ",mats)
    print("Cities: ",cities)
    you = input("President: ")
    if you == '':
        clear
        menu()

def reset():
    print('resetting now')
    makestats()
    
def info():
    print('every 100 power 50 100 $ a turn to maintain')
    print('every city generates 500 $ each round')
    print('power costs 100$ ever 100 power')
    print('resetting will reset all of the games values to the og virsion like u just starts')
    print('to reset type -- resest')
    you = input("President: ")
    if you == 'reset':
        you = input("are you 100% sure? Y/N")
        if you == 'y':
            print('...resetting')
        if you == 'n':
            print('ok back to menu')
            menu()

def menu():
    print("---menu---")
    print("to view stats -- 'stats'")
    print("to manage cities -- 'cities'")
    print("to manage diplomacy -- 'diplo'")
    print("to manage army -- 'power'")
    print("to view info and settings -- 'info'")
    print('---to end turn press enter---')
    you = input("President: ")
    if you == 'info':
        info()
    if you == 'stats':
        print(clear)
        mystats()
    if you == 'diplo':
        print(clear)
        diplo_menu()
    if you == 'cities':
        citimenu()
    if you == '':
        citybal = cities * 500
        powercheck = power / 10
        newpowerbal = powercheck * -50
        citypower = citybal + newpowerbal
        newbal = bal + citypower
        
        getturn()
        updateint('bal', newbal,'Destan')
        print("will display for 3 seconds")
        time.sleep(1)
        print(clear)
        menu()

    if you == 'power':
        print('every 100 power 50$ a turn to maintain')
        print('power costs 100$ ever 100 power')
        print('type "buy" to buy power')
        print('type "disban" to disband power (less maintaining cost)')
        print("(remember) to go back to main type nothing and press enter")
        you = input("President: ")
        if you == "buy":
            amttopotbuy = input("amt: ")
            amttopotbuy = int(amttopotbuy)
            amtcost = (amttopotbuy / 10) * 100
            if amtcost > bal:
                print('you dont have enough money :(')
            else:
                print("successfully bought", amttopotbuy, "for ", amtcost)
                updateint('power', amttopotbuy, 'Destan')




menu()