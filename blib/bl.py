from PIL import Image
import os
from os.path import exists as file_exists
from hashlib import blake2b

import time
import cv2
import numpy as np
import math
import shutil
from stegano import lsb
from subprocess import call, STDOUT
from alive_progress import alive_bar


#------------My functions------------#

def clear():
    os.system('clear||cls')


def banner():
    banner = """

              ██████╗ ██╗   ██╗████████╗███████╗
              ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
              ██████╔╝ ╚████╔╝    ██║   █████╗  
              ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
              ██████╔╝   ██║      ██║   ███████╗
              ╚═════╝    ╚═╝      ╚═╝   ╚══════╝


Made by Ori#6338 | @therealOri_ | https://github.com/therealOri




    """
    return banner



# Check Hash
def check():
    clear()
    buffer_size = 65536

    file = input("Name of the file you want check the hash of?: ")

    if file_exists(file):
        clear()

        with open(file, 'rb') as fh:
            while True:
                data = fh.read(buffer_size)
                if not data:
                    break
                nhash = blake2b(data, digest_size=32).hexdigest()

        print(f'Here is the hash for "{file}".\n\nblake2b hash: {nhash}')
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

        with open(file, 'rb') as fh:
            while True:
                data = fh.read(buffer_size)
                if not data:
                    break
                nhash = blake2b(data, digest_size=32).hexdigest()
        if fhash == nhash:
            p = print(f"The hash you provided matches {file}'s hash!\n\nYour hash - (blake2b): {fhash}\nFile hash - (blake2b): {nhash}")
            return p
        else:
            p = print(f"The hash you provided does not match {file}'s hash!\n\nYour hash - (blake2b): {fhash}\nFile hash - (blake2b): {nhash}")
            return p
    else:
        print(f'The file with the name "{file}" does not exist in the current directory.')
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
    with alive_bar(0) as bar:
        for i in compute(video):
            bar()
    print('[INFO] Done!')

        
def encode_string(input_string,root=".tmp/"):
    split_string_list=split_string(input_string)
    for i in range(0,len(split_string_list)):
        f_name="{}{}.png".format(root,i)
        secret_enc=lsb.hide(f_name,split_string_list[i])
        secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name,split_string_list[i]))
    clear()



def clean_tmp(path=".tmp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] tmp files have been cleaned up.")


def decode_string(video):
    frame_extraction(video)
    secret=[]
    root=".tmp/"
    for i in range(len(os.listdir(root))):
        f_name="{}{}.png".format(root,i)
        secret_dec=lsb.reveal(f_name)
        if secret_dec == None:
            break
        secret.append(secret_dec)
        
    result = ''.join([i for i in secret])
    clear()
    clean_tmp()
    print(f'\n[LOG] Encoded data is: "{result}"')

#------------End of My functions------------#






#------------Credited functions and Stuff------------#
# https://www.geeksforgeeks.org/image-based-steganography-using-python/
# Functions genData(), modPix(), encode_enc(), encode(), and decode() can be creddited to "geeksforgeeks" for the help with the library functions to make this possible. <3
# Hopefully I changed/added enough here to be ok. I'd change more but tbh, I don't exactly know what to change as it's so precise and would probably break if I did.
# To anyone reading this, you are more then welcome to make a push request here on github and edit the functions to work better!
# I am still going to call this whole byte project mine and that I made it.



def genData(data):
        dlist = []
        for i in data:
            dlist.append(format(ord(i), '08b'))
        return dlist



def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):
        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]
 
        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
 

        # The 8th pixel of every set tells it whether to stop or read further. 0 means keep reading, 1 means the message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
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
    img = input("Enter image name (with extension): ")
    if file_exists(img):
        image = Image.open(img, 'r')
 
        data = input("Enter data to be injected: ")
        if (len(data) == 0):
            raise ValueError('You need to provide data/text to inject into the image.')
    
        newimg = image.copy()
        encode_enc(newimg, data)
    
        new_img_name = input("Save image as (with extension): ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
        clear()
        print(f'SAVED!\nFile with injected data saved as: {new_img_name}')
    else:
        clear()
        print(f'The file with the name "{img}" does not exist in the current directory.')
        quit()




# Decodes your data in the image
def decode():
    clear()
    img = input("Enter image name (with extension): ")
    clear()

    if file_exists(img):
        image = Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())
    
        while (True):
            pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
            #String of binary data
            binstr = ''
    
            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'
    
            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data
    else:
        print(f'The file with the name "{img}" does not exist in the current directory.')
        quit()

#------------End of Credited Library------------#


if __name__ == '__main__':
    pass
