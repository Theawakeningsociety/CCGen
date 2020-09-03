#!/usr/bin/env python
#-*- coding: iso-8859-1 -*-
import getopt
import time
import os
import sys
import datetime
from random import randint
try:
    from colorama import init
    from termcolor import colored
except ImportError:
    print("""
    Tienes que instalar primero los requisitos,
    esto lo logras escribiendo el siguiente comando:
    pip install -r req.txt
    """)

embl =  """
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ? _____________________      ?
 ?| Hello member,       |     ?
 ?| welcome to          |     ?
 ?| RESET CCGEN         |     ?
 ? ---------------------      ?
 ?                    \       ?
 ?                     (oo)   ?
 ?                     (__)   ?
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 | Edited by: Durd3n & Guarc0n |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 """
init()
print(colored(embl, 'red'))

print("")
me = colored("ME", 'green')
xi = colored("XI", 'white')
co = colored("CO", 'red')
print("\t\t" + colored('FROM ', 'yellow')  + me + xi + co + colored(" TO THE WORLD", 'yellow'))
print(colored("\t    +------------------------------+", 'green'))
print("\t    + \t    GENERADOR DE BINS      +")
print(colored("\t    +------------------------------+", 'red'))
print("")
time.sleep(.5)
print("")

#CHECKER BASADO EN ALGORITMO LUHN
def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

#GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX
def ccgen(bin_format):
    out_cc = ""
    if len(bin_format) == 16:
        #Iteration over the bin
        for i in range(15):
            if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                out_cc = out_cc + bin_format[i]
                continue
            elif bin_format[i] in ("x"):
                out_cc = out_cc + str(randint(0,9))
            else:
                print("\nCaracter no valido en el formato: {}\n".format(bin_format))
                print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
                sys.exit()

        #Generate checksum (last digit) -- IMPLICIT CHECK
        for i in range(10):
            checksum_check = out_cc
            checksum_check = checksum_check + str(i)

            if cardLuhnChecksumIsValid(checksum_check):
                out_cc = checksum_check
                break
            else:
                checksum_check = out_cc

    else:
        print("\033[1;32m")
        print("\nERROR: Inserta un bin valido\n")
        print("SOLUCION: El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        print("AYUDA: python2 ccgenR.py -h\n")
        sys.exit()

    return(out_cc)
#Random ccv gen
def ccvgen():
    ccv = ""
    num = randint(10,999)

    if num < 100:
        ccv = str(num) + "0"
    else:
        ccv = str(num)

    return(ccv)

#Random exp date
def dategen():
    now = datetime.datetime.now()
    date = ""
    month = str(randint(1, 12))
    if len(month) == 1:
    	month = "0" + month

    current_year = str(now.year)
    year = str(randint(int(current_year[-0:]) + 1, int(current_year[-0:]) + 6))
    date = month + "|" + year

    return date

#The main function
def main(argv):
    bin_format = raw_input("Ingrese el formato: ")
    print("")
    limit = raw_input("Cantidad (Por defecto 10): ")
    if limit == '':
        limit = 10;
    print("")
    date = raw_input("Desea generar la fecha? [Y/N] (Por defecto Y): ")
    print("")
    if date == "y" or date == 'Y' or date == '':
        date = True
    else:
        date = False
    ccv = raw_input("Desea generar el cvv [Y/N] (Por defecto Y): ")

    if ccv == 'y' or ccv == 'Y' or ccv == '':
        ccv = True
    else:
        ccv = False
    bin_list = []
    #get arg data
    if bin_format is not "":
        for i in range(int(limit)):
            if ccv and date:
                bin_list.append(ccgen(bin_format) + "|" + dategen() + "|" + ccvgen())
                print(colored(bin_list[i], 'red'))
            elif ccv and not date:
                bin_list.append(ccgen(bin_format) + "|" + ccvgen())
                print(colored(bin_list[i], 'red'))
            elif date and not ccv:
                bin_list.append(ccgen(bin_format) + "|" + dategen())
                print(colored(bin_list[i], 'red'))
            elif not date and not ccv:
                bin_list.append(ccgen(bin_format))
                print(colored(bin_list[i], 'red'))

        if not bin_list:
            print("\nERROR: el bin que insertaste no es valido\n")
        else:
            print(colored("""
            Todas las tarjetas fueron
            validadas correctamente
            por el Algoritmo de Luhn.
            Pueden ser usadas
            satisfactoriamente.
            """, 'yellow'))
    else:
        usage()
        sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])
