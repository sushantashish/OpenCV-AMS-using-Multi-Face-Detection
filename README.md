# OpenCV-AMS-using-Multi-Face-Detection
Attendance Management System using Face Recognition
This project is made using OpenCV v3.3.1 and uses CSV to store the recorded faces to mark attendance.

Requirements:
  Python 2.7
  OpenCV 3.0+
  SQLite
  (Other prerequisites should be present in the OpenCV installation requirements)
  
  File Description:
  1. datasetcreate.py- Creates an entry in a database and captures pictures of users in DataSet folder
  2. trainer.py- Trains the image and stores it in trainer.yml
  3. detector.py- The main program. It detects the faces and recognizes the recorded faces and updates the attendance in a csv file
  

