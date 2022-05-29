#!/usr/bin/env python

#Import some important opencv libraries
import rospy
import cv2
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

#Import messages types
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
 
print("HI") # Intial check

bridge = CvBridge()
 
# Initialize the ROS Node named 'opencv_example', allow multiple nodes to be run with this name
rospy.init_node('opencv_example', anonymous=True)

# Print "Hello ROS!" to the Terminal and ROSLOG
rospy.loginfo("Hello ROS!") # Check

img_list = [] # Intialize an array where images are going to be stored into

# Function to create an image window
def show_image(img):
     cv2.imshow("Image Window", img)
     cv2.waitKey(3)

# Callback function converts images from img_smg format to cv2 format for later use in Python
def image_callback(img_msg):

    global img_list
    # log some info about the image topic
    rospy.loginfo(img_msg.header)
    
    try:
         cv_image = bridge.imgmsg_to_cv2(img_msg, "rgba8")
    except CvBridgeError as e:
         rospy.logerr("CvBridge Error: {0}".format(e))
    
    img_list.append(cv_image) # Add converted image to the array
    
    	
    	
# Callback function performs K-means clustering on the images from the beforementioned array
def timer_callback(event):
    global img_list
    for count in range(len(img_list)):
		
        cv2.imwrite(str(count) + 'ci1.jpeg', img_list[count])
            
        path = str(count) + 'ci1.jpeg'
        img = cv2.imread(path)
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        twoDimage = img.reshape((-1, 3))
        twoDimage = np.float32(twoDimage)
    
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 12, 1.0)
        K = 9
        attempts=10
    
        ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        result_image = res.reshape((img.shape))
        
        cv2.imwrite(str(count) + 'ci1.jpeg', result_image)
    
        plt.imshow(result_image)
        #plt.show()

# Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("robotLA/camera_node/image/raw", Image, image_callback)
rospy.Timer(rospy.Duration(2), timer_callback)

# Initialize an OpenCV Window named "Image Window"
cv2.namedWindow("Image Window", 1)


# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
     rospy.spin()
