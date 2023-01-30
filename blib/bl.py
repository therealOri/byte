from PIL import Image
import os
from os.path import exists as file_exists
from hashlib import blake2b
import base64
import gcm

import time
import cv2
import numpy as np
import math
import shutil
from stegano import lsb
from subprocess import call, STDOUT
from alive_progress import alive_bar
from imutils.video import count_frames


#------------Functions------------#

def clear():
    os.system('clear||cls')


def banner():
    return """

              ██████╗ ██╗   ██╗████████╗███████╗
              ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
              ██████╔╝ ╚████╔╝    ██║   █████╗  
              ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
              ██████╔╝   ██║      ██║   ███████╗
              ╚═════╝    ╚═╝      ╚═╝   ╚══════╝


Made by Ori#6338 | @therealOri_ | https://github.com/therealOri

    """



# Check Hash
def check():
    clear()
    file = input('File to check hash of. - (Drag & Drop): ').replace('\\ ', ' ').strip().replace("'", "")

    if file_exists(file):
        clear()

        buffer_size = 65536

        with open(file, 'rb') as fh:
            while True:
                data = fh.read(buffer_size)
                if not data:
                    break
                nhash = blake2b(data, digest_size=32).hexdigest()

        input(f'Here is the hash for "{file}".\n\nblake2b hash: {nhash}\n\nPress "enter" to continue...')
    else:
        print(f'The file with the name "{file}" does not exist in the current directory.\n\nPress "enter" to continue...')
        quit()
# End of Check Hash




# Compare hash
def compare(fhash):
    file = input('File to compare hash against. - (Drag & Drop): ').replace('\\ ', ' ').strip().replace("'", "")

    if file_exists(file):
        clear()

        buffer_size = 65536

        with open(file, 'rb') as fh:
            while True:
                data = fh.read(buffer_size)
                if not data:
                    break
                nhash = blake2b(data, digest_size=32).hexdigest()
        return (
            input(
                f'The hash you provided matches the hash of {file}\n\nYour hash - (blake2b): {fhash}\nFile hash - (blake2b): {nhash}\n\nPress "enter" to continue...'
            )
            if fhash == nhash
            else input(
                f'The hash you provided does not match the hash of {file}\n\nYour hash - (blake2b): {fhash}\nFile hash - (blake2b): {nhash}\n\nPress "enter" to continue...'
            )
        )

    else:
        input(f'The file with the name "{file}" does not exist in the current directory.\n\nPress "enter" to continue...')
        quit()
# End Compare hash



def split_string(s_str,count=10):
    per_c=math.ceil(len(s_str)/count)
    c_cout=0
    out_str=''
    split_list=[]
    for s in s_str:
        out_str+=s
        c_cout+=1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str=''
            c_cout=0
    if c_cout!=0:
        split_list.append(out_str)
    return split_list



def count_frames(vid):
    video = cv2.VideoCapture(vid)
    total = 0
    
    try:
        total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    except Exception as e:
        print(f'Could not get frames of the video to count.\n\nError: {e}\n')
        total = 0

    video.release()
    return total


def compute(video):
    if not os.path.exists(".tmp"):
        os.makedirs(".tmp")
    temp_folder=".tmp"
        
    vidcap = cv2.VideoCapture(video)
    count = 0
    
    while True:
        success, image = vidcap.read()
        if not success:
            break
            
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1
        yield

        
def frame_extraction(video):
    print("[INFO] tmp directory is being created. Please be patient!")
    total = count_frames(video)
    with alive_bar(total) as bar:
        for _ in compute(video):
            bar()
    print('[INFO] Done!')

        
def encode_string(input_string,root=".tmp/"):
    split_string_list=split_string(input_string)
    for i in range(len(split_string_list)):
        f_name = f"{root}{i}.png"
        secret_enc=lsb.hide(f_name,split_string_list[i])
        secret_enc.save(f_name)
        print(f"[INFO] frame {f_name} holds {split_string_list[i]}")
    clear()



def clean_tmp(path=".tmp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] tmp files have been cleaned up.\n")


def decode_string(video):
    frame_extraction(video)
    secret=[]
    root=".tmp/"
    for i in range(len(os.listdir(root))):
        f_name = f"{root}{i}.png"
        secret_dec=lsb.reveal(f_name)
        if secret_dec is None:
            break
        secret.append(secret_dec)

    result = ''.join(list(secret))
    clear()
    print("[INFO] Cleaning up tmp files...")
    clean_tmp()
    return result



def genData(data):
    return [format(ord(i), '08b') for i in data]



def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        # Extracting 3 pixels at a time
        pix = list(
            imdata.__next__()[:3]
            + imdata.__next__()[:3]
            + imdata.__next__()[:3]
        )


        # Pixel value should be made odd for 1 and even for 0
        for j in range(8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1


        # The 8th pixel of every set tells it whether to stop or read further. 0 means keep reading, 1 means the message is over.
        if (
            (i == lendata - 1)
            and (pix[-1] % 2 == 0)
            and (pix[-1] != 0)
            or i != lendata - 1
            and (pix[-1] % 2 != 0)
        ):
            pix[-1] -= 1
        elif (i == lendata - 1) and (pix[-1] % 2 == 0):
            pix[-1] += 1

        pix = tuple(pix)
        yield pix[:3]
        yield pix[3:6]
        yield pix[6:9]




# Putting modified pixels into the new image
def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1




# Encodes/injects your data into the image
def encode():
    clear()
    img = input("Image file - (Drag & Drop): ").replace('\\ ', ' ').strip().replace("'", "")
    if file_exists(img):
        image = Image.open(img, 'r')
 
        data = input("Enter data to be injected: ")
        if (len(data) == 0):
            raise ValueError('You need to provide data/text to inject into the image.')

        key_data = input("Input data to make encryption key (100+ characters in length minimum): ")
        if len(key_data) < 100:
            raise ValueError("Key must be 100 characters in length or more!")

        gcm.clear()
        bkey = bytes(key_data, 'utf-8')
        data = bytes(data, 'utf-8')
        key = gcm.keygen(bkey)
        save_me = base64.b64encode(key)
        input(f'Save this key for decrypting later: {save_me.decode()}\n\nPress "enter" to continue...')
        gcm.clear()

        data_enc = gcm.stringE(enc_data=data, key=key)

        newimg = image.copy()
        encode_enc(newimg, data_enc)
    
        new_img_name = input("Save image as (with extension): ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
        clear()
        input(f'SAVED!\nFile with injected data saved as: {new_img_name}\n\nPress "enter" to continue...')
        clear()
    else:
        clear()
        raise ValueError("I can't find the file..it does not exist where specified or isn't a file.")




# Decodes your data in the image
def decode():
    clear()
    img = input("Image File - (Drag & Drop): ").replace('\\ ', ' ').strip().replace("'", "")
    clear()

    if file_exists(img):
        image = Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())

        while True:
            pixels = list(
                imgdata.__next__()[:3]
                + imgdata.__next__()[:3]
                + imgdata.__next__()[:3]
            )

            #String of binary data
            binstr = ''.join('0' if (i % 2 == 0) else '1' for i in pixels[:8])

            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data
    else:
        clear()
        raise ValueError("I can't find the file..it does not exist where specified or isn't a file.")

#------------End of Functions Library------------#

if __name__ == '__main__':
    pass
