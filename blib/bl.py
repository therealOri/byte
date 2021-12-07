from PIL import Image
import os
from os.path import exists as file_exists
import hashlib


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
    img = input("Enter image name(with extension): ")
    if file_exists(img):
        image = Image.open(img, 'r')
 
        data = input("Enter data to be injected: ")
        if (len(data) == 0):
            raise ValueError('You need to provide data/text to inject into the image.')
    
        newimg = image.copy()
        encode_enc(newimg, data)
    
        new_img_name = input("Save image as(with extension): ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
    else:
        clear()
        print(f'The file with the name "{img}" does not exist in the current directory.')
        quit()




# Decodes your data in the image
def decode():
    clear()
    img = input("Enter image name(with extension): ")

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
