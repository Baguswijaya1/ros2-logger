import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bagus/ichimonji/ros2-logger/install/sensor_pub_py'
