import skimage as sk
import skimage.io as skio

image = skio.imread("fisat.jpg",False)
uimage = sk.img_as_uint(image)

Pass = raw_input("Enter password :")
uPass = int(Pass.encode('hex'),16)
uPass %= 65536
print image.shape
print uPass
print uimage[0,0]
u = (uimage[0,0,0] + uPass) % 65536
u2 = (u - uPass) % 65536
print u, u2
u = u ^ uPass
print u
u = u ^ uPass
print u
