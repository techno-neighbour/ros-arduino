import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from in_files.msg import MotorSensor

class Sensor(Node):
    def __init__(self):
        super().__init__("sen_sub")
        self.pub = self.create_publisher(String, "sen_say", 10)
        self.sub = self.create_subscription(MotorSensor, "mot_sen", self.subCall, 10)
        self.get_logger().info("Updating...")
        print()
        
    def subCall(self, msg):
        if msg.distance and msg.distance < 10 :
            self.get_logger().warn("WARNING: Too close!")
            sen_msg = String()
            sen_msg.data = "go back"
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