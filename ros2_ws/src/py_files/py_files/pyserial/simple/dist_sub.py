import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Distance(Node):
    def __init__(self):
        super().__init__("dist_sub")
        self.sub = self.create_subscription(Float32, "distance", self.subscriberCallback, 10)
        self.get_logger().info("Listening...")
        print()
        
    def subscriberCallback(self, msg):
        if msg.data and msg.data < 10 :
            self.get_logger().warn("WARNING: Too close!")
        self.get_logger().info(f"Distance is {msg.data: .4f} cm")
        print()

def main(args=None):
    rclpy.init(args=args)
    node = Distance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()