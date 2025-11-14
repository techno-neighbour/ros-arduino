import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from in_files.msg import MotorSensor

class Sensor(Node):
    def __init__(self):
        super().__init__("sen_sub")
        self.pub = self.create_publisher(String, "sen_say", 10)
        self.sub = self.create_subscription(MotorSensor, "car", self.subCall, 10)
        self.get_logger().info("Updating...")
        print()
        
    def subCall(self, msg):
        sen_msg = String()
        sen_msg.data = ""

        if msg.distance < 10 and not getattr(self, 'is_backing_up', False):
            self.get_logger().warn("WARNING: Too close!")
            sen_msg.data = "go back"
            self.is_backing_up = True

        elif msg.distance >= 10 and getattr(self, 'is_backing_up', False):
            sen_msg.data = "stop"
            self.is_backing_up = False

        if sen_msg.data:
            self.pub.publish(sen_msg)

        self.get_logger().info(f"Sensor is {msg.distance: .4f} cm")
        print()

def main(args=None):
    rclpy.init(args=args)
    node = Sensor()
    try:
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        print(" Execution stopped: User interrupted.")

if __name__ == "__main__":
    main()