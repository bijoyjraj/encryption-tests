import skimage as sk
import skimage.io as skio
inputimg = "fisat3.jpg"
outputimg = "fisat4.jpg"
image = skio.imread(inputimg)
out = image
row,col,ch = image.shape
pval = 0
nval = 0
for k in range(3):
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                out[i,j,k] = image[i,j,k]
            elif j == 0 and i != 0:
                out[i,j,k] = out[i - 1,col - 1,k] + image[i,j,k]
            else:
                out[i,j,k] = out[i,j-1,k] + image[i,j,k]

skio.imsave(outputimg,out)
print out[0,0],out[0,1],image[0,0],image[0,1]
