import cv2
from ipywidgets import interact, Button

# Feature Controls
window_width = 700
window_height = 700
window_one = 'base_image'
window_two = 'result_image'

# UI bits
close_button=Button(
        description='Close Feed',
        style = {'description_width': 'initial'},
        disable=False)

# Face cascade - used to detect face (front facing)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Actual video feed
vc = cv2.VideoCapture(0)

# Comparative windows
cv2.namedWindow(window_one, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(window_two, cv2.WINDOW_AUTOSIZE)

# Adjust position of above windows to be side-by-side
cv2.moveWindow(window_one, 0, 100)
cv2.moveWindow(window_two, 400, 100)

# Start the window for what was set up above
cv2.startWindowThread()
