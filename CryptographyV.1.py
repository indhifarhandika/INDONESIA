#!/usr/bin/env python3
#code by indhifarhandika

import string
WHITE, NON, RED, YELLOW = '\33[1;97m', '\33[0m', '\33[1;91m', '\33[93m'
print(RED + '''
             # ##   # ###    ##  ##   # ####   ###  #  ##
             # # #  # #  #  #  # # #  # #     #   * # #  #
             # #  # # #   # #  # #  # # ###    #    # #### '''+ WHITE +'''
             # #   ## #  #  #  # #   ## #    *  #   # #  #
             # #    # ###    ##  #    # ####  ####  # #  #'''  )

print(WHITE +'''          
                   Criptography by INDHI FARHANDIKA R

                                 V.1

                     indhi.farhandika@programmer.net'''+ NON)
def menu():
    print(YELLOW +'''
                  -_-_-_-_-_-_-_- MENU -_-_-_-_-_-_-_-
                  |                                   |
                  |           1. Encrypt              |
                  |                                   |
                  |           2. Decrypt              |
                  |                                   |
                  |           0. Exit                 |
                  |_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|'''+ NON)
    a = input('>>> ')
    if a == '1':
        print(ency())
    elif a == '2':
        print(dec())
    elif a == '0':
        print('')
        print('Thanks')
        exit()
def dec():
  result = ''
  message = input('Decrypt : ')
  key = int(input('Key : '))
  for i in range(0, len(message)):
    result = result + chr(ord(message[i]) + key )
  print(result + '')
  result = ''
  print(menu())

def ency():
  result = ''
  message = input('Encrypt : ')
  key = int(input('Key : '))
  for i in range(0, len(message)):
    result = result + chr(ord(message[i]) - key )
  print(result + '')
  result = ''
  print(menu())

if __name__ == '__main__':
  menu()