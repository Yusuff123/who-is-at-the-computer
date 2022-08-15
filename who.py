import cv2
import time
import os
import datetime

CAMERAID = 0
PATH = ''
NAMING = '%Y-%m-%d--%H-%M-%S'
EXTENSION = '.jpg'
INTERVAL = 10

def capture_image() -> None:
    cap = cv2.VideoCapture(CAMERAID)
    ret, frame = cap.read()
    cap.release()

    if ret and frame is not None:
        image_name = datetime.datetime.today().strftime(NAMING) + EXTENSION
        cv2.imwrite(os.path.join(PATH, image_name), frame)

while True:
    capture_image()
    time.sleep(INTERVAL)