from PIL import Image

def resize_thumb(path):

    image = Image.open(path)

    image.save(path)
