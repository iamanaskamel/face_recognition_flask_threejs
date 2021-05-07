import cv2

#model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
#Capture
cap = cv2.VideoCapture(0)
#function of face recognition
def face_recogntion():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#coordinate of face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    ret, jpeg = cv2.imencode('.jpg', frame)
    #final return
    return jpeg.tobytes()
# if cv2.waitKey(1) & 0xff == ord('v'):
#     break
