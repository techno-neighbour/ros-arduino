#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

def main(args=None):
    rclpy.init(args=args)
    my_node = Node("py_says")
    pub = my_node.create_publisher(Float32, "fake_distance", 10)
    msg = Float32()
    msg.data = 32.0966757
    pub.publish(msg)
    my_node.get_logger().info(f"Message Published.")
    rclpy.shutdown()

if __name__ == "__main__":
    main()