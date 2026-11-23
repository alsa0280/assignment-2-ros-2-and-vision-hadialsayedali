import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2

# Define this class as inheriting from class Node
class ImagePublisher(Node):

    def __init__(self):
        # Name this node 'image_publisher'
        super().__init__('image_publisher')
        # Publish Image messages on the 'video_frames' topic (queue size 10)
        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
        # Call timer_callback every 0.1 seconds (~10 frames per second)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # Open the default webcam (device 0)
        self.cap = cv2.VideoCapture(0)
        # Converter between OpenCV images and ROS Image messages
        self.br = CvBridge()

    def timer_callback(self):
        # Grab one frame from the webcam; ret is True if it worked
        ret, frame = self.cap.read()
        if ret == True:
            # Convert the OpenCV frame to a ROS Image message and publish it
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame))


def main(args=None):
    # Start the ROS2 communication process for this module
    rclpy.init(args=args)

    # Create an ImagePublisher node
    image_publisher = ImagePublisher()

    # Run the ImagePublisher node
    rclpy.spin(image_publisher)

    # Free up the node's resources when it stops running
    image_publisher.destroy_node()

    # Shut down the ROS2 communication process for this module
    rclpy.shutdown()

# If the module is run itself, call its main() function
if __name__ == '__main__':
    main()
