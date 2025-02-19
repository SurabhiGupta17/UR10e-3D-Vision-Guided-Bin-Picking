# UR10e-3D-Vision-Guided-Bin-Picking

## Overview
This project focuses on developing an autonomous bin-picking system using the UR10e robotic arm, integrated with a 3D vision system for precise object detection and manipulation. The goal is to enable the robotic arm to identify, pick, and place objects from a bin using real-time vision feedback and motion planning.

## Hardware & Simulation Setup
The robotic system is built using the UR10e manipulator, equipped with a Model T42 gripper for object handling. The simulation environment is set up in Gazebo. The Intel RealSense D435 camera will be used to provide depth perception and enable object recognition.

https://private-user-images.githubusercontent.com/103124390/414504098-493e9f8f-b443-472b-b18a-b137cda246a7.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk5Mjc1ODMsIm5iZiI6MTczOTkyNzI4MywicGF0aCI6Ii8xMDMxMjQzOTAvNDE0NTA0MDk4LTQ5M2U5ZjhmLWI0NDMtNDcyYi1iMThhLWIxMzdjZGEyNDZhNy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxOVQwMTA4MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zMWY2YmUyNzM2NTZmOWJhOWU5MmQyYTk4OWI1ODNiNGZjODNmMTg3YjkwN2U3NDlhZTAwNDg4MjFhNjk2MTVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.UUnvYhjOeInpDq91fShTGxWce8opdBYJtq27O2_XJeQ

## Software Stack
The project is implemented using ROS2 Jazzy, with Gazebo Harmonic for simulation. The control framework will include MoveIt for motion planning and real-time execution. The perception pipeline will utilize OpenCV and PCL for point cloud processing and object localization.

## Current Progress
The UR10e robotic arm model, along with the Model T42 gripper, has been integrated into the simulation. Controllers have been configured for smooth joint actuation, and the environment has been set up with relevant objects for testing. The next step is integrating the vision system by adding the Intel RealSense D435 camera to the robot, which will enable object detection and pose estimation.

### Simulation Setup Video  
https://private-user-images.githubusercontent.com/103124390/414502265-7a57e7e8-6601-46dd-add0-7d9dbdf206e7.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk5MjcwODUsIm5iZiI6MTczOTkyNjc4NSwicGF0aCI6Ii8xMDMxMjQzOTAvNDE0NTAyMjY1LTdhNTdlN2U4LTY2MDEtNDZkZC1hZGQwLTdkOWRiZGYyMDZlNy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxOVQwMDU5NDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NTk3M2VkYjhiY2RjMjQyYWMzYjU3YmUyMjcxZDAzNmQ0MjUxZTk0YmRlNTU3MmFlN2ZjYTg1ZDc0OGE2OTI0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.HED4P3_vmrQAqwKffR6wLl4wc9r60WFVo3JVK4i8QwA

## Next Steps
- Implement vision-based object detection and pose estimation.
- Develop a grasp planning strategy for efficient picking.
- Integrate MoveIt for autonomous trajectory planning.
- Test and optimize the complete bin-picking pipeline in simulation.

## How to Run
1. Set up the ROS 2 workspace and source it.
2. Launch the Gazebo simulation with the configured UR10e and gripper:

   ```sh
   ros2 launch gazebo bin_picking.launch.py
