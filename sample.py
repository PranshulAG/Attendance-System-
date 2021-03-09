import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\13054\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")


def face_extractor(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None

    for (x, y, w, h) in faces:
        crop = img[y:y + h, x:x + w]

    return crop


cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (300, 300))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = 'C:/Users/13054/Downloads/faces/user'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)

        cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("face crop", face)
    else:
        print("Face Not Found")
        pass

    if cv2.waitKey(1) == 13 or count==50:
        break


cap.release()
cv2.destroyAllWindows()
print("Samples Collected!!")
