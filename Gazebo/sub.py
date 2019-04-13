#!/usr/bin/env python
import numpy as np
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt

#kernel = np.ones((5,5),np.float32)/255  For Morphological Transforms

def getYellow(frame):		#Extracting Yellow colour
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_yellow = np.array([20,100,100])
	upper_yellow = np.array([30,255,255])
	#img = cv2.morphologyEx(hsv,cv2.MORPH_CLOSE,kernel)	
	mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
	res = cv2.bitwise_and(frame,frame,mask=mask)
	#cv2.imshow('mask',mask)
	return mask,res

def getBlue(frame):			#Extracting Blue colour
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_blue = np.array([100,50,50])
	upper_blue = np.array([130,255,255])
	#img = cv2.morphologyEx(hsv,cv2.MORPH_CLOSE,kernel)	
	mask = cv2.inRange(hsv,lower_blue,upper_blue)
	res = cv2.bitwise_and(frame,frame,mask=mask)
	return mask,res

def roi(frame):			#Cropping out the sky
	x = frame.shape[1]
	y = frame.shape[0]
	crop_img = frame[195:x,0:2*y]
	return crop_img

def boundingboxes(frame,mask):		#Finding contours 
	border = cv2.copyMakeBorder(mask,top=195,bottom=0,left=0,right=0,borderType=cv2.BORDER_CONSTANT)
	_,conts,_ = cv2.findContours(border.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(frame,conts,-1,(255,0,0),3)
	for i in range(len(conts)):
		x,y,w,h = cv2.boundingRect(conts[i])
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		#rect = frame[y:y+h,x:x+w]
		#cv2.imshow('cone',rect)
		#cv2.waitKey(0)


bridge = CvBridge()			

def image_callback(data):
	try:
		frame = bridge.imgmsg_to_cv2(data,"bgr8")
	except CvBridgeError as e:
		print(e)
	#img = cv2.morphologyEx(frame,cv2.MORPH_CLOSE,kernel)	
	roiimg = roi(frame)
	ymas,yres = getYellow(roiimg)
	bmas,bres = getBlue(roiimg)
	cv2.imshow('resyellow',yres)
	cv2.imshow('resblue',bres)
	try:		#Creating bounding boxes for yellow and blue cones
		boundingboxes(frame,ymas)
		boundingboxes(frame,bmas)
	except:
		pass
	cv2.imshow('frame',frame)
	cv2.waitKey(3)


if __name__=='__main__':
	rospy.init_node('image_converter',anonymous=True)		#ROSbridge
	image_sub = rospy.Subscriber("/zed/left/image_raw",Image,image_callback)
	try:
		rospy.spin()
	except rospy.ROSInterruptException:
		print("shutting down")
	cv2.destroyAllWindows()
	