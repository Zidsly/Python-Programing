from ast import Num
from pyfiglet import figlet_format
from termcolor import colored
import os

x = 0
per = 0
hall = 0
totalPrice = 0
nemesisPrice = 85000
primePrice = 50000


def NumOfPerson():
    global x
    x = int(input('Please Enter Number of Person: '))


def price():
    global per
    if hall == 1 or hall == 3:
        per = primePrice
    elif hall == 2 or hall == 4:
        per = nemesisPrice
    return per


def summary():
    os.system('cls||clear')
    print("===================================================")
    print("          SUMMARY OF YOUR BOOKING TICKET")
    print("===================================================")
    print("\n")
    print("Movie Title\t: ")

    if hall == 1 or hall == 2:
        d = figlet_format("Doctor Strange : Into the Multiverse of Madness", font="slant")
        print(d)
    elif hall == 3 or hall == 4:
        t = figlet_format("Thor: Love and Thunder", font="slant")
        print(t)

    print("\n")
    print("HALL \t\t: ", hall)
    print("Total Price\t: Rp " + str(totalPrice))
    print("\n==================================================")


def printHall():
    os.system('cls||clear')
    f = figlet_format("Lancelot Cinema", font="slant")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("\n")
    print("The local time is: ")
    print("---------------------------------------------------------------")
    print("|     Hall         |          Movie          |    Show Time   |")
    print("| |1| Prime Hall   |  Doctor Strange:ITMOM   |      12:15     |")
    print("| |2| Nemesis Hall |  Doctor Strange:ITMOM   |      12:45     |")
    print("| |3| Prime Hall   |  Thor: Love and Thunder |      15:30     |")
    print("| |4| Nemesis Hall |  Thor: Love and Thunder |      15:55     |")
    print("---------------------------------------------------------------")
    print("Prime Hall   : Rp ", primePrice, " per person")
    print("Nemesis Hall : Rp ", nemesisPrice, " per person")


def movieList():
    f = figlet_format("Lancelot Cinema", font="slant")
    global hall
    global totalPrice
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("\n")
    print("The local time is: ")
    print("-----------------------------------------------------")
    print("|\t\t     Movie List                     |")
    print("-----------------------------------------------------")
    print("|           Movie           |           Duration    |")
    print("-----------------------------------------------------")
    print("|    Doctor Strange:ITMOM   |           2 h 6 m     |")
    print("|   Thor: Love and Thunder  |           2 h 13 m    |")
    print("-----------------------------------------------------")
    print("\n")
    print("                  |1| Buy Movie Ticket")
    print("                  |2| Exit Programs\n")
    Pref = int(input("Please enter your preferance: "))
    if Pref == 1:
        printHall()
        print("\n")
        hall = int(input("Select Your Hall: "))
        return hall

        price()
        NumOfPerson()
        totalPrice = int(per * x)
        return totalPrice

    elif Pref == 2:
        exit = figlet_format("THANK YOU !!")
        print(exit)
    else:
        wrong = figlet_format("WRONG - INPUT")
        print(wrong)


movieList()
summary()