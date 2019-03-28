/*#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <sstream>
using namespace std;
ros::Publisher velocity_publisher;
ros::Subscriber pose_subscriber;
turtlesim::Pose turtlesim_pose;

const double x_min = 0.0;
const double y_min = 0.0;
const double x_max = 11.0;
const double y_max = 11.0;
const double PI = 3.141592;

void move (double speed, double distance, bool isForward);
void rotate (double angular_speed, double angle, bool clockwise);
double degrees2radians (double angle_in_degrees);
double setDesiredOrientation (double desired_angle_radians);
void poseCallback (const turtlesim::Pose::ConstPtr & pose_message);
void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance);
double getDistance(double x1, double y1, double x2, double y2);

int main(int argc, char **argv)
{
	ros::init(argc, argv, "robot_cleaner");
	ros::NodeHandle n;
	double speed;
    double distance;
    bool isForward;
    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",10);
    pose_subscriber = n.subscribe("/turtle1/pose",10,poseCallback);
    

    /*setDesiredOrientation(degrees2radians(120));
    ros::Rate loop_rate (0.5);
    loop_rate.sleep();
    setDesiredOrientation(degrees2radians(-60));
    loop_rate.sleep();
    setDesiredOrientation(degrees2radians(0));

    cout<<"enter speed: ";
	cin>>speed;
	cout<<"enter distance: ";
	cin>>distance;
	cout<<"forward?: ";
	cin>>isForward;
	move(speed, distance, isForward);
    double angular_speed; double angle; bool clockwise;
    cout<<"enter angular velocity (degree/sec): ";
	cin>>angular_speed;
	cout<<"enter desired angle (degrees): ";
	cin>>angle;
	cout<<"clockwise ?: ";
	cin>>clockwise;
	rotate(degrees2radians(angular_speed), degrees2radians(angle), clockwise);
    
    ros::Rate loop_rate (0.5);

    turtlesim::Pose goal_pose;
    goal_pose.x = 1;
    goal_pose.y = 1;
    goal_pose.theta = 0;
    moveGoal(goal_pose,0.01);
    loop_rate.sleep();
    ros::spin();
}
void move (double speed, double distance, bool isForward)
{
	geometry_msgs::Twist vel_msg;	
    if(isForward)
    {
        vel_msg.linear.x = abs(speed);
    }
    else
    {
        vel_msg.linear.x = -abs(speed);
    }
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;
    vel_msg.angular.z = 0;
    double t0 = ros::Time::now().toSec();
    double current_distance = 0;
    ros::Rate loop_rate(100);
    do{
        velocity_publisher.publish(vel_msg);
        double t1 = ros::Time::now().toSec();
        current_distance = speed * (t1 - t0);
        ros::spinOnce();
        loop_rate.sleep();
    }while(current_distance < distance);
    vel_msg.linear.x = 0;
    velocity_publisher.publish(vel_msg);
}
void rotate (double angular_speed, double relative_angle, bool clockwise)
{
    geometry_msgs::Twist vel_msg;
    vel_msg.linear.x = 0;
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;

    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;
    if (clockwise)
    {
        vel_msg.angular.z = -abs(angular_speed);
    }    
    else
    {
        vel_msg.angular.z = abs(angular_speed);
    }
        
    double current_angle = 0.0;
    double t0 = ros::Time::now().toSec();
    ros::Rate loop_rate(10);
    do{
        velocity_publisher.publish(vel_msg);
        double t1 = ros::Time::now().toSec();

        current_angle = angular_speed *(t1-t0);
        ros::spinOnce();
        loop_rate.sleep();

    }while (current_angle < relative_angle);
    
    vel_msg.angular.z =0;
    velocity_publisher.publish(vel_msg);
}
double degrees2radians (double angle_in_degrees)
{   
    return angle_in_degrees * PI /180.0;
}
double setDesiredOrientation (double desired_angle_radians)
{
    double relative_angle_radians = desired_angle_radians - turtlesim_pose.theta;
    bool clockwise = ((relative_angle_radians<0)?true:false);
    //cout<<desired_angle_radians <<" , "<<turtlesim_pose.theta<<" , "<<relative_angle_radians
    rotate(abs(relative_angle_radians), abs(relative_angle_radians), clockwise);
}
void poseCallback (const turtlesim::Pose::ConstPtr & pose_message)
{
    turtlesim_pose.x = pose_message->x;
    turtlesim_pose.x = pose_message->y;
    turtlesim_pose.theta = pose_message->theta;
}
void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance)
{
    geometry_msgs::Twist vel_msg;
    
    ros::Rate loop_rate(100);
	double E = 0.0;
	do{
        //  proportional controller
		//linear
		double Kp=1.0;
		double Ki=0.02;
		double e = getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y);
		double E = E+e;
		vel_msg.linear.x = (Kp*e);
		vel_msg.linear.y =0;
		vel_msg.linear.z =0;
		//angular
		vel_msg.angular.x = 0;
		vel_msg.angular.y = 0;
		vel_msg.angular.z = 4 * (atan2(goal_pose.y-turtlesim_pose.y, goal_pose.x-turtlesim_pose.x)-turtlesim_pose.theta);

		velocity_publisher.publish(vel_msg);

		ros::spinOnce();
		loop_rate.sleep();

	}while(getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y)>distance_tolerance);
	cout<<"end move goal"<<endl;
    vel_msg.linear.x = 0;
    vel_msg.angular.z = 0;
    velocity_publisher.publish(vel_msg);
}
double getDistance(double x1, double y1, double x2, double y2){
	return sqrt(pow((x1-x2),2)+pow((y1-y2),2));
}
*/