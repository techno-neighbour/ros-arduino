import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Distance(Node):
    def __init__(self):
        super().__init__("dist_sub")
        self.sub = self.create_subscription(String, "motor", self.subscriberCallback, 10)
        self.get_logger().info("Listening...")
        print()
        
    def subscriberCallback(self, msg):
        self.get_logger().info(f"Motor moves: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = Distance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()