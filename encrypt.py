import imageencryption as ie

i1 = raw_input("Enter the name of the image without extension  : ")
f1 = raw_input("Enter the name of the encrypted imagefile without extension  : ")
Password,rows,columns,channels = ie.encrypt(i1,f1)
print "Password = " + Password
print "rows = ",rows
print "columns = ",columns
print "channels = ",channels
