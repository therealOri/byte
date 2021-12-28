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
try:
    option = int(input(f"{bl.banner()}\n\nWhat would you like to do?\n\n1. Encode\n2. Decode\n3. Get hash\n4. Compare hashes\n\nEnter: "))
except Exception as e:
    bl.clear()
    print(f'Value given is not an integer.\nError: {e}')
    quit()
    
if (option == 1):
    bl.clear()
    vid_or_img = input('What would you like to do?\n\n1. Image  |  (.png, .jpg, etc.)\n2. Video  |  (.webm, .mov, etc.)\n\nEnter: ')
    vid_or_img = int(vid_or_img)
    bl.clear()
    if vid_or_img == 1:
        bl.encode()

    if vid_or_img == 2:        
        f_name = input('Please provide the file you would like to inject data into: ')
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
        call(["ffmpeg", "-i", f_name, "-q:a", "0", "-map", "a", "./tmp/audio.mp3", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
        
        bl.encode_string(input_string)
        call(["ffmpeg", "-i", "./tmp/%d.png" , "-vcodec", "png", "./tmp/video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
        
        call(["ffmpeg", "-i", "./tmp/video.mov", "-i", "./tmp/audio.mp3", "-codec", "copy", "video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
        os.walk("./tmp/video.mov", os.getcwd())
        os.rename('video.mov', ofile_name)
        bl.clean_tmp()
        print(f'\n[LOG] Data successfully injected into "{ofile_name}"')

    elif vid_or_img == 0 or vid_or_img > 2:
        bl.clear()
        print("Incorrect value given. Please choose a valid option.")
        quit()


elif (option == 2):
    bl.clear()
    dec = input('What would you like to decode?\n\n1. Image  |  (.png, .jpg, etc.)\n2. Video  |  (.webm, .mov, etc.)\n\nEnter: ')
    dec = int(dec)
    bl.clear()
    if dec == 1:
        print("Decoded Data:  " + bl.decode())
    
    if dec == 2:
        bl.clear()
        video = input("Enter the name of video. (With extension): ")
        bl.clear()
        bl.decode_string(video)
        

    elif dec == 0 or dec > 2:
        bl.clear()
        print("Incorrect value given. Please choose a valid option.")
        quit()

elif (option == 3):
    bl.check()
elif (option == 4):
    bl.clear()
    fhash = input('Please provide a sha256 hash to compare: ')
    bl.clear()
    bl.compare(fhash)
else:
    bl.clear()
    print("Incorrect value given. Please choose a valid option.")
    quit()
