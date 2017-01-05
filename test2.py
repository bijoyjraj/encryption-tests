import skimage as sk
import skimage.io as skio
import random
import numpy as np

img_in = "fisat"
img_out1 = "encrypted"
img_out2 = "decrypted"

def create_pass():
    pw = []
    while len(pw) < 10:
        t = chr(random.randint(35,126))
        if t not in pw:
            pw.append(t)
    return str().join(pw)
#ENCRYPTING IMAGE
image = skio.imread(img_in + ".jpg")
PWD = create_pass()
print image
r,c,ch = image.shape

f = open(img_out1 + ".txt",'w')
string = ""
for i in range(r):
    for j in range(c):
        for k in range(ch):
            n = str(image[i,j,k])
            for val in n:
                string += PWD[int(val)]
            string += " "
#print string
f.write(string)
f.close()

#DECRYPTING image
f = open(img_out1 + ".txt", 'r')
string = f.read()
f.close()
string = string.split()
vlist = []
for i in string:
    val = ""
    for j in i:
        val += str(PWD.index(j))
    vlist.append(int(val))

#creating image
nimage = np.zeros((r,c,ch),dtype = np.uint8)
print nimage
index = 0
while index < len(vlist):
    for i in range(r):
        for j in range(c):
            for k in range(ch):
                nimage[i,j,k] = vlist[index]
                index += 1
print nimage
skio.imsave(img_out2 + ".jpg",nimage)
