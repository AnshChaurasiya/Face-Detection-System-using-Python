import cv2
face_cap = cv2.CascadeClassifier("C:/Users/HP/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, video1 = video_cap.read()
    col = cv2.cvtColor(video1,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video1,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video_meow",video1)
    if cv2.waitKey(10) == ord("a"):
      break
video_cap.release()