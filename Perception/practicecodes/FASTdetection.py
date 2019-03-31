import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fast = cv2.FastFeatureDetector_create(20)

while True:
	_, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
		rect = frame[y:y+h,x:x+w]

		kp = fast.detect(rect,None)
		img = cv2.drawKeypoints(rect,kp,None)

		fast.getThreshold()
		fast.getNonmaxSuppression()
		fast.getType()

	cv2.imshow('original',frame)
	cv2.imshow('detect',img)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()