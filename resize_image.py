#!/usr/bin/env python3
from PIL import Image
import os.path 

in_path = 'forest.png'
out_width = 800

image = Image.open(in_path)
width, height = image.size
ratio = out_width / width
out_height = int(height * ratio)
image = image.resize((out_width, out_height), Image.ANTIALIAS)
file_root, file_ext = os.path.splitext(in_path)
out_path = f'{file_root}.{out_width}x{out_height}{file_ext}'
image.save(out_path)
