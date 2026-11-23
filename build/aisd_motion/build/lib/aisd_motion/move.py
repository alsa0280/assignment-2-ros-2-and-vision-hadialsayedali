import rclpy
from rclpy.node import Node
from aisd_msgs.msg import Hand
from geometry_msgs.msg import Twist

# This class inherits from class Node
class Move(Node):

    def __init__(self):
	# Initialize the node with name "move"
        super().__init__('move')
	# Establish node as subscribing to cmd_hand topic
	# with message type Hand
	# and execute listener_callback() each time a message is received
	# queue up to 10 messages
        self.subscription = self.create_subscription(
            Hand,
            'cmd_hand',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
	# Move node is also a publisher to cmd_vel topic with Twist msg type
        self.vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
	
    # Callback function every time a Hand message is received
    def listener_callback(self, msg):
        angle = 0.0
        linear = 0.0
	# if index finger is on RHS of screen, set up turn to right
        if msg.xindex > 0.55:
            self.get_logger().info('right')
            angle = -0.1
	# if index finger on LHS of screen, set up turn to left
        elif msg.xindex < 0.45:
            self.get_logger().info('left')
            angle = 0.1
	# otherwise (if in middle of screen), don't turn
        else:
            angle = 0.0
	# if index finger closer to right than pinky (right backhand), set forward velocity to 0.5m/s 
        if msg.xindex > msg.xpinky:
            self.get_logger().info('come')
            linear = 0.5
        else:
	# otherwise (right palm facing screen), set forward velocity to 0
            self.get_logger().info('stay')
            linear = 0.0
	# create a Twist message with movement specifications
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angle
	# if there's at least one subscriber to cmd_vel, publish the Twist message
        if self.vel_publisher.get_subscription_count() > 0:
            self.vel_publisher.publish(twist)
	# otherwise, keep waiting for one subscriber
        else:
            self.get_logger().info('waiting for subcriber')

# the main function called by the executable
def main(args=None):
    # initiate the ROS2 communication 
    rclpy.init(args=args)
   
    # construct a Move node
    move = Move()

    # keep the node running and calling listener_callback when a message is received (until the node quits)
    rclpy.spin(move)

    # once the node stops spinning, free its resources
    move.destroy_node()

    # shut down the ROS2 communication for this process
    rclpy.shutdown()

# if the module is called directly, call its main() function
if __name__ == '__main__':
    main()
