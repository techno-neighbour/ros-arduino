import rclpy
import serial
import threading
from rclpy.node import Node
from in_files.msg import MotorSensor
from std_msgs.msg import String

class MS(Node):
    def __init__(self):
        super().__init__("motor_sensor_pub")
        self.pub = self.create_publisher(MotorSensor, "car", 10)
        self.sub = self.create_subscription(String, "sen_say", self.listener_callback, 10)
        self.lock = threading.Lock()
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.get_logger().info("Starting node...")
        self.timer = self.create_timer(0.05, self.timer_callback)

        # to store last values
        self.last_dire = ""
        self.last_dist = 0.0
        self.last_volt = ""

        # to get input in background thread
        threading.Thread(target=self.read_user_input, daemon=True).start()

    def read_user_input(self):
        while True:
            state = input("Enter direction (1=fwd, 2=back, 3=left, 4=right, 0=stop): ").strip()
            if state in ["0", "1", "2", "3", "4"]:
                with self.lock:
                    self.last_dire = state
                self.ser.write(state.encode())

    def timer_callback(self):
        # to read and send sensor data continuously.
        line = self.ser.readline().decode(errors="ignore").strip()
        msg = MotorSensor()

        if msg is None:
            return

        if line.endswith('V'):
            self.last_volt = line  # voltage

        elif line.replace('.', '', 1).isdigit():
            self.last_dist = float(line) # distance

        elif line:
            self.last_dire = line  # direction

        with self.lock:
            msg.direction = self.last_dire
            msg.distance = self.last_dist
            msg.voltage = self.last_volt

        self.pub.publish(msg)

    def listener_callback(self, msg):# called only when sensor says 'too close.
        if msg.data == "go back":
            self.ser.write(b'2')  

        elif msg.data == "stop":
            self.ser.write(b'0')  

        
def main(args=None):
    rclpy.init(args=args)
    node = MS()
    try:
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        print(" \nExecution stopped: User interrupted.")

if __name__ == "__main__":
    main()
