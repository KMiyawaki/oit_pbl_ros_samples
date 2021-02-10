#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import actionlib
import rospy
from geometry_msgs.msg import Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler


def main():
    rospy.init_node('simple_navigation_goals')
    # Action Client
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    while not ac.wait_for_server(rospy.Duration(5)):
        rospy.loginfo("Waiting for the move_base action server to come up")

    rospy.loginfo("The server comes up")

    # make navigation goal
    coord_type = "map"
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = coord_type
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = 3.0
    goal.target_pose.pose.position.y = 3.6
    goal.target_pose.pose.orientation.w = 1.0
    q = quaternion_from_euler(0, 0, math.radians(90))
    goal.target_pose.pose.orientation = Quaternion(q[0], q[1], q[2], q[3])

    rospy.loginfo("Sending goal")
    ac.send_goal(goal)
    finished = ac.wait_for_result(rospy.Duration(30))
    state = ac.get_state()
    if finished:
        rospy.loginfo("Finished: (%d)", state)
    else:
        rospy.loginfo("Time out: (%d)", state)


if __name__ == '__main__':
    main()
