# Face-Recognition-Attendance-System
This project identifies a real-time face recognition-based attendance system along with computer vision and Firebase for backend solutions. This captures live video feed from a webcam, recognizes the faces of the people in the frame, matches them with the face encoding saved in the database and records the attendance.

**Key Components:**
1.Face Detection and Recognition:
(i)For face detection, the system encompasses the face_recognition library for real-time face detection. Pre-defined student faces are already encoded by EncodeGenerator.py script, which takes the student images and converts it into an encoding and saves the encoded data in a pickle file EncodingFile.p, for fast matching.
(ii)In the attendance session (main.py) each face detected in the frames captured from the webcam is matched to known encodings. If there is a match, then the student ID is produced.

2.Firebase Integration:
(i)Firebase Realtime Database and Firebase Storage are employed for both students’ information and attendance records. Firebase Authentication with service account keys assures identity and the database is protected from unauthorized access.
(ii)The script addDataToDatabase.py initially loads student information into Firebase namely; name, course, section, total attendance, time stamp of the last attendance.
(iii)In main.py, information of students (for example, the number of attendances) is taken and changed according to the identified faces.

3.Attendance Management:
(i)For each recognized face, the system retrieves the student's data from Firebase, displays relevant information, and updates the attendance count.
(ii)The GUI is enhanced with background and mode images to provide visual cues about the attendance status. The real-time display overlays the webcam image on a custom background with mode-specific images.

4.Encoding Generator:
The EncodeGenerator.py script processes images of students and generates face encodings. These encodings, along with the student IDs, are saved into a file to facilitate quick comparisons during runtime.

5.Workflow:
(i)Initialization: Load face encodings, initialize Firebase, and set up the webcam feed.
(ii)Real-Time Face Detection: Continuously capture frames from the webcam, resize and convert for efficient processing, and detect faces.
(iii)Face Recognition: Compare detected faces with stored encodings to identify students and fetch attendance data from Firebase.
(iv)Attendance Recording: Update attendance data in Firebase, display information on screen, and visually highlight recognized faces.

This project provides an efficient and automated solution for attendance tracking, ideal for schools, universities, and workplaces. By leveraging face recognition and Firebase, it minimizes manual work, ensures data accuracy, and allows seamless scalability.
