import cv2
import csv
import pandas as pd
import time
import datetime
import numpy as np
import sqlite3
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

def getProfile(Id):
	conn=sqlite3.connect("facebase")
	cmd="SELECT * FROM student WHERE ID="+str(Id)
	cursor=conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close
	return profile

from_date = datetime.datetime.today()

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale=1
fontColor=(255,255,255)
cond=0
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        profile=getProfile(Id)
	if(profile!=None):
		with open('log.csv', 'a') as csv_file:
	
			profile=getProfile(Id)
     			fieldnames = ['ID', 'Name', 'Date']
     			thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames)

     			
                        x1=str(from_date)
     			thewriter.writerow({'ID':str(profile[0]), 'Name':str(profile[1]), 'Date':x1[0:11]})
	        cv2.putText(im,str(profile[0]), (x,y+h),font, fontScale, fontColor)
		cv2.putText(im,str(profile[1]), (x,y+h+30),font, fontScale, fontColor)
                
    cv2.imshow('im',im)
    
    
 
    if cv2.waitKey(10) & 0xFF==ord('q') :
        break
data=pd.read_csv('log.csv')
df_clean=data.drop_duplicates(subset=['ID','Name','Date'])
df_clean.to_csv('nlog.csv')
cam.release()
cv2.destroyAllWindows()
