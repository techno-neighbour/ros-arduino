import serial
import rclpy
from rclpy.node import Node

class ButtonState(Node):
    def __init__(self):
        super().__init__("button_state")
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.timer = self.create_timer(0.005, self.timerCallback)
        self.get_logger().info("Informing the state...")
        print()
        
    def timerCallback(self):
        line = self.ser.readline().decode(errors="ignore")
        self.get_logger().info(f"Button state is: {line}")

def main(args=None):
    rclpy.init(args=args)
    node = ButtonState()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()