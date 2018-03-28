import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def insertOrUpdate(Id,name):	
	conn= sqlite3.connect("facebase")
	cmd="SELECT ID,Name FROM student WHERE ID="+str(Id)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if(isRecordExist==1):
		cmd="UPDATE student SET Name="+str(name)+"WHERE ID="+str(Id)
	else:
		cmd="INSERT INTO student Values("+str(Id)+","+str(name)+")"
	conn.execute(cmd)
	conn.commit()
	conn.close()

Id=raw_input('Enter your ID: ')
name=raw_input('Enter your Name: ')
insertOrUpdate(Id,name)
sampleNum=0
while(True):
	ret, img = cam.read()
	if ret is True:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	else:
		continue    
	faces = detector.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
         
                sampleNum=sampleNum+1
        
                cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('frame',img)
     
	if cv2.waitKey(100) & 0xFF == ord('q'):
        	break
    
	elif sampleNum>50:
        	break
cam.release()
cv2.destroyAllWindows()


