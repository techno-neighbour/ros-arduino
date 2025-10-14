import rclpy
import random
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class IntAddClient(Node):
    def __init__(self):
        super().__init__("int_add_client")
        self.client = self.create_client(AddTwoInts, "add_two_ints")
        self.timer = self.create_timer(1.5,self.timerCallback);

    def send_request(self, a, b):
        while not self.client.wait_for_service(1):  # wait for the service to be available
            self.get_logger().warn("Service not available, waiting ...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        self.get_logger().info(f"Requesting {request.a} + {request.b}")

        future = self.client.call_async(request)
        future.add_done_callback(self.callback)
    
    def callback(self, future):
        response = future.result()
        self.get_logger().info(f"Server says: {response.sum}")
        print()

    def timerCallback(self):
        a, b = random.randint(0, 100), random.randint(0, 100)
        self.send_request(a, b)
        
def main(args=None):
    rclpy.init(args=args)
    node = IntAddClient()
    rclpy.spin(node) # this is what you should use, but will only send one request
    rclpy.shutdown()

if __name__ == "__main__":
    main()