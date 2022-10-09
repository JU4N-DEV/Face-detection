from pyfiglet import Figlet
#By:JUANHG (T4RS)
pyf = Figlet(font='big',width=10 )
pyg = Figlet(font='epic', width=10,)
a = pyf.renderText("Reconocimiento Facial")
b = pyg.renderText("by: Juan")

print(a)
print(b)


import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)

while(True):
    ret,frame = vid.read()
    faces = face_cascade.detectMultiScale(frame)

    for (x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()