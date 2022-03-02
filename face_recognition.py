import cv2
import dlib
# read the image 
img = cv2.imread("tieu_de_so_ciu.png")

#conver img to grayscale: 3D => 2D
gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)

#dlib: Load Face Recognition Detector
face_detector = dlib.get_frontal_face_detector()

#use detector to find face landmarks 
faces = face_detector(gray)

for face in faces:
    x1 = face.left() #left point
    y1 = face.top() #top poinnt
    x2 = face.right() #right point
    y2 = face.bottom() #bottom poinnt

    #Draw  a rectangle
    cv2.rectangle(img = img, pt1 = (x1, y1), pt2 = (x2, y2),
    color=(0,255,0), thickness=3)
    
#show the image
cv2.imshow(winname="Face Recognition App", mat = img)

#wait for a key press to exit   
cv2.waitKey(delay=0)

#Close All windows
cv2.destroyAllWindows()