import cv2 

video = cv2.VideoCapture(0) 
if not video.isOpened():
    video = cv2.VideoCapture(1) 

while True:
    ret, frame = video.read() 
    cv2.imshow('frame',frame) 
    if cv2.waitKey(1) & 0xFF: 
        break 
video.release() 
cv2.destroyAllWindows()