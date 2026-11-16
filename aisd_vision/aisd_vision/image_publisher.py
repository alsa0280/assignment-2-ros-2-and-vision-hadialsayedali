import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2


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
    rclpy.init(args=args)

    image_publisher = ImagePublisher()

    rclpy.spin(image_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
