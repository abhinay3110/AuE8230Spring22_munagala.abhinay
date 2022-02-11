#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #
    print('make the turtlesim make a square_openloop')
    #setting up while loop to run the below command 4 times
    x = 1
    while(x<5):

        #linear velocity in x
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        vel_msg.linear.x = 0.2
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        
        t0 = rospy.Time.now().to_sec()
        distance = 0

        #to move the turtle in an specified distance
        while(distance < 2):
            #Publish velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            distance= 0.2*(t1-t0)
        #After the loop stop the bot
        #Give angular velocity
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0.2
        ta =  rospy.Time.now().to_sec()

        angle = 0
        while(angle<1.57):
            #Publishing the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            tb=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            angle= 0.2*(tb-ta)
        vel_msg.angular.z = 0
        x = x+1

        #Making the robot stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing the function
        move()
    except rospy.ROSInterruptException: pass
