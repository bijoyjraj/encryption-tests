import skimage as sk
import skimage.io as skio
inputimg = "fisat.jpg"
outputimg = "fisat3.jpg"
image = skio.imread(inputimg)
print image[0,0],image[0,1]
out = image
row,col,ch = image.shape
for k in range(3):
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                pval = 0
            elif j == 0 and i != 0:
                pval = image[i - 1,col - 1,k]
            else:
                pval = image[i,j-1,k]
            nval = image[i,j,k]
            out[i,j,k] = nval - pval
skio.imsave(outputimg,image)
print out[0,0],out[0,1],image[0,0],image[0,1]
