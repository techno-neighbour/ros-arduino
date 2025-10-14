import rclpy
from rclpy.node import Node
from in_files.msg import MotorSensor

class Motor(Node):
    def __init__(self):
        super().__init__("mot_sub")
        self.sub = self.create_subscription(MotorSensor, "mot_sen", self.caller, 10)
        self.get_logger().info("Updating...")
        print()
        
    def caller(self, msg):
        if msg.direction:
            self.get_logger().info(f"Motor moves: {msg.direction}")

def main(args=None):
    rclpy.init(args=args)
    node = Motor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()