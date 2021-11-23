import os
from os.path import exists as file_exists
import base64


#------------Functions and global veriables START.------------#
menu = """
|_______________________|
|                       |
|      1. PNG           |
|      2. JPEG/JPG      |
|                       |
|_______________________|
"""

menu2 = """
|_______________________|
|                       |
|      1. Inject        |
|      2. Read          |
|                       |
|_______________________|
"""


def clear():
    os.system('clear||cls')


# Inject data into file.
def inject():
    clear()
    file = input("Name of file to use: ")

    if file_exists(file):
        clear()
        text1 = input("What text would you like to use?: ")
        clear()

        b64_txt = base64.b64encode(bytes(text1, 'utf-8'))
        with open(file, "ab") as f:
            f.write(b64_txt)
            print("Data has been injected!")

    else:
        print(f'The file with the name "{file}" does not exist in the current directory.')
        quit()
# End of Inject


# Read Injected Data
def read():
    clear()
    while True:

        try:
            file_format = int(input(f"{menu}\n\nIs this file a PNG or JPEG/JPG?: "))
            break
        except Exception as e:
            clear()
            print(f"Oops! Value given was not an integer, please try again.\nError: {e}")
    
    # PNG
    if file_format == 1:
        clear()
        file = input("Name of file to use: ")

        if file_exists(file):
            clear()
            with open(file, "rb") as f:
                content = f.read()
                offset = content.index(bytes.fromhex('0000000049454E44AE426082'))
                f.seek(offset + 12)
                inj_bytes = f.read()
                b64 = inj_bytes.decode('utf-8')
                result = base64.b64decode(b64)
                print(result)

        else:
            print(f'The file with the name "{file}" does not exist in the current directory.')
            quit()

    #JPG        
    if file_format == 2:
        clear()
        file = input("Name of file to use: ")

        if file_exists(file):
            clear()
            with open(file, "rb") as f:
                content = f.read()
                offset = content.index(bytes.fromhex('FFD9'))
                f.seek(offset + 2)
                inj_bytes2 = f.read()
                b64 = inj_bytes2.decode('utf-8')
                result = base64.b64decode(b64)
                print(result)
        else:
            print(f'The file with the name "{file}" does not exist in the current directory.')
            quit()

    # Not on menu
    if file_format == 0 or file_format > 2:
        clear()
        print("Invalid Number. | Number is not a choosable option.")
# End of Read

#------------Functions and global veriables END.------------#





#------------Code Start.------------#
while True:
    try:
        options = int(input(f"{menu2}\n\nWhat would you like to do?: "))
        break
    except Exception as e:
        clear()
        print(f"Oops! Value given was not an integer, please try again.\nError: {e}")


clear()
if options == 1:
    inject()

if options == 2:
    read()

if options == 0 or options > 2:
    print("Number not recconized")
    quit()

#------------Code End.------------#