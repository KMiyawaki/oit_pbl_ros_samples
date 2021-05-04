#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import actionlib
import rospy
from geometry_msgs.msg import Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from utils import navigation, wait_string_message


def main():
    rospy.init_node('simple_navigation_goals')
    # Action Client
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    while not ac.wait_for_server(rospy.Duration(5)):
        rospy.loginfo("Waiting for the move_base action server to come up")

    rospy.loginfo("The server comes up")
    navigation(ac, 3, 3.6, math.radians(90))


if __name__ == '__main__':
    main()
