import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aisd/ros2_ws/src/assignment-2-ros-2-and-vision-hadialsayedali/install/aisd_motion'
