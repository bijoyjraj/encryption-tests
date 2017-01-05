#importing dependencies
import skimage as sk
import skimage.io as skio
import random
import numpy as np

#creating a random password
def create_pass():
    pw = []
    while len(pw) < 10:
        t = chr(random.randint(35,126))
        if t not in pw:
            pw.append(t)
    return str().join(pw)

#ENCRYPTING THE IMAGE INTO A FILE
def encrypt(inputfile,outputfile):
    #initialising filenames
    img_in = inputfile
    img_out1 = outputfile
    #initialising required values
    image = skio.imread(img_in + ".jpg")
    PWD = create_pass()
    r,c,ch = image.shape
    f = open(img_out1 + ".txt",'w')
    string = ""
    #actual encryption
    for i in range(r):
        for j in range(c):
            for k in range(ch):
                n = str(image[i,j,k])
                for val in n:
                    string += PWD[int(val)]
                string += " "
    #saving encrypted file
    f.write(string)
    f.close()
    #returning password and the 'shape' of the image
    return(PWD,r,c,ch)

#DECRYPTING THE FILE INTO AN IMAGE
def decrypt(inputfile,outputfile,PWD,r,c,ch):
    #initialising filenames
    img_out1 = inputfile
    img_out2 = outputfile
    #initialising required values
    f = open(img_out1 + ".txt", 'r')
    string = f.read()
    f.close()
    string = string.split()
    vlist = []
    #actual decryption
    for i in string:
        val = ""
        for j in i:
            val += str(PWD.index(j))
        vlist.append(int(val))
    #recreating the image
    nimage = np.zeros((r,c,ch),dtype = np.uint8)
    index = 0
    while index < len(vlist):
        for i in range(r):
            for j in range(c):
                for k in range(ch):
                    nimage[i,j,k] = vlist[index]
                    index += 1
    #saving the decrypted image
    skio.imsave(img_out2 + ".jpg",nimage)
