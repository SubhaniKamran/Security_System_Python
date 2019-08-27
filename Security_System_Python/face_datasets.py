
# Import OpenCV2 for image processing
import cv2
import sqlite3
# Start capturing video 
vid_cam = cv2.VideoCapture(0)
def InsrtUpdate(id,name,recored,reg):
    conn = sqlite3.connect('Face.db')
    cmd = "SELECT * FROM Detail WHERE id="+str(id)
    cursor = conn.execute(cmd)
    isExist = 0
    for row in cursor:
        isExist=1
    if(isExist==1):
        cmda = "UPDATE Detail SET name="+str(name)+", crminal_recored="+str(recored)+", roll_No="+str(reg)+" WHERE id="+str(id)
    else:
        cmda = "INSERT INTO Detail(id,name,crminal_recored,roll_No) VALUES("+str(id)+","+str(name)+","+str(recored)+","+str(reg)+")"
    conn.execute(cmda)
    conn.commit()
    conn.close()

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = raw_input('Enter ID :')
Name = raw_input('Enter name :')
Record = raw_input('Enter record :')
Reg = raw_input('Enter reg :')
InsrtUpdate(face_id,Name,Record,Reg)

# For each person, one face id

# Initialize sample face image
count = 0

# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count>100:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
