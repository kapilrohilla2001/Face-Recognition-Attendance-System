import os
import pickle
import cv2
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-5ed2f-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-5ed2f.appspot.com"
})

# Initialize webcam
cap = cv2.VideoCapture(0)  # Open webcam (index 0)
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Set webcam resolution
cap.set(3, 315)  # width
cap.set(4, 510)  # height

# Load background image
imgBackground = cv2.imread("Resources/background.png")

# Load mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imageModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in modePathList]

# Load face encodings
print("Loading Encode File ....")
with open('EncodingFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded Successfully")


modeType = 0
counter = 0
id = -1

# Run the webcam feed and process face recognition
while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image.")
        break

    # Resize and convert the image
    img = cv2.resize(img, (315, 510))
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Detect face locations and encodings
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # Update background with webcam image and mode image
    imgBackground[70:70+510, 15:15+315] = img
    imgBackground[0:0 + 600, 420:420 + 380] = imageModeList[modeType]

    # Compare detected faces with known encodings
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("Matches:", matches)
        print("Face Distance:", faceDis)

        matchIndex = np.argmin(faceDis)
        print("Match Index:", matchIndex)

        if matches[matchIndex]:
            # print("Known Face Detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 15 + x1, 70 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)
            id = studentIds[matchIndex]
            # print(id)

            if counter == 0:
                counter = 1
                modeType = 1

    if counter != 0:

        if counter == 1:
            studentInfo = db.reference(f'Students/{id}').get()
            print(studentInfo)

        cv2.putText(imgBackground,str(studentInfo['total_attendance']),)


        counter += 1

        # Further processing can go here (e.g., drawing rectangles or displaying IDs)

    # Display the result
    cv2.imshow("Face Attendance", imgBackground)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
