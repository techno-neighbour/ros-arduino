#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32

class PublishingClass(Node):
    def __init__(self):
        super().__init__("py_says")
        self.counter = 1
        self.pub = self.create_publisher(Float32, "fake_distance", 10)
        self.get_logger().info("Starting...")
        self.timer = self.create_timer(1, self.timerCaller)

    def timerCaller(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 10.0)
        self.pub.publish(msg)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublishingClass()
    rclpy.spin(node)
    node.destroy_node
    rclpy.shutdown()

if __name__ == "__main__":
    main()