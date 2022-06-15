
import sys
import os
from PIL import Image

# assigns command line args to variables
# argv[1] = folder containing original images
# argv[2] = new folder to hold png images
folder = sys.argv[1]
new = sys.argv[2]

# creates list of all images in the given folder
fs = os.listdir(folder)

# creates folder for new png images
if not os.path.exists(new):
    os.makedirs(new)

# loops through images, converts to png and saves to new folder
for i in fs:
    im = Image.open(f'{folder}{i}')
    raw_name = os.path.splitext(i)[0]
    im.save(f'{new}{raw_name}.png', 'png')


