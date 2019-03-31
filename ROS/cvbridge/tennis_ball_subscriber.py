
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
    yellowLower =(30, 150, 100)
    yellowUpper = (50, 255, 255)
    
    gray_image = read_rgb_gray_video(frame, False, True)
    binary_image_mask = filter_color(gray_image, yellowLower, yellowUpper)    
    contours = getContours(binary_image_mask)
    draw_ball_contour(binary_image_mask, gray_image,contours)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        

def read_rgb_gray_video(frame, gray, blur):
    
    if gray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if blur:
        frame = cv2.GaussianBlur(frame, (5, 5), 0) 
    cv2.imshow("Frame from fn1",frame)
    return frame ###NO TAB

def convert_gray_to_binary(gray_image, adaptive, show):
    if adaptive:
        binary_image = cv2.adaptiveThreshold(gray_image, 
                            255, 
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                            cv2.THRESH_BINARY_INV, 5, 2)
    else:
        _,binary_image = cv2.threshold(gray_image,60,255,cv2.THRESH_BINARY_INV)
    if show:
        cv2.imshow("Binary Image", binary_image)
    return binary_image

def getContours(binary_image):      
    _, contours, hierarchy = cv2.findContours(binary_image.copy(), 
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
    return contours

def filter_color(rgb_image, lower_bound_color, upper_bound_color):
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image",hsv_image)
    yellowLower =(30, 150, 100)
    yellowUpper = (50, 255, 255)

    #define a mask using the lower and upper bounds of the yellow color 
    mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)

    return mask

def draw_ball_contour(binary_image, rgb_image, contours):
    black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3],'uint8')
    
    for c in contours:
        area = cv2.contourArea(c)
        perimeter= cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if (area>3000):
            cv2.drawContours(rgb_image, [c], -1, (150,250,150), 1)
            cv2.drawContours(black_image, [c], -1, (150,250,150), 1)
            cx, cy = get_contour_center(c)
            cv2.circle(rgb_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),5,(150,150,255),-1)
            print ("Area: {}, Perimeter: {}".format(area, perimeter))
    print ("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours",rgb_image)
    cv2.imshow("Black Image Contours",black_image)

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx= int(M['m10']/M['m00'])
        cy= int(M['m01']/M['m00'])
    return cx, cy


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('camera_image', Image, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
cv2.waitKey(0)
cv2.destroyAllWindows()