import rclpy
import random
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node("int_add_client_no_oops")
    client = node.create_client(AddTwoInts, "add_two_ints")
    
    while not client.wait_for_service(1.5): # wait for the service to be available
        node.get_logger().warn("Service not available, waiting ...")

    request = AddTwoInts.Request()
    request.a = random.randint(0, 100)
    request.b = random.randint(0, 100)
    node.get_logger().info(f"Requesting {request.a} + {request.b}")

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future, timeout_sec = 1) # asks the server until the timeout is reached
    response = future.result()

    if response is not None:
        node.get_logger().info(f"Server says: {response.sum}") # if a response is received within the timeout
    else:
        print()
        node.get_logger().error("Service call failed") # if no response is received within the timeout
        
    rclpy.shutdown()

if __name__ == "__main__":
    main()