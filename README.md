# RosProject-2022-AO-and-LK
Rosproject of year 2022 by Arman Orynbekov and Leya Kurmangaleyeva. Real time semantic segmentation for duckietown.

This the the code developed for Jacobs University ROS Project course.

To launch the code:
1. Prepare your duckiebot and computer
2. Find your dusckiebot with the command "dts fleet discover"
3. Start GUI tools with "dts start_gui_tools robotname"
4. Run "rosrun image_transport republish compressed in:=/robotname/camera_node/image raw out:=/robotname/camera_node/image/raw" to create a publisher node for decompression of images
5. Run the python file
6. It will start to create images in the folder the python file locates in
7. Stop when you get enough images
8. Run a program to convert these images into video
