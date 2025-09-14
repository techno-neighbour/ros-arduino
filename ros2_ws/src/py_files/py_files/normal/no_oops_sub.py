#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_hears")
    sub = node.create_subscription(Float32, "fake_distance", lambda msg: node.get_logger().info(f"Data reads: {msg.data}"), 10)
    node.get_logger().info("Listening...")
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()