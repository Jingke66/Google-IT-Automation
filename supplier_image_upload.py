#!/usr/bin/env python3

import requests
import os

# set url and image dir
url = "http://localhost/upload/"
img_dir = "supplier-data/images/"

# loop to open image files and upload to website
for img_file in os.listdir(img_dir):
    if img_file.endswith(".jpeg"):
        with open(img_file, "rb") as opened:
            r = requests.post(url, files={"file": opened})
            
    