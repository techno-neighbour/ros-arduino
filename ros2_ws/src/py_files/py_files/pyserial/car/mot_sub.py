import rclpy
from rclpy.node import Node
from in_files.msg import MotorSensor

class Motor(Node):
    def __init__(self):
        super().__init__("mot_sub")
        self.sub = self.create_subscription(MotorSensor, "car", self.caller, 10)
        self.last_dir = ""
        self.get_logger().info("Updating...")
        print()
        
    def caller(self, msg):
        if msg.direction and msg.direction != self.last_dir:
            self.last_dir = msg.direction
            self.get_logger().info(f"Currently motor moving: {msg.direction}")
            print()

def main(args=None):
    rclpy.init(args=args)
    node = Motor()
    try:
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        print(" Execution stopped: User interrupted.")

if __name__ == "__main__":
    main()