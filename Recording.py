# imports
import cv2
import numpy as np

#Found cam calib constants
ret = 0.3316338761548716
cameraMatrix = np.array([[715.03132426, 0.0, 462.25626965],
 [0.0, 715.67733789, 265.2425816],
 [0.0,        0,              1]])
dist = np.array([[0.05515529], [-0.20330285], [-0.00108968], [-0.00468666], [0.25046973]])

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # change this value until you get the correct cam
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# print(height)
# print(width)

fourcc = cv2.VideoWriter_fourcc(*'MJPG') #*'mp4v' *'MJPG'
out = cv2.VideoWriter('250PWM.avi', fourcc, 30.0, (width, height), isColor=True)

while True:
    _, img = cap.read()
    # resizing for faster processing
    img = cv2.resize(img, (width,height), interpolation = cv2.INTER_LINEAR)
       
    newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (width,height), 1, (width,height))

    # # # Undistort
    dst = cv2.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

    # # crop the image
    # x, y, w, h = roi
    # dst = dst[y:y+h, x:x+w]

    out.write(dst)
    cv2.imshow("Robot Tracking", dst)
   
    # 'Esc' key to exit video streaming
    key = cv2.waitKey(1)
    if key ==27:
        break
   
cap.release()
out.release()
cv2.destroyAllWindows()