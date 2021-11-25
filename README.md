# Byte
Steganography Image/Data Injector. For artists or people to inject their own Datamark "Watermark" into their images/art or files!
__ __
<br />

# TODO
> - [ ] Add more file formats to support.
> - [ ] Clean up code and improve things.
__ __

<br />
<br />

# Hashing
> "Hashing" is the process of scrambling raw information to the extent that it cannot be reproduced back into its original form. It takes a piece of information and passes it through a function that performs mathematical operations. This function is called the hash function, and the output is called the hash value/digest. And hash values/hashes can be used to compare files or text to see if they match or are the same.

With this being said, You can use the new "Check Hash" function to get the hash of your art!

 <br />

Example (Of test files called `Arch_btw_no_datamark.png` and `Arch_btw_datamark.png`):
 - No Datamark: `6db87cd806d5cfbaebd928dfd1dd14888c39767415f4fcac180ccf69b2dbbfcb` | Anyone removing the datamark in the hex code/data will get this hash value. (original art/image hash before you added your datamark.)
 
- Datamark: `c2b494018149d9964876fdddd2535786fac09de179882bc7c4bcc3b9b4e5db9b` | Anyone not removing the datamark will get this hash value. | Watermark/Datamark is --> "This art is made by: Ori#6338 (On Discord)."

- Changed Datamark: `eb85e8254407f6b8491eab57ad63d6860719cafeee5a37103923c6059b8ea0b9` | If anyone changed or edited your datamark, they will get a different hash value all together. | Watermark/Datamark changed/edited to --> "This art is made by: SomeGuy#7830 (On Discord)"

 <br />

As you can see, The hashes are completely different and can let you or others know, which image/art is the original and came from you!
__ __

Find out more about hashing and the sha256 algorithm I use [Here!](https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm)



<br />
<br />

# Installation/Links
- [Python3 | Direct (Windows 10)](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
- [Python3 | Website](https://www.python.org)

```bash
git clone https://github.com/therealOri/byte.git
cd byte
python3 byte.py
```
__ __

<br />
<br />

# Supported Filetypes
> - [x] PNG
> - [x] JPG/JPEG
> - [x] GIF

<br />
<br />

# Notes:
> - This will **not** affect image quality or anything else to do with the image. It will be exactly the same to the naked eye.
> - This code does not inject files/images into said image. I may make a seperate file in this repo for that.
> - You need python3 in order to use this. (Very easy to get/install and use)
> - If you want to make this code cleaner, better, more optimized, or add onto the code. Please make a pull request and push your code for me to review.
> - Hashing does **Nothing** to the image/art or image/art quality. Your art will still look, feel, and be the same.
