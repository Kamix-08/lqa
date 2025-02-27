import tesserocr
from PIL import Image

def preprocess_image(image:Image) -> Image:
    image = image.convert('L')
    image = image.point(lambda x: 0 if x < 128 else 255, '1')

    image.save("image_processed.png")

    return image

def get_text(image:Image) -> str:
    return tesserocr.image_to_text(image)