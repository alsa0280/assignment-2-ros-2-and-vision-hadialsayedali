import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands

from aisd_msgs.msg import Hand

# This class inherits from class Node
class Hands(Node):

    def __init__(self):
	# Give this node the name "hands"
        super().__init__('hands')

        # A converter between ROS and OpenCV images
        self.br = CvBridge()
	# This node is a publisher to the cmd_hand topic
	# It sends messages of type Hand
        self.hand_publisher = self.create_publisher(Hand, 'cmd_hand', 10)

	# This node subscribers to the video_frames topic
	# It receives messages of type Image
	# Each time it receives an image, it calls listener_callback()
        self.subscription = self.create_subscription(
            Image,
            'video_frames',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
	# convert the ROS2 Image type to OpenCV image
        image = self.br.imgmsg_to_cv2(msg)
	
	# MediaPipe landmark for pinky finger tip
        PINKY_FINGER_TIP = 20
	# MediaPipe landmark for index finger tip
        INDEX_FINGER_TIP = 8
        # Create an instance of a MediaPipe Hands model (detects hand landmarks from OpenCV image)
        with mp_hands.Hands(
		# use a lightweight and faster model
                model_complexity=0,
		# count something still as a hand if at least 50% confident
                min_detection_confidence=0.5,
		# count something movement-tracked as a hand if at least 50% confident
                min_tracking_confidence=0.5) as myhands:

            # Mark the image as non-writeable (read-only)
            image.flags.writeable = False
	    # OpenCV stores images as BGR, but MediaPipe expects RGB 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	    # Process the image and get coordinates for hand landmarks
            results = myhands.process(image)
	    # If a hand landmark was found
            if results.multi_hand_landmarks:
                # Create a Hand object and fill it with the results' landmark coordinates
                msg = Hand()
                msg.xpinky = results.multi_hand_landmarks[0].landmark[PINKY_FINGER_TIP].x
                msg.xindex = results.multi_hand_landmarks[0].landmark[INDEX_FINGER_TIP].x
	        # If there's at least one subscriber to this node's topic                
		if self.hand_publisher.get_subscription_count() > 0:
		    # Then publish the Hand message
                    self.hand_publisher.publish(msg)
                else:
		    # Otherwise, don't publish
                    self.get_logger().info('waiting for subcriber')


def main(args=None):
    # Start up the ROS2 communication process for this module
    rclpy.init(args=args)

    # Create a Hands node
    hands = Hands()

    # Run the node, calling listener_callback when a message arrives
    rclpy.spin(hands)

    # Free up the node's resources when made inactive
    hands.destroy_node()
    # Shut down the ROS2 process for this module
    rclpy.shutdown()

# If this module is run directly, call its main() function
if __name__ == '__main__':
    main()
