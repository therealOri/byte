# Byte
Steganography Image/Data Injector. For artists or people to inject their own Datamark "Watermark" into their images/art or files!
__ __

Update | 11/27/2021:
> - New overhaul to code, so even if someone were to edit your watermark out or cover it and then saves/exports your art. Your datamark will still be there in the image's data.
__ __
<br />

# TODO
> - `.gif file support` [Help Wanted!]
__ __

<br />
<br />

# Hashing
> "Hashing" is the process of scrambling raw information to the extent that it cannot be reproduced back into its original form. It takes a piece of information and passes it through a function that performs mathematical operations. This function is called the hash function, and the output is called the hash value/digest. And hash values/hashes can be used to compare files or text to see if they match or are the same.

With this being said, You can use the new "Check Hash" function to get the hash of your art!

 <br />

Examples (Of test files called `Arch_btw_no_datamark.png` and `Arch_btw_datamark.png`):
 - No Datamark: `6db87cd806d5cfbaebd928dfd1dd14888c39767415f4fcac180ccf69b2dbbfcb` | This hash value is of the file before you would add your datamark or edit the file. (original art/image hash)
 
- Datamark: `4f2270017307c5475363d9e9bc0342356079383d77034510035534c9164f03fc` | This hash value is of the file after you have added a datamerk. | Watermark/Datamark is --> "This art is made by: Ori#6338 (On Discord). <3"

- Changed Datamark: `890e9902a2054611cea9460a9806aea8aaa9cd8bbd3bae3a2b2e2802916f3d0e` | If anyone changed your datamark to something else, they will get a different hash value all together. | Watermark/Datamark changed/edited to --> "This art is made by: SomeGuy#1234 (On Discord) <3"

- Edited File: `09b552856d9e355fdbfbf21bfc077ef3233ee809bb8ebc2e85608136e81cdc45` | This hash value is what I got when I edited the image/art and exported it as a png, etc. after already giving it my datamark.

 <br />

As you can see, The hashes are completely different and can let you or others know, which image/art is the original that came from you!
__ __

Find out more about hashing and the sha256 algorithm I use [Here!](https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm)



<br />
<br />

# Installation/Links
- [Python3 | Direct (Windows 10)](https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe)
- [Python3 | Website](https://www.python.org)
- [Git Download](https://git-scm.com/downloads)

```bash
git clone https://github.com/therealOri/byte.git
cd byte
pip3 install requirements.txt
python3 byte.py
```
> If you do not know how to install anything or if you are unsure how to do things. I encourage you to create/make an issue and I'll happily help you out!
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
