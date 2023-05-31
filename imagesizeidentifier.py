import os
from PIL import Image


directoryName = 'assets/'
iamges = os.listdir(directoryName)
for filename in iamges:
    imagePath = directoryName + filename
    im = Image.open(imagePath)
    height = im.size[0]
    width = im.size[1]
    if height % 4 == 0:
        if width % 4 == 0:
            print("#################### \n")
            print("\t ImageName : " + imagePath + "\n")
            print("\t ImageWidth : " + str(width) + "\n")
            print("\t ImageName : " + str(height) + "\n")
            print("\t Status :  responsible image" + "\n")
            print("####################")
        else:
            print("####################")
            print("\t ImageName : " + imagePath + "\n")
            print("\t ImageWidth : " + str(width) + "\n")
            print("\t ImageName : " + str(height) + "\n")
            print("\t Status :  Image is not responsible" + "\n")
            print("####################")
    else:
        print("####################")
        print("\t ImageName : " + imagePath + "\n")
        print("\t ImageWidth : " + str(width) + "\n")
        print("\t ImageName : " + str(height) + "\n")
        print("\t Status :  Image is not responsible" + "\n")
        print("####################")
