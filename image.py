import cv2 


videoCapture = cv2.VideoCapture(2)
if videoCapture.isOpened() == False:
    print("Error opening the video capture")
    quit()

def getFrame():
    if not videoCapture.isOpened(): return None

    ret, frame = videoCapture.read()
    if not ret: return None

    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def release():
    videoCapture.release()
