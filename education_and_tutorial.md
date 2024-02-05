# Education and tutorials

This page will contain a list of education courses or tutorials for aerial robotics. 
This is a partly compilation of [this ROS discourse thread](https://discourse.ros.org/t/how-did-you-get-started-in-aerial-robotics/31512) and the May meeting about [tutorials and education](https://discourse.ros.org/t/may-2023-meetings-aerial-robotics/31231/5) and some googling :)

This also includes input from [a Linkedin post](https://www.linkedin.com/feed/update/urn:li:activity:7079385991144185856/) for a call of suggestions. This has been an adaption from the following [Bitcraze Blogpost](https://www.bitcraze.io/2023/07/online-courses-in-aerial-robotics/), and [the overview presentation done for the ROS-aerial CWG meetings](https://discourse.ros.org/t/august-2023-meetings-aerial-robotics/32809/8)

## Course explanation
This section explains some of the recourses in more detail. 

### Books
There is this important resource which is the book titled ‘Small Unmanned Aircraft: Theory and Practice.’ This book has been written by Randy Beard and Tim McLain of Brigham Young University, and it covers everything from the absolute basics of coordinate frames and quadrotor dynamics to path planning and cameras. It is a must-read for anybody starting in UAVs and Aerial robotics.

The physical book can be found here: http://press.princeton.edu/titles/9632.html

The available PDFs can be accessed on GitHub: https://github.com/randybeard/uavbook

### Online Courses on Aerial Robotics

_This section shows online courses for aerial robotics with online instructor._

Coursera offers the **‘Robotics: Aerial Robotics’** course as part of the Robotics specialization. Taught by Prof. Vijay Kumar from Penn University, this 4-week course covers the mechanics and control of aerial vehicles using Matlab. It starts from 1 dimension and gradually progresses to the 3rd dimension in simulation. The course is part of a paid educational program, but you can audit the lessons for free.

Link: https://www.coursera.org/learn/robotics-flight 

Udacity has been offering a course on Aerial Vehicles for quite some time for the **Flying car nano degree**. The lessons are taught by top names in the industry and cover key aspects of Aerial Robotics, such as motion planning, controls, and estimation, with lab assignments involving a real drone. The course duration is 4 months, and access is available for a fee.

Link: https://www.udacity.com/course/flying-car-nanodegree–nd787

Additionally, there’s the course **‘Applied Control System 3: UAV Drone (3D Dynamics & Control)’** which is part of a series by Mark Misin. This course delves deep into the dynamics, control, and modeling of quadrotors.

Link: https://www.udemy.com/course/applied-control-systems-for-engineers-2-uav-drone-control/

### University courses on Aerial Robotics with open resources
_This section showes university courses that have released recordings of lectures, slides and/or assignments. For instructions participants would need to follow the actual course at that one university._

The University of Maryland offers a course on **Autonomous Aerial Robotics**, making all videos, slides, and assignments available. Taught by Nitin J. Sanket and Chahat Deep Singh, the course covers everything from basic control and dynamics to full autonomy. It’s a comprehensive resource for aerial robotics. The course utilizes the _Parrot Bebop 2.0_, and while a Mocap system is required, you may explore the possibility of adapting the course to a different platform. _ROS_ is also part of this course

Link: http://prg.cs.umd.edu/enae788m

**‘Visual Navigation For Autonomous Vehicles’** is a course available on MIT Open Courseware, taught by Prof. Luca Carlone. As the name implies, the course primarily focuses on autonomous navigation for any autonomous vehicle. It includes exercises where students implement vision algorithms on both ground robots and drones. Additionally, the course covers working with ROS and applying the knowledge to a simulated drone in Unity. The students also get to learn how to work with _ROS_

Link: https://ocw.mit.edu/courses/16-485-visual-navigation-for-autonomous-vehicles-vnav-fall-2020/

The **‘Bio-inspired Robotics’** course at the University of Washington, led by Prof. Sawyer Fuller, explores the realm of drawing inspiration from nature rather than reinventing the wheel. It covers various robots inspired by creatures capable of swimming, walking, hopping, and of course, flying. Lab assignments in this course involve working with a _Crazyflie_ drone.

Link: https://faculty.washington.edu/minster/bio_inspired_robotics/

Brown University offers a course called **‘Introduction to Robotics’** taught by Prof. Stefanie Tellix. While the introduction covers generic robotics, the focus of the full course is on building and programming the _Duckiedrone_. The course dives straight into autonomy and also teaches students how to work with _ROS_.

Link: https://cs.brown.edu/courses/cs1951r/

Princeton University  have also decided to release their **‘Intro to Robotics’** lectures and materials for the public. It covers all from control and estimation, computer vision and planning. Also it offers lab assignments with the _Crazyflie_.

Link: https://irom-lab.princeton.edu/intro-to-robotics/

### Youtube
_Youtube also has quite some tutorials available so this section highlights a few._

**Drone Programming with Python**: This popular tutorial/course teaches viewers how to program a real drone using Python with the _DJI Tello_. It offers a great opportunity for anyone looking for a short and enjoyable project to undertake, especially on a rainy day, while still working with a real platform.

Link: https://youtu.be/LmEcyQnfpDA

**Intelligent Quads YouTube Channel**: This channel is entirely dedicated to creating autonomous UAVs, covering topics from Ardupilot to MAVlink to ROS and Gazebo. It appears to be a valuable resource for beginners in the field of autonomous UAVs. This also includes _ROS_ as part of the lessons as well.

Link: https://www.youtube.com/@IntelligentQuads

### Code Examples

Here are some code examples that can be used as reference for experiments.

**Mambo ROS Examples:** This is a collection of experiments targeted Parrot Mambo drones, there are experiments with one or multiple vehicles at the same time. It runs over ROS over BLE, and some test are adapted to make use of a Vicon MoCap system. From a control theory's perspective, it showcases an optional robust control strategy, using an H-Infinity controller with perturbation estimation and a identified dynamic model of a Parrot Mambo drone. 

Link: https://github.com/TOTON95/Mambo_ROS_Examples


### Some special mentions
_So here there are some courses that either doesn't fit in the above categories or are deprecated._ 

* University of Twente UAV Centre: The University of Twente has created a portal with a variety of UAV-related courses. You can find a wealth of information and educational materials on their website. Link: https://www.itc.nl/facilities/centres-of-expertise/uav-centre/
* Self-Driving Car Specialization: If you are interested in learning more about SLAM (Simultaneous Localization and Mapping) and sensors, this specialization is tailored for self-driving cars but the theory can be useful for drones as well. Link: https://www.coursera.org/specializations/self-driving-cars
* Autonomous Navigation for Flying Robots: This older course is still highly relevant for anyone interested in autonomous navigation for flying robots. It offers valuable insights and knowledge. Link: https://www.edx.org/course/autonomous-navigation-for-flying-robots
* Drone Dojo: For those looking to build their own drones, Drone Dojo provides useful instructions and courses to get started on DIY drone projects. Link: https://dojofordrones.com/
* Bachelor Majors in UAV Engineering: If you are fully committed to pursuing a career in aerial robotics, both Embry-Riddle Aeronautical University and the University of North Dakota offer full bachelor’s majors in becoming a UAV engineer. Embry-Riddle Aeronautical University: https://erau.edu/degrees/bachelor/unmanned-aircraft-systems University of North Dakota: https://und.edu/programs/unmanned-aircraft-system-operations-bs-aero/

## Working list
_This list contains some resources that we haven't included in the overview. Remove the item once it has been included_

* [PX4 getting started page](https://px4.io/software/getting-started/)
* [Learning ArduPilot](https://ardupilot.org/dev/docs/learning-ardupilot-introduction.html)
* [Aerial robotics 101 medium article](https://medium.com/r3plica/aerial-robotics-101-introduction-f6eeb88c760f)
* [Aerial robotics with ROS](https://aerialrobotics.readthedocs.io/) (work in progress)
* [Bitcraze crazyflie tutorial page](https://www.bitcraze.io/documentation/tutorials/)
* [Simnet + Ardupilot academy](http://www.simnet.aero/academy)
* [Autonomy course Worcester Polytechnic Institute](https://pear.wpi.edu/teaching/rbe595/fall2023.html)
* [List of robotic aerial resources](http://www.kostasalexis.com/literature-and-links1.html)

## Credit

Lots of thanks for anybody contributing to this [linkedin post](https://www.linkedin.com/feed/update/urn:li:activity:7079385991144185856/). This was extremely helpful!
