from django.conf import settings
import numpy as np
import cv2

def opencv_dface(path):
    img = cv2.imread(path, 1)
    
    if (type(img) is np.ndarray):
        print(img.shape)
    
        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        face_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_eye.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imwrite(path, img)

    else:
        print('something error')
        print(path)

# 웹캠 로직
def opencv_webcam(path):
    cam = cv2.VideoCapture('http://localhost:8000')
    face_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_eye.xml')

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        if ret:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cropped = cv2.resize(frame[y:y+h, x:x+w], (198, 198))
                cv2.rectagle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.destroyAllWindows()
        cv2.imshow('Stram', frame)

