# import the opencv library
import cv2

#Load the Cascade Classifier File
face_cascade = cv2.CascadeClassifier('C:/Users/Adit Kadiyan/Downloads/c118-FaceDetection-1_4-main/c118-FaceDetection-1_4-main/haarcascade_frontalface_default.xml') 

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
    ret,frame = vid.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w,y+h) ,(255,0,0) , 2)

    cv2.imshow("frame",frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()
cv2.destroyAllWindows()

