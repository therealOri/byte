import os
from os.path import exists as file_exists
from blib import bl

import time
import cv2
import numpy as np
import math
from stegano import lsb
from subprocess import call, STDOUT


bl.clear()
while True:
    try:
        option = int(input(f"{bl.banner()}\n\nWhat would you like to do?\n\n1. Encode\n2. Decode\n3. Get hash\n4. Compare hashes\n5. Quit?\n\nEnter: "))
    except Exception as e:
        bl.clear()
        print(f"Oops and error occured..Not an integer.\nError: {e}\n\n")
        input("Press enter to continue...")
        bl.clear()

    if option == 1:
        bl.clear()
        while True:
            try:
                vid_or_img = int(input('What would you like to Encode?\n\n1. Image  |  (.png, .jpg, etc.)\n2. Video  |  (.webm, .mov, etc.)\n3. Back?\n\nEnter: '))
            except Exception as e:
                bl.clear()
                print(f"Oops and error occured..Not an integer.\nError: {e}\n\n")
                input("Press enter to continue...")
                bl.clear()
                continue

            bl.clear()
            if vid_or_img == 1:
                bl.encode()

            if vid_or_img == 2:        
                f_name = input('Please provide the file you would like to inject data into: ').replace('\\', ' ').strip()
                if file_exists(f_name):
                    bl.clear()
                    input_string = input('Enter data to be injected: ')
                    bl.clear()
                    ofile_name = input('Name of newly encoded file (with extension): ')
                    bl.clear()
                else:
                    print(f'The file with the name "{file}" does not exist in the current directory.')
                    quit()

                bl.frame_extraction(f_name)
                call(["ffmpeg", "-i", f_name, "-q:a", "0", "-map", "a", ".tmp/audio.mp3", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

                bl.encode_string(input_string)
                print("Encoding and recompiling data...")
                call(["ffmpeg", "-i", ".tmp/%d.png" , "-vcodec", "png", ".tmp/video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
                if file_exists('.tmp/audio.mp3'):
                    call(["ffmpeg", "-i", ".tmp/video.mov", "-i", ".tmp/audio.mp3", "-codec", "copy", "video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
                else:
                    call(["ffmpeg", "-i", ".tmp/video.mov", "-codec", "copy", "video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

                cwd = os.getcwd()
                os.walk(".tmp/video.mov", cwd)
                os.rename('video.mov', ofile_name)
                bl.clear()
                print("Cleaning up...")
                bl.clean_tmp()
                print(f'\n[LOG] Data successfully injected into "{ofile_name}"\n')
                input("Press enter to continue...")
                bl.clear()


            elif vid_or_img == 3:
                bl.clear()
                break

            elif vid_or_img < 1 or vid_or_img > 3:
                bl.clear()
                print("Incorrect value given. Please choose a valid option.")
                input("Press enter to continue...")
                bl.clear()


    elif option == 2:
        bl.clear()
        while True:
            try:
                dec = int(input('What would you like to decode?\n\n1. Image  |  (.png, .jpg, etc.)\n2. Video  |  (.mp4, .webm, .mov, etc.)\n3. Back?\n\nEnter: '))
            except Exception as e:
                bl.clear()
                print(f"Oops and error occured..Not an integer.\nError: {e}\n\n")
                input("Press enter to continue...")
                bl.clear()
                continue

            bl.clear()
            if dec == 1:
                data = bl.decode()
                if not data or data == None:
                    print("There must have been an error...that or there was no data to be decoded.")
                    input("Press enter to continue...")
                    bl.clear()
                else:
                    print(f"Decoded Data:  {data}\n")
                    input("Press enter to continue...")
                    bl.clear()

            if dec == 2:
                bl.clear()
                video = input("Enter the name of video. (With extension): ").replace('\\', ' ').strip().replace('"','').replace("'","")
                bl.clear()
                bl.decode_string(video)

            if dec == 3:
                bl.clear()
                break

            elif dec < 1 or dec > 3:
                bl.clear()
                print("Incorrect value given. Please choose a valid option.")
                input("Press enter to continue...")
                bl.clear()
                



    elif option == 3:
        bl.check()

    elif option == 4:
        bl.clear()
        fhash = input('Please provide a valid blake2b hash to compare: ')
        bl.clear()
        bl.compare(fhash)

    elif option == 5:
        bl.clear()
        exit('Goodbye!')

    elif option < 1 or option > 5:
        bl.clear()
        print("Unknown option...")
        input("Press enter to continue...")
        bl.clear()
        continue
