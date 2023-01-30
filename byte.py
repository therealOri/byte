import os
import sys
from os.path import exists as file_exists
from blib import bl
import beaupy
import gcm
import base64

import time
import cv2
import numpy as np
import math
from stegano import lsb
from subprocess import call, STDOUT


while True:
    options = ['Encode?', 'Decode?', 'Get hash?', 'Compare Hashes?', 'Quit?']
    bl.clear()

    print(f'{bl.banner()}\n\nWhat would you like to do? |   Press "ctrl+c" to exit or go back.\n-----------------------------------------------------------\n')
    option = beaupy.select(options, cursor_style="#ffa533")

    if not option:
        bl.clear()
        sys.exit("Keyboard Interuption Detected!\nGoodbye <3")

    if options[0] in option:
        bl.clear()
        encode_options = ['Image  |  (.png, .jpg, etc.)', 'Video  |  (.webm, .mov, etc.)']
        print(f'{bl.banner()}\n\nWhat would you like to do? |   Press "ctrl+c" to exit or go back.\n-----------------------------------------------------------\n')
        encode_option = beaupy.select(encode_options, cursor_style="#ffa533")

        if not encode_option:
            bl.clear()
            continue

        bl.clear()
        if encode_options[0] in encode_option:
            bl.encode()

        if encode_options[1] in encode_option:
            f_name = input('Please provide the file you would like to inject data into - (Drag & Drop): ').replace('\\ ', ' ').strip().replace("'", "")
            if file_exists(f_name):
                bl.clear()
                input_string = input('Enter data to be injected: ')

                key_data = input("Input data to make encryption key (100+ characters in length minimum): ")
                if len(key_data) < 100:
                    raise ValueError("Key must be 100 characters in length or more!")
                gcm.clear()

                bkey = bytes(key_data, 'utf-8')
                data = bytes(input_string, 'utf-8')
                key = gcm.keygen(bkey)
                save_me = base64.b64encode(key)
                input(f'Save this key for decrypting later: {save_me.decode()}\n\nPress "enter" to continue...')
                gcm.clear()
                data_enc = gcm.stringE(enc_data=data, key=key)

                bl.clear()
                ofile_name = input('Name of newly encoded file (with extension): ')
                bl.clear()
            else:
                raise ValueError("I can't find the file..it does not exist where specified or isn't a file.")


            bl.frame_extraction(f_name)
            call(["ffmpeg", "-i", f_name, "-q:a", "0", "-map", "a", ".tmp/audio.mp3", "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)

            bl.encode_string(data_enc)
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
            bl.clean_tmp()
            print(f'[LOG] Data successfully injected into "{ofile_name}"')



    if options[1] in option:
        bl.clear()
        decode_options = ['Image  |  (.png, .jpg, etc.)', 'Video  |  (.webm, .mov, etc.)']
        print(f'{bl.banner()}\n\nWhat would you like to do? |   Press "ctrl+c" to exit or go back.\n-----------------------------------------------------------\n')
        decode_option = beaupy.select(decode_options, cursor_style="#ffa533")

        if not decode_option:
            bl.clear()
            continue

        bl.clear()
        if decode_options[0] in decode_option:
            key = input("Encryption key: ")
            dKey = base64.b64decode(key)
            img_enc_data = bl.decode()
            result = gcm.stringD(dcr_data=img_enc_data, key=dKey)
            input(f'Decoded Data:  {result}\n\nPress "enter" to continue...')
            bl.clear()


        if decode_options[1] in decode_option:
            bl.clear()
            key = input("Encryption key: ")
            dKey = base64.b64decode(key)
            video = input("Video File - (Drag & Drop): ").replace('\\ ', ' ').strip().replace("'", "")
            bl.clear()
            vid_enc_data = bl.decode_string(video)

            result = gcm.stringD(dcr_data=vid_enc_data, key=dKey)
            input(f'Decoded Data:  {result}\n\nPress "enter" to continue...')
            bl.clear()



    if options[2] in option:
        bl.check()

    if options[3] in option:
        bl.clear()
        fhash = input('Please provide a valid blake2b hash to compare: ')
        bl.clear()
        bl.compare(fhash)

    if options[4] in option:
        bl.clear()
        sys.exit('Goodbye! <3')



