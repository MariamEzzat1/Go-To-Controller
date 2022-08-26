#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
'''------------------------------inputs----------------------------------------------'''
rospy.set_param("/goal_x",5)
x=rospy.get_param("/goal_x")
rospy.set_param("/goal_y",2)
y=rospy.get_param("/goal_y")
rospy.set_param("/beta",1.5)
beta =rospy.get_param("/beta")
rospy.set_param("/phai",6)
phai=rospy.get_param("/phai")
'''----------------------------------subscriber--------------------------------------'''
'''once the subscriber get a new data save it in current position'''
current_pose=Pose()
def callback_pose(data):
    current_pose.x=data.x
    current_pose.y=data.y
    current_pose.theta=data.theta


'''subscriber node to get the current pose of the turtle from the /turtle1/pose topic'''
def listener():
    rospy.init_node("position_listener",anonymous=True)
    pose_listener=rospy.Subscriber("/turtle1/pose",Pose,callback_pose)
    rate= rospy.Rate(1)
'''----------------------------------publisher------------------------------------------'''
'''publisher node which publishes the linear and angle velociety to turtle1/cmd_vel topic'''
def publishing():
    vel_publisher=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate1= rospy.Rate(1)
    '''h publish lw l goal bta3y ab3d mn mkan mo3yn so ana mhtaga min dis lets se it 0.5'''
  
    while (sqrt(pow((current_pose.x-x),2)+pow((current_pose.y-y),2))>0.5):
        msg=Twist()
        msg.linear.x=linear_velociety()
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=angular_velociety()
        vel_publisher.publish(msg)
        #rate1.sleep()



'''function to calculate the distance between the current and goal position and use it in linear velocity''' 
def linear_velociety (beta=1.5):
    euclidean_distance=sqrt(pow((current_pose.x-x),2)+pow((current_pose.y-y),2))
    return beta*euclidean_distance

    

'''----------------------fuction to calc the steering angle then the angular velocity---------------------'''
def angular_velociety (phai=6):
    steering_angle=atan2(y-current_pose.y,x-current_pose.x)
    return phai*(steering_angle-current_pose.theta)


'''--------------------------------------main function inshallah----------------------------------------- '''
if __name__=="__main__":
    try:
        listener()
        publishing()
    except rospy.ROSInterruptException:
        pass