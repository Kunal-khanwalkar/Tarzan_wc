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
sudo apt-get install build-essential
sudo apt-get install git
sudo apt-get install pip 
pip install --user wheel numpy scipy matplotlib scikit-image scikit-learn ipython dlib

echo "*********ROS installation*********"
sudo apt-get install ros-"$dist"-desktop-full -y

echo "*some dependencies*"
sudo apt-get install v4l2ucp v4l-utils libv4l-dev

echo "*********OpenCV installation*********"
./opencv"$vr".sh

