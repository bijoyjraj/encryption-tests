import skimage as sk
import skimage.io as skio

img_in = "fisat.jpg"
img_out = "encrypted.jpg"

image = skio.imread(img_in)
image = sk.img_as_float(image)
#print image
PWD = input("enter a numerical (integer) password : ")

row,col,ch = image.shape

for k in range(ch):
    for i in range(row):
        for j in range(col):
            val = image[i,j,k]
            nval = val / PWD
            image[i,j,k] = nval

skio.imshow(image)
skio.show()

for k in range(ch):
    for i in range(row):
        for j in range(col):
            val = image[i,j,k]
            nval = val * PWD
            image[i,j,k] = nval
skio.imshow(image)
skio.show()
