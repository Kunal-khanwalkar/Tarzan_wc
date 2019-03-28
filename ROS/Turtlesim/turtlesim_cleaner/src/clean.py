#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0 
y = 0
yaw = 0

def poseCallback(pose_message):
    global x  
    global y , yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta
    ##Insert

def position():
    global x , y , yaw
    print ( x , y , yaw)		

def move (speed , distance , is_clockwise):
    global x , y
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0

    if is_clockwise:
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = abs(speed)
    
    distance_travelled = 0.0
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic , Twist , queue_size= 10)

    t0 = rospy.Time.now().to_sec()
    
    while True:
        rospy.loginfo("moving")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        distance_travelled = (t1 - t0)* speed
        loop_rate.sleep()

        if(distance_travelled > distance):
            rospy.loginfo("reached")
            break
    
    velocity_message.linear.x = 0 
    velocity_publisher.publish(velocity_message)
def rotate (angular_speed_degree , relative_angle_degree, clockwise):
    global yaw
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0

    theta0 = yaw
    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z = -(abs(angular_speed))
    else:
        velocity_message.angular.z = abs(angular_speed)
    
    angle_moved = 0.0
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic , Twist , queue_size= 10)

    t0 = rospy.Time.now().to_sec()
    
    while True:
        rospy.loginfo("rotating")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1 - t0)* angular_speed_degree
        loop_rate.sleep()

        if(current_angle_degree > relative_angle_degree):
            rospy.loginfo("reached")
            break
    
    velocity_message.angular.z = 0 
    velocity_publisher.publish(velocity_message)

def go_to_goal(x_goal , y_goal):
    global x,y,yaw
    velocity_message = Twist()
    loop_rate = rospy.Rate(100)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    distance_tolerance=0.01
    while True:
        linear_displacement = abs(math.sqrt(((x_goal-x) ** 2) + ((y_goal-y) ** 2)))
        angular_displacement = math.atan2((y_goal-y), (x_goal-x))-yaw
        velocity_message.linear.x=1.1*linear_displacement
        velocity_message.angular.z=4*angular_displacement
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        print("moving to goal")
        print(x,y)
        print(linear_displacement)
        print(angular_displacement)
        if (linear_displacement<distance_tolerance):
            print("reached but")
            break
    
    velocity_message.linear.x = 0
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


def setDesiredOrientation(desired_angle_radians):
    relative_angle_radians = desired_angle_radians - yaw
    if relative_angle_radians < 0:
        clockwise = 1
    else:
        clockwise = 0
    print relative_angle_radians
    print desired_angle_radians
    rotate(70 , math.degrees(abs(relative_angle_radians)), clockwise )

def gridClean():
    go_to_goal(1.0 , 1.0)
    
    print ("NIBBA DED LOL")
    '''go_to_goal(5.45, 5.45)
    go_to_goal(4.5 , 6.5)
    go_to_goal(5.45 , 5.45)
    go_to_goal(3.5 , 4.5)
    
    
    rotate(20 , 90 , False)
    move(2.0, 9.0, True)
    rotate(20 , 90 , False)
    move(2.0, 1.0, True)
    rotate(20 , 90 , False)
    move(2.0, 9.0, True)
    rotate(30 , 90 , True)
    move(2.0, 1.0, True)
    rotate(30 , 90 , True)
    move(2.0, 9.0, True)
    pass
    '''
def spiralClean():
    global x , y
    x0 = x
    y0 = y
    velocity_message = Twist()
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic , Twist , queue_size= 10)

    rk = 0.1
    
    ##while((math.sqrt(((x-x0)**2) + ((y-y0)**2))) < 5):
    while ((x < 10) and (y < 10)):
        velocity_message.linear.x = rk + 0.1
        velocity_message.linear.y = 0
        velocity_message.linear.z = 0
        velocity_message.angular.x = 0
        velocity_message.angular.y = 0
        velocity_message.angular.z = 2.0
        rk+=0.1
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

    velocity_message.linear.x = 0
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)
if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 
        time.sleep(2)
        #rotate(60, 60 , 1)
        #move(5 , 4 , 1)
        go_to_goal(1.0, 1.5)
        #go_to_goal(5.4 , 5.4)
        #setDesiredOrientation(math.radians(90))
        # spiralClean()
        #gridClean()
        #position()
        print ("NIBBA DED LOL")
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
