import skimage as sk
import skimage.io as skio
import random
import sys
inputimg = "fisat3.jpg"
outputimg = "fisat4.jpg"
pwd = raw_input("PASSWORD :")
Pwd = list(pwd)
image = skio.imread(inputimg)
row,col,ch = image.shape
pl = len(Pwd)
pp = 0
c = 0
for i in range(row):
    for j in range(col):
        for k in range(ch):
            ival = image[i,j,k]
            pval = ord(Pwd[pp]) % 256
            pp += 1
            if pp >= pl:
                pp = 0
            val = (ival - pval) % 256
            image[i,j,k] = val

skio.imsave(outputimg,image)
