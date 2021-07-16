import cv2
#load pretrained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose image to detect face
#img = cv2.imread('face.jpg')

#capture video
webcam = cv2.VideoCapture(0,  cv2.CAP_DSHOW)
#webcam = cv2.VideoCapture('Mapara_A_Jazz_-_John_Vuli_Gate_[Feat_Ntosh_Gazi_&_Colano]_(Official_Music_Video)(480p).mp4)
#iterate forever over frames
while True:
    
    #read the current frame
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #dEtect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #draw rectangles around faces 
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow('Mutant Face Detector', frame )
    key = cv2.waitKey(1)

    #stop if a or q is pressed
    if key== 97 or key == 113:
        break
#release the videocapture object
webcam.release()

    

    
    






#convert to grascale
"""
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#dEtect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#print(face_coordinates)

#draw rectangles around faces 
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)



#display image on a photo
cv2.imshow('Mutant Face Detector', img)
cv2.waitKey()
"""

print('gone')