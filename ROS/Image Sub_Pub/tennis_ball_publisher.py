import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
import sys

VideoCapture = cv2.VideoCapture(0)
#For using video
# video_name = "video/tennis-ball-video.mp4"
# VideoCapture = cv2.VideoCapture(video_name)
bridge = CvBridge()

def detect():
	while True:
		ret,frame = VideoCapture.read()
		
		try:
			talker(frame)
		except rospy.ROSInterruptException:
			pass

		cv2.imshow('webcam',frame)
		k = cv2.waitKey(1) & 0xff
		if k == 27:
			break

def talker(frame):
	pub = rospy.Publisher('camera_image', Image, queue_size=100)
	rospy.init_node('image_publisher', anonymous=True)
	image_message = bridge.cv2_to_imgmsg(frame, "bgr8")
	
	pub.publish(image_message)


if __name__=='__main__':
	detect()

cv2.destroyAllWindows()