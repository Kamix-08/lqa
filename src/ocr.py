import tesserocr

def get_text(image) -> str:
    tesserocr.image_to_text(image)