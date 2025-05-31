import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import numpy as np

class sensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.temp_pub = self.create_publisher(Float32, 'temperature', 10)
        self.hum_pub = self.create_publisher(Float32, 'humidity', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callbck(self):
        # inisialisasikan pesan
        temp_msg = Float32()
        
        #baca sensor
        temp_msg.data = self.readtemp()
        
        # kirim ke terminal
        self.get_logger().info(f'temperature : {temp_msg.data}')

        # publish
        self.temp_pub.publish(temp_msg)

    def readtemp(self):
        temperature = np.random.normal(25, 0.2)
        return float(temperature)
    
    def readhum(self):
        humidity = np.random.normal(30, 2)
        return float(humidity)
    
def main(args=None):
    rclpy.init(args=args)
    node = sensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    