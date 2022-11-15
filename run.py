#!/usr/bin/env python3

from os import listdir
import requests
import json

# define variables of fruits, keys and values
fruits = {}
keys = ["name", "weight", "description", "image_file"]
values = []

# set text dir
txt_dir = "supplier-data/descriptions/"

# set url
url = "http://localhost/fruits"

for txt_file in os.listdir(txt_dir):
    file_name = file.split(".")[0]
    img_file = file_name + ".jpeg"
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
        name, weight, description = lines
        
    # remove " lbs" from weight and reformt integer
    weight = int(weight.replace(" lbs", ""))
    
    # fill data into dictionary
    values = [name, weight, description, img_file]
    fruits = dict(zip(keys, values))
    
    # upload txt file and image file
    response = requests.post(url, json = fruits)
    if response.ok:
        continue
    else:
        print(f"Error: {response.status_code}")
        
    fruits.clear()
    
