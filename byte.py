# Library for byte. | Aka the file being used for all of the functions to call and use.
from blib import bl


#------------Code Start.------------#
bl.clear()
try:
    a = int(input(f"{bl.banner()}\n\nWhat would you like to do?\n\n1. Encode\n2. Decode\n3. Get hash\n4. Compare hashes\n\nEnter: "))
except Exception as e:
    bl.clear()
    print(f'Value given is not an integer.\nError: {e}')
    quit()
    
if (a == 1):
    bl.encode()
elif (a == 2):
    print(f"Decoded Data:  {bl.decode()}")
elif (a == 3):
    bl.check()
elif (a == 4):
    bl.clear()
    fhash = input('Please provide a sha256 hash to compare: ')
    bl.clear()
    bl.compare(fhash)
else:
    bl.clear()
    print("Incorrect value given. Please choose a valid option.")
    quit()

#------------Code End.------------#
