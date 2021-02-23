from django.conf import settings
import numpy as np
import cv2

def opencv_dface(path):
    img = cv2.imread('media/images/2021/02/23/1YYTXFF17O_1.jpg')
    
    if (type(img) is np.ndarray):
        print(img.shape)
    
        baseUrl = settings.MEDIA_ROOT + settings.MEDIA_URL
        print(baseUrl)
        face_cascade = cv2.CascadeClassifier('D:/Project/opencv_webapp/opencv_webapp/media/' + 'haarcascade_frontface.xml')
        eye_cascade = cv2.CascadeClassifier('D:/Project/opencv_webapp/opencv_webapp/media/' + 'haarcascade_eye.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x: x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imwrite('media/images/2021/02/23/1YYTXFF17O_1.jpg', img)

    else:
        print('something error')
        print(path)