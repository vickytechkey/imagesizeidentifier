import os
from PIL import Image
directoryName = 'assets/'
iamges = os.listdir(directoryName)


for filename in iamges :
    print(filename)

# im = Image.open("sample.png")
# print(im.size[0])
