import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class sensorLogger(Node):
    def __init__(self):
        super().__init__('sensor_logger')
        self.temp_sub = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10
        )
        self.hum_sub = self.create_subscription(
            Float32,
            'humidity',
            self.listener_callback,
            10
        )
    
    def temp_callback(self, temp_msg):
        self.get_logger().info(f'received temperatre data: {temp_msg.data:.2f}')
        
    def hum_callback(self, hum_msg):
        self.get_logger().info(f'received humidity data: {hum_msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = sensorLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()