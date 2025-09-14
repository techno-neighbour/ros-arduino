import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Distance(Node):
    def __init__(self):
        super().__init__("dist_pub")
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.pub = self.create_publisher(Float32, "distance", 10)
        self.timer = self.create_timer(0.05, self.timerCallback)
        self.get_logger().info("Distance measuring has begun...")
        print()
        
    def timerCallback(self):
        line = self.ser.readline().decode(errors="ignore").strip()
        value = float(line) if line else 0.0
        msg = Float32()
        msg.data = value
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Distance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()