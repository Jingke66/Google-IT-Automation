#!/usr/bin/env python3

from os import listdir
from PIL import Image

# set image dir
img_dir = "supplier-data/images/"

# set variables of image changes
img_new_size = (600, 400)
img_new_format = "JPEG"

# loop to change each image
for img_file in os.listdir(img_dir):
    if img_file.endswith(".tiff"):
        split_name = img_file.split(".")[0]
        img_new_name = split_name + ".jpeg"
        
    new_img = Image.open(img_file).convert("RGB").resize(img_new_size)
    new_img.save(img_dir + img_new_name, img_new_format)

