#!/usr/bin/env python3
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

x_cor=[5,8,8,5,5]
y_cor=[5,5,8,8,5]

print('make the bot go on the coordinates')

class cor_task():

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x,4)
        self.pose.y = round(self.pose.y,4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self):
        goal_pose = Pose()
        goal_pose.x = a_cor
        goal_pose.y = b_cor
        distance_tolerance = 0.001
        vel_msg = Twist()
        angle=self.pose.theta
        correct_angle=abs(angle-(atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)))
        while((abs(atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta))>0.0001):

            #angular velocity in the z:
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
            correct_angle=abs(self.pose.theta-(atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)))

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        vel_msg.angular.z =0


        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))>= distance_tolerance:
            
            #linear velocity in x:
            vel_msg.linear.x = 1 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            self.velocity_publisher.publish(vel_msg)

            distance_new= sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))

            vel_msg.linear.x=0

        #Stop robot after the movement is complete
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)


if __name__ == '__main__':

    for itr in range(5):

        try:
            #Testing our function
            x = cor_task()
            a_cor=x_cor[itr]
            b_cor=y_cor[itr]
            x.move2goal()

        except rospy.ROSInterruptException: pass

print('Completed making the turtlesim move in a square closed loop')
