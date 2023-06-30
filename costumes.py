import sys
from PIL import Image

images = []

# receives a list of filenames (gifs) as command line arguments and 
# creates a list of those images
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# concatenate the list of images into a single gif, using the pillow library
# which results in an animated gif
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
