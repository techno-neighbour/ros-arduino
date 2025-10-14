import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class IntAddServer(Node):
    def __init__(self):
        super().__init__("int_add_server")
        self.srv = self.create_service(AddTwoInts, "add_two_ints", self.callback)
        self.get_logger().info("IntAddServer is ready to add two integers.")

    def callback(self, request, response):
        self.get_logger().info(f"Received request: {request.a} + {request.b}")
        response.sum = request.a + request.b
        self.get_logger().info(f"Sending response: {response.sum}")
        print()
        return response

def main(args=None):
    rclpy.init(args=args)
    node = IntAddServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()