import rclpy
from rclpy.node import Node
from in_files.msg import MotorSensor

class Volt(Node):
    def __init__(self):
        super().__init__("volt_sub")
        self.sub = self.create_subscription(MotorSensor, "car", self.listener_callback, 10)

    def listener_callback(self, msg):
        if msg.voltage:
            volt:float = float(msg.voltage.rstrip('V'))
            if volt < 3.0:
                self.get_logger().warn(f"WARNING: Low Voltage")
        self.get_logger().info(f"Voltage: {msg.voltage}")
        print()

def main(args=None):
    rclpy.init(args=args)
    volt = Volt()
    try:
        rclpy.spin(volt)
        volt.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        print(" Execution stopped: User interrupted.")  

if __name__ == "__main__":
    main()