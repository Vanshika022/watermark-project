import cv2
import time
import cvzone.HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector()

while True:
    ret, frame = cap.read()
    frame= detector.findHands(frame)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, f'FPS:{int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow('frame', frame)
    #cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
#cv2.destroyAllWindows()

