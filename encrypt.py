import skimage as sk
import skimage.io as skio

class img :
    def encrypt(self,Inpf, Outf, Pass):
        self.image = skio.imread(Inpf,True)
        self.image = sk.img_as_uint(self.image)
        pass = unicode(Pass)
        for i in self.image:
            for j in i:
                

        skio.imsave(Outf,self.image)


inputImage1 = img()
inputImage1.encrypt("fisat.jpg","fisat3.jpg","")
