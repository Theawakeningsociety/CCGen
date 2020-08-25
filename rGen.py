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
time.sleep(.5)
print("")
#Informacion de ayuda
def usage():
    print(colored("\t    +------------------------------+", 'green'))
    print("\t    + \t    GENERADOR DE BINS      +")
    print(colored("\t    +------------------------------+", 'red'))
    print("")
    print(colored(" Metodo de uso ", 'yellow'))
    print("")
    print(colored("     python2 rGen.py -b     [Opciones de uso]", 'cyan'))
    print(colored("     python2 rGen.py -h     Mensaje de ayuda", 'cyan'))
    print("")
    print(colored("+-----------------+", 'red'))
    print(colored("+ ", 'red') + colored("Opciones de uso", 'green') + colored(" +", 'red'))
    print(colored("+-----------------+", 'red'))
    print(colored("""
         -b, -bin          Formato de bin"
         -u, -cantidad     Cantidad de tarjetas a generar"
         -c, -ccv          Genera ccv al azar"
         -d, -date         Genera fechas al azar"
         -g, -guardar      Guarda las tarjetas en un archivo
         """, 'cyan'))
    print(colored("+----------------+", 'red'))
    print(colored("+ ", 'red') + colored("Ejemplo de uso", 'green') + colored(" +", 'red'))
    print(colored("+----------------+", 'red'))
    print(colored("""     
         python2 rGen.py -b 549949xxxxxxxxxx -u 5
         python rGen.py -b  557907xxxxxxxxxx -u 10 -d -c 
         """, 'cyan'))

#Arg parser
def parseOptions(argv):
    bin_format = ""
    saveopt = False
    limit = 10
    ccv = False
    date = False
    check = False

    try:
        import colorama
        opts, args = getopt.getopt(argv, "h:b:u:gcd",["help", "bin", "guardar", "cantidad", "ccv", "date"])
        for opt, arg in opts:
            if opt in ("-h"):
                usage()
                sys.exit()
            elif opt in ("-b", "-bin"):
                bin_format = arg
            elif opt in ("-g", "-guardar"):
                saveopt = True
            elif opt in ("-u", "-cantidad"):
                limit = arg
            elif opt in ("-c", "-ccv"):
                ccv = True
            elif opt in ("-d", "-date"):
                date = True

        return(bin_format, saveopt, limit, ccv, date)

    except getopt.GetoptError:
        usage()
        sys.exit(2)

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
                print("Ayuda: python2 rGen.py -h \n")
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

#Write on a file that takes a list for the argument
def save(generated):
    now = datetime.datetime.now()
    file_name = "cc-gen_output_{0}.txt".format(str(now.day) + str(now.hour) + str(now.minute) + str(now.second))
    f = open(file_name, 'w')
    for line in generated:
        f.write(line + "\n")
    f.close

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
    bin_list = []
    #get arg data
    (bin_format, saveopt, limit, ccv, date) = parseOptions(argv)
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

        if saveopt:
            save(bin_list)
    else:
        usage()
        sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])
