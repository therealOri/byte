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
> Hashing means using some function or algorithm to map object data to some representative integer value.
This so-called hash code (or simply hash) can then be used as a way to narrow down our search when looking for the item in the map. Or to compare files to see if they match/are the same.

With this being said, You can use the new "Check Hash" function to get the hash of your art!

Example (Of a test file called `Arch_btw.png`):
 - No Datamark: `6db87cd806d5cfbaebd928dfd1dd14888c39767415f4fcac180ccf69b2dbbfcb` | Anyone removing datamark in the hex code/data will get this hash value.
- Datamark: `c2b494018149d9964876fdddd2535786fac09de179882bc7c4bcc3b9b4e5db9b` | Anyone not removing the datamark will get this hash value. | Watermark/Datamark is --> "This art is made by: Ori#6338 (On Discord)."

As you can see, The hashes are completely different and can let you or others know, which image/art is the original and came from you!



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
