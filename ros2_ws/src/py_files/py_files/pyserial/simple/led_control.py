import rclpy
import serial
from rclpy.node import Node
from std_msgs.msg import String

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600, timeout=1)

class LEDControl(Node):
    def __init__(self):
        super().__init__("PySerial_LED_switch")
        self.pub = self.create_publisher(String, "path", 10)
        self.get_logger().info("Startng the node...")
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = String()
        state = input("What color do you want the LED to be?: ")
        ser.write(state.encode())
        line = ser.readline().decode(errors="ignore")
        msg.data = line
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LEDControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()