from ultralytics import YOLO
from PIL import Image
import time

model = YOLO("media\\models\\uploads\\violence.pt")

image = Image.open("nivaaranapp\\sample.jpg")

def convertToByteArray(image):
    byte_data = bytearray(image.tobytes())
    return byte_data

def convertToImage(byte_data):
    image = Image.frombytes("RGB", (416, 416), byte_data)
    return image

sample = convertToByteArray(image)

def detect():
    model.predict(source=convertToImage(sample), show=True, conf=0.5)
