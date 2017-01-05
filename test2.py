import skimage as sk
import skimage.io as skio
inputimg = "fisat3.jpg"
outputimg = "fisat4.jpg"
image = skio.imread(inputimg,False)
row,col,ch = image.shape
uimage = sk.img_as_uint(image)
nimage = uimage
Pass = raw_input("Enter password :")
uPass = int(Pass.encode('hex'),16)
uPass %= 65536
for i in range(row):
    for j in range(col):
        for k in range(ch):
            nimage[i,j,k] = (uimage[i,j,k] - uPass) % 65536
            nimage[i,j,k] = (nimage[i,j,k]).decode('hex')
#nimage = sk.img_as_ubyte(nimage)
skio.imsave(outputimg,nimage)
'''
print image.shape
print uPass
print uimage[0,0,0]
u = (uimage[0,0,0] + uPass) % 65536
u2 = (u - uPass) % 65536
print u, u2
'''
