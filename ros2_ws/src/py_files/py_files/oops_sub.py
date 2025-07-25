#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SubscribingClass(Node):
    def __init__(self):
        super().__init__("py_hears")
        self. sub = self.create_subscription(Float32, "fake_distance", self.subscriberCallback, 10)
        self.get_logger().info("Listening...")
        print()
        
    def subscriberCallback(self, msg):
        self.get_logger().info(f"Data reads: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = SubscribingClass()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()