# Byte
Steganography Image/Data Injector. For artists or people to inject their own Datamark "Watermark" into their images/art or files!
__ __

Update | 8/10/2022:

Warning: The bigger the video, the more frames it'll need to extract..which means longer wait times. It may take a while for bigger video files.. Gifs are also still unsupported as of now, still looking into how to get that to work.

> - Updated the menu so things work smoother and looks a bit cleaner.
> - Added some more print messages to let you know what's happening at certain times.

__ __
<br />

# TODO
> - `.gif file support` [Help Wanted!]
> - `Better way of encoding data into video files. (Without frame extraction)` [Help Wanted!]
> - `Extract frames faster for larger/longer videos.` [Help Wanted!]
__ __

<br />
<br />

# Hashing
> "Hashing" is the process of scrambling raw information to the extent that it cannot be reproduced back into its original form. It takes a piece of information and passes it through a function that performs mathematical operations. This function is called the hash function, and the output is called the hash value/digest. And hash values/hashes can be used to compare files or text to see if they match or are the same.

With this being said, You can use the new "Check Hash" function to get the hash of your art!

 <br />

Examples (Of test files called `Arch_btw_no_datamark.png` and `Arch_btw_datamark.png`):
 - No Datamark: `1f82f21419729c3e3c39702cdf98815371571f8fa11327fcd80b0cb77fef2bea` | This hash value is of the file before you would add your datamark or edit the file. (original art/image hash)
 
- Datamark: `d45bd77ee6c3fc53b13298d72dd23994eddcd891ef1f8794e54b6188356e9eca` | This hash value is of the file after you have added a datamerk. | Watermark/Datamark is --> "This art is made by: Ori#6338 (On Discord). <3"

- Changed Datamark: `d5bde81df87f826a48464775e5eff69ea6fb319f0b9325ceda2f6de5c4358b95` | If anyone changed your datamark to something else, they will get a different hash value all together. | Watermark/Datamark changed/edited to --> "This art is made by: SomeGuy#1234 (On Discord) <3"

- Edited File: `87c8f58043e5877350d679cea697d601df98b85e78e1145e47e1b2a8d5428822` | This hash value is what I got when I edited the image/art and exported it as a png, etc. after already giving it my datamark.

 <br />

As you can see, The hashes are completely different and can let you or others know, which image/art is the original that came from you!
__ __

- Find out more about "what is hashing" [here!](https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm#what_is_hashing)
- [blake2b hashlib documentation](https://docs.python.org/3/library/hashlib.html#blake2)
- [blake2b website](https://www.blake2.net)



<br />
<br />

# Installation/Links
- [Python3 | Direct (Windows 10)](https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe)
- [Python3 | Website](https://www.python.org)
- [Git Download](https://git-scm.com/downloads)
- [Python3 venv documentation](https://docs.python.org/3/library/venv.html)

```bash
git clone https://github.com/therealOri/byte.git
cd byte

python3 -m venv bytENV
source bytENV/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

python3 byte.py

deactivate
(For leaving the venv when done. Or just close the terminal/cmd window.)
```
> If you do not know how to install anything or if you are unsure how to do things. I highly encourage you to create/make an issue or hop on over to our discussions area and I'll happily help you out!

[Byte Discussions](https://github.com/therealori/byte/discussions)
__ __

<br />
<br />

# Supported Filetypes
Your favorites:
> - [x] PNG
> - [x] JPG/JPEG

[More here](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)

<br />

# Unsupported Filetypes
> - [x] GIF

<br />
<br />

# Notes:
> - This will **not** affect image quality or anything else to do with the image. It will be exactly the same to the naked eye.
> - This code does not inject files/images into said image. I may make a seperate file in this repo for that.
> - You need python3 in order to use this. (Very easy to get/install and use)
> - If you want to make this code cleaner, better, more optimized, or add onto the code. Please make a pull request and push your code for me to review.
> - Hashing does **Nothing** to the image/art or image/art quality. Your art will still look, feel, and be the same.
