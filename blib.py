import os
from os.path import exists as file_exists
import base64
import hashlib


#------------Functions and Stuff------------#

# I would like better menus..
def ftype_menu():
    menu = """
    |_______________________|
    |                       |
    |      1. PNG           |
    |      2. JPEG/JPG      |
    |      3. GIF           |
    |                       |
    |_______________________|
    """
    return menu


def option_menu():
    menu2 = """
    |____________________________|
    |                            |
    |      1. Inject Data        |
    |      2. Read Data          |
    |      3. Check File Hash    |
    |      4. Compare Hashes     |
    |                            |
    |____________________________|
    """
    return menu2


# Clears the terminal.
def clear():
    os.system('clear||cls')











# Inject data into file.
def inject():
    clear()
    file = input("Name of the file to use: ")

    if file_exists(file):
        clear()
        text1 = input("What text do you want to inject?: ")
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
            file_format = int(input(f"{ftype_menu()}\n\nIs this file a PNG or JPEG/JPG?: "))
            break
        except Exception as e:
            clear()
            print(f"Oops! Value given was not an integer, please try again.\nError: {e}")
    
    # PNG
    if file_format == 1:
        clear()
        file = input("Name of the file you want to read data from: ")

        if file_exists(file):
            clear()
            with open(file, "rb") as f:
                content = f.read()
                offset = content.index(bytes.fromhex('0000000049454E44AE426082'))
                f.seek(offset + 12)
                inj_bytes = f.read()
                result = base64.b64decode(inj_bytes)
                b64 = result.decode('utf-8')
                print(b64)

        else:
            print(f'The file with the name "{file}" does not exist in the current directory.')
            quit()

    #JPG        
    if file_format == 2:
        clear()
        file = input("Name of the file you want to read data from: ")

        if file_exists(file):
            clear()
            with open(file, "rb") as f:
                content = f.read()
                offset = content.index(bytes.fromhex('FFD9'))
                f.seek(offset + 2)
                inj_bytes2 = f.read()
                result = base64.b64decode(inj_bytes2)
                b64 = result.decode('utf-8')
                print(b64)
        else:
            print(f'The file with the name "{file}" does not exist in the current directory.')
            quit()

    #GIF      
    if file_format == 3:
        clear()
        file = input("Name of the file you want to read data from: ")

        if file_exists(file):
            clear()
            with open(file, "rb") as f:
                content = f.read()
                offset = content.index(bytes.fromhex('00003B'))
                f.seek(offset + 3)
                inj_bytes3 = f.read()
                result = base64.b64decode(inj_bytes3)
                b64 = result.decode('utf-8')
                print(b64)
        else:
            print(f'The file with the name "{file}" does not exist in the current directory.')
            quit()

    # Not on menu
    if file_format == 0 or file_format > 3:
        clear()
        print("Invalid Number. | Number is not a choosable option.")
# End of Read










# Check Hash
def check():
    buffer_size = 65536

    file = input("Name of the file you want check the hash of?: ")

    if file_exists(file):
        clear()

        sha256 = hashlib.sha256()
        with open(file, 'rb') as fh:
            while True:
                data = fh.read(buffer_size)
                if not data:
                    break
                sha256.update(data)
                nhash = sha256.hexdigest()

        print(f'Here is the hash for "{file}".\n\nsha256 hash: {nhash}')
    else:
        print(f'The file with the name "{file}" does not exist in the current directory.')
        quit()
# End of Check Hash










# Compare hash
def compare(fhash):
    buffer_size = 65536

    file = input("Name of the file to compare your hash against: ")

    if file_exists(file):
        clear()

        sha256 = hashlib.sha256()
        with open(file, 'rb') as fh:
            while True:
                data = fh.read(buffer_size)
                if not data:
                    break
                sha256.update(data)
                nhash = sha256.hexdigest()
        if fhash == nhash:
            p = print(f"The hash you provided matches {file}'s hash!\n\nYour hash - (sha256): {fhash}\nFile hash - (sha256): {nhash}")
            return p
        else:
            p = print(f"The hash you provided does not match {file}'s hash!\n\nYour hash - (sha256): {fhash}\nFile hash - (sha256): {nhash}")
            return p
    else:
        print(f'The file with the name "{file}" does not exist in the current directory.')
        quit()
# End Compare hash




if __name__ == '__main__':
    pass