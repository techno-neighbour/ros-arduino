import rclpy
import serial
from rclpy.node import Node
from std_msgs.msg import String

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600, timeout=1)

class Motor(Node):
    def __init__(self):
        super().__init__("motor_pub")
        self.pub = self.create_publisher(String, "motor", 10)
        self.get_logger().info("Startng the node...")
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = String()
        state = input("What direction do you want the wheels to move?: ")
        ser.write(state.encode())
        line = ser.readline().decode(errors="ignore")
        msg.data = line
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Motor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()