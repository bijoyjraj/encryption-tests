import imageencryption as ie

f1 = raw_input("Enter the name of the encrypted imagefile without extension  : ")
i2 = raw_input("Enter the name of the decrypted imagefile without extension  : ")
rows = input("Enter no of rows in the image : ")
columns = input("Enter no of columns in the inage : ")
channels = input("Enter no of channels in the image : ")
Password = raw_input("Enter the Password for the image : ")

ie.decrypt(f1,i2,Password,rows,columns,channels)
