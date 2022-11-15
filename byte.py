import os
from os.path import exists as file_exists
from blib import bl
from gcm import GCMlib #gcm.so file | Contains functions for AES encryption using mode GCM
import base64
gcm = GCMlib()

import time
import cv2
import numpy as np
import math
from stegano import lsb
from subprocess import call, STDOUT


bl.clear()
try:
    option = int(input(f"{bl.banner()}\n\nWhat would you like to do?\n\n1. Encode\n2. Decode\n3. Get hash\n4. Compare hashes\n5. Quit\n\nEnter: "))
except Exception as e:
    bl.clear()
    print(f'Value given is not an integer.\nError: {e}')
    quit()

if option == 1:
    bl.clear()
    vid_or_img = input('What would you like to do?\n\n1. Image  |  (.png, .jpg, etc.)\n2. Video  |  (.webm, .mov, etc.)\n\nEnter: ')
    vid_or_img = int(vid_or_img)
    bl.clear()
    if vid_or_img == 1:
        bl.encode()

    if vid_or_img == 2:
        f_name = input('Please provide the file you would like to inject data into - (Drag & Drop): ').replace('\\ ', ' ').strip()
        if file_exists(f_name):
            bl.clear()
            input_string = input('Enter data to be injected: ')

            key_data = input("Input data to make encryption key (100+ characters in length minimum): ")
            if len(key_data) < 100:
                raise ValueError("Key must be 100 characters in length or more!")
            gcm.clear()

            key = bytes(key_data, 'utf-8')
            data = bytes(input_string, 'utf-8')
            key = gcm.keygen(key)
            save_me = base64.b64encode(key)
            input(f'Save this key for decrypting later: {save_me.decode()}\n\nPress "enter" to continue...')
            gcm.clear()
            enc_data = gcm.stringE(data, key)

            bl.clear()
            ofile_name = input('Name of newly encoded file (with extension): ')
            bl.clear()
        else:
            raise ValueError("I can't find the file..it does not exist where specified or isn't a file.")


        bl.frame_extraction(f_name)
        call(["ffmpeg", "-i", f_name, "-q:a", "0", "-map", "a", ".tmp/audio.mp3", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

        bl.encode_string(enc_data)
        print("[INFO] finalizing & Cleaning up tmp files...")

        call(["ffmpeg", "-i", ".tmp/%d.png" , "-vcodec", "png", ".tmp/video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
        if file_exists('.tmp/audio.mp3'):
            call(["ffmpeg", "-i", ".tmp/video.mov", "-i", ".tmp/audio.mp3", "-codec", "copy", "video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
        else:
            call(["ffmpeg", "-i", ".tmp/video.mov", "-codec", "copy", "video.mov", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

        cwd = os.getcwd()
        os.walk(".tmp/video.mov", cwd)
        os.rename('video.mov', ofile_name)
        bl.clear()
        #print("[INFO] Cleaning up tmp files...")
        bl.clean_tmp()
        print(f'[LOG] Data successfully injected into "{ofile_name}"')

    elif vid_or_img == 0 or vid_or_img > 2:
        bl.clear()
        print("Incorrect value given. Please choose a valid option.")
        quit()


elif option == 2:
    bl.clear()
    dec = input('What would you like to decode?\n\n1. Image  |  (.png, .jpg, etc.)\n2. Video  |  (.webm, .mov, etc.)\n\nEnter: ')
    dec = int(dec)
    bl.clear()
    if dec == 1:
        key = input("Encryption key: ")
        dKey = base64.b64decode(key)
        img_enc_data = bl.decode()
        result = gcm.stringD(img_enc_data, dKey)
        input(f'Decoded Data:  {result}\n\nPress "enter" to continue...')
        bl.clear()


    if dec == 2:
        bl.clear()
        key = input("Encryption key: ")
        dKey = base64.b64decode(key)
        video = input("Video File - (Drag & Drop): ").replace('\\ ', ' ').strip()
        bl.clear()
        vid_enc_data = bl.decode_string(video)

        result = gcm.stringD(vid_enc_data, dKey)
        input(f'Decoded Data:  {result}\n\nPress "enter" to continue...')
        bl.clear()


    elif dec == 0 or dec > 2:
        bl.clear()
        print("Incorrect value given. Please choose a valid option.")
        quit()

elif option == 3:
    bl.check()
elif option == 4:
    bl.clear()
    fhash = input('Please provide a valid blake2b hash to compare: ')
    bl.clear()
    bl.compare(fhash)
elif option == 5:
    clear()
    exit('Goodbye!')
else:
    bl.clear()
    print("Incorrect value given. Please choose a valid option.")
    quit()
