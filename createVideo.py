import cv2
import os

path = "Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ["jpg", "jpeg", "png", "gif", "bmp", "webp"]:
        filename = path + "/" + file
        images.append(filename)
count = len(images)
