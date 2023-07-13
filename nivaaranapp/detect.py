from ultralytics import YOLO
from PIL import Image
import time,os
from io import BytesIO

from nivaaransite.settings import BASE_DIR
model = YOLO(os.path.join(BASE_DIR,'media','models','uploads','violence.pt'))

# image = Image.open("nivaaranapp\\sample.jpg")

def convertToByteArray(image):
    byte_data = bytearray(image.tobytes())
    return byte_data

def convertToImage(byte_data,w,h):
    image = Image.frombytes("RGB", (w, h), byte_data)
    return image

# sample = convertToByteArray(image)

def detect(img):
    # bImg= convertToByteArray(img)
    bImg=img.read()
    stream = BytesIO(bImg)

# Open the image using PIL
    image = Image.open(stream)

    # Get the size (dimensions) of the image
    width, height = image.size
    
    print(width)
    print(height)
    model.predict(source=image, show=True, conf=0.5)

    return {
        "confidence" : "",
        "is_violence": True
    }
