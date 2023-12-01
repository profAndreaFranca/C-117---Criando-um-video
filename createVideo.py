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

frame = cv2.imread(image[0])
height,width,channels = frame.shape
size = (width,height)

output = cv2.VideoWriter("sum.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,size)