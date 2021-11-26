# Library for byte. | Aka the file being used for all of the functions to call and use.
from blib import bl

#------------Code Start.------------#
while True:
    try:
        options = int(input(f"{bl.option_menu()}\n\nWhat would you like to do?: "))
        break
    except Exception as e:
        blib.clear()
        print(f"Oops! Value given was not an integer, please try again.\nError: {e}")


bl.clear()
if options == 1:
    bl.inject()

if options == 2:
    bl.read()

if options == 3:
    bl.check()

if options == 4:
    fhash = input('Please provide a sha256 hash to compare: ')
    bl.clear()
    bl.compare(fhash)

if options == 0 or options > 4:
    print("Invalid Number. | Number is not a choosable option.")
    quit()

#------------Code End.------------#
