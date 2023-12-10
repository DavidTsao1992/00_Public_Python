import os
from PIL import Image

## change the image size under the max_size
def resize_image(image, max_size=1500000):
    image_size = image.size[0] * image.size[1]
    ratio = max_size / image_size
    new_width = int(image.size[0] * ratio)
    new_height = int(image.size[1] * ratio)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return image

def main():
    folder_path = "the source image file path"
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)
        image = resize_image(image)
        image.save(image_path)

if __name__ == "__main__":
    main()
