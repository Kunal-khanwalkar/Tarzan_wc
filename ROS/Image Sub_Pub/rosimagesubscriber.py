
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
bridge = CvBridge()

def callback(data):
    try:
        frame = bridge.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError as e:
        print(e)
    print('Recieved')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.waitKey(3)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('camera_image', Image, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

cv2.destroyAllWindows()