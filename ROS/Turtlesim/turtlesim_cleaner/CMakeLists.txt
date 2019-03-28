cmake_minimum_required(VERSION 2.8.3)
project(turtlesim_cleaner)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  message_generation
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES turtlesim_cleaner
   CATKIN_DEPENDS roscpp rospy std_msgs geometry_msgs message_runtime
#  DEPENDS system_lib
)
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(robot_cleaner_node src/robot_cleaner.cpp)
target_link_libraries (robot_cleaner_node ${catkin_LIBRARIES})
add_dependencies(robot_cleaner_node beginner_tutorials_gencpp)

