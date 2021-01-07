import cv2
from ipywidgets import interact, Button

window_name = 'Webcam Feed'

# UI bits
close_button=Button(
        description='Close Feed',
        style = {'description_width': 'initial'},
        disable=False)

cv2.namedWindow(window_name)
vc = cv2.VideoCapture(0)
    
if vc.isOpened(): # Test first frame
    rval, frame = vc.read()
else:
    rval = False

while rval is True:
    cv2.imshow("View", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20) # T key
    if key == 27: # ESC to exit process
        break
vc.release()
cv2.destroyWindow(window_name)
