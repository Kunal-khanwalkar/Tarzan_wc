#!/bin/bash

echo "******INSTALLATION START******"
vr=`lsb_release -r`
vr=${vr:9}
if [ "$vr" = "16.04" ];	
then
	dist="kinetic"
elif [ "$vr" = "18.04" ];
then
	dist="melodic"
else
	echo "ERROR: Not a compatible version of Ubuntu"
	exit
fi 

echo "*****Update Ubuntu*****"
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install build-essential -y
sudo apt-get install git -y
sudo apt-get install pip -y
pip install --user wheel numpy scipy matplotlib scikit-image scikit-learn ipython dlib -y

echo "*********ROS installation*********"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get install ros-"$dist"-desktop-full -y

echo "*some dependencies*"
sudo apt-get install v4l2ucp v4l-utils libv4l-dev -y

echo "*********OpenCV installation*********"
sudo ./opencv"$vr".sh

