
'''
                   Multiple Images Resizing
'''

# Import Important library
from PIL import Image
import os
# Initialized Pixel Size
image_size = (300,300)

for file in os.listdir("D:\\work\\Dr\\data\\"):

    # Select image files(.tif) from file
    if file.endswith('.tif'):
        a = file

        # Creating image object k
        k = Image.open(a)

        # resize image without any changes in original image
        k.thumbnail(image_size)

        # Save image in to resize foler
        k.save("resize/{}".format(a))