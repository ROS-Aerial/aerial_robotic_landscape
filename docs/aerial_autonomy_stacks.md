# Aerial Autonomy Stacks

Based on [this discussion in Discourse]( https://discourse.ros.org/t/more-aerial-autonomy-stacks/30992/) and [our startup meeting](https://discourse.ros.org/t/start-up-meeting-aerial-robotics-wg/30869), we can define an aerial autonomy stack as follows:

> An aerial autonomy robotics stack is a collection of building blocks that enable the development of autonomous aerial vehicles, by providing a modular and scalable architecture for sensing, perception, planning, and control tasks. It allows unmanned aerial vehicles to perform complex missions without human intervention, while accommodating different hardware configurations and simulation environments.

## Comparison

From the paper 

> Fernandez-Cortizas, Miguel, et al. "Aerostack2: A Software Framework for Developing Multi-robot Aerial Systems." arXiv preprint arXiv:2303.18237 (2023).
  
the following autonomy stack table was extracted and adapted. 

| Flight stack   | OS/OC | Modular | Tested in | Middleware | last  update | MF  | RO  | MA  | MP  | PO  |
| -------------- | ----- | ------- | --------- | ---------- | ------------ | --- | --- | --- | --- | --- |
| Aerostack      | ✓    | ✓      | S,RIL,ROL   | ROS        | 10/2021      | ✗  | ✓  | ✓  | ✓  | ✗  |
| Aerostack2     | ✓    | ✓      | S,RIL,ROL   | ROS 2      | 03/2023      | ✓  | ✓  | ✓  | ✓  | ✓  |
| AerialCore     | ✓    | ✓      | S,RIL,ROL   | ROS        | 03/2023      | ✓  | ✓  | ✓  | ✗  | ✓  |
| Agilicious     | ✓    | ✓      | S,RIL      | ROS        | 03/2023      | ✗  | ✓  | ✗  | ✗  | ✗  |
| KumarRobotics  | ✓    | ✗      | S,RIL,ROL   | ROS        | 12/2022      | ✗  | ✓  | ✗  | ✓  | ✗  |
| CrazyChoir     | ✓    | ✗      | S,RIL      | ROS 2      | 02/2023      | ✗  | ✓  | ✓  | ✗  | ✗  |
| UAL            | ✓    | ✗      | S,RIL,ROL   | ROS        | 12/2022      | ✓  | ✗  | ✗  | ✓  | ✗  |
| XTDrone        | ✓    | ✓      | S         | ROS        | 03/2023      | ✗  | ✓  | ✗  | ✗  | ✗  |
| RotorS         | ✓    | ✓      | S         | ROS        | 07/2021      | ✗  | ✓  | ✗  | ✗  | ✗  |
| GAAS           | ✓    | ✓      | S         | ROS        | 10/2021      | ✗  | ✗  | ✗  | ✗  | ✗  |
| MRS AUV System | ✓    | ✓      | S,RIL,ROL   | ROS        | 09/2023      | ✓  | ✓  | ✓  | ✓  | ✗  |
| Crazyswarm     | ✓    | ✗      | S,RIL      | ROS        | 12/2022      | ✗  | ✓  | ✓  | ✗  | ✗  |
| Crazyswarm2     | ✓    | ✓      | S,RIL      | ROS 2       | 09/2023      | ✗  | ✓  | ✓  | ✗  | ✓  |


**Abbrivations**
* OS/OC: Open source or Open code
* S: Experiments in simulation
* RIL: Experiments in the lab
* ROL: Experiments outside the lab
* MF: Multi-frame 
* RO: Rate output
* MA: Multi agent
* MP: Multi platform
* PO: Plugin oriented

## VIO packages

Visual Inertial Odometry packages is an very important strategy of positioning within GPS deprived environments. Since UAVs can not use wheel odometry and heavily relient on cameras, this is one of the main drivers for autonomous exploration with these vehicles. 

Here is a list of VIO packages that people can use if they have a [depth camera](hardware.md) on their platform.

- [OpenVins](https://github.com/rpng/open_vins?tab=readme-ov-file) (ROS1/ROS2): 
- [VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) stand alone
- [SLAMcore](https://www.slamcore.com/product/) stand alone SDK
- [ORB-SLAM3 ROS2](https://github.com/suchetanrs/ORB-SLAM3-ROS2-Docker)

## Working list autonomy stacks

This is just a list of autonomy stacks with links, such that later we can add them to the overview.

Working list:
* [Aerostack2](https://aerostack2.github.io/)
* [Aerostack(1)](https://github.com/cvar-upm/aerostack/wiki)
* [KumarRobotics Autonomy Stack](https://github.com/KumarRobotics/kr_autonomous_flight)
* [Agilicious](https://agilicious.readthedocs.io/en/latest/index.html)
* [Crazyswarm2](https://imrclab.github.io/crazyswarm2/)
* [Crazyswarm(1)](https://crazyswarm.readthedocs.io/en/latest/)
* [MRS UAV System](https://github.com/ctu-mrs/mrs_uav_system)
* [Hector quadrotor](http://wiki.ros.org/hector_quadrotor)
* [RotorS](https://github.com/ethz-asl/rotors_simulator)
* RISE [paper](https://doi.org/10.55417/fr.2023015)
* [MRS AUV System](https://github.com/ctu-mrs/mrs_uav_system)
* [Clover](https://github.com/CopterExpress/clover)
* [/HKUST-Aerial-Robotics](https://github.com/HKUST-Aerial-Robotics)

## Partial autonomy packages

A list of packages which don't comprise a full stack but do offer value on top of basic flight controller firmware.

* [MAVROS Controllers](https://github.com/Jaeyoung-Lim/mavros_controllers)

## Indoor navigation packages
Given the above [Aerial Autonomy Stacks](https://github.com/ROS-Aerial/aerial_robotic_landscape/blob/main/aerial_autonomy_stacks.md#aerial-autonomy-stacks), the list below outlines specific implementations of indoor navigation software packages in ROS, running on aerial vehicle platforms. The list, though not exhaustive, provides a good overview of available off-the-shelf non-commercial software.

| Package name        | OS/OC | Sensors required         | Middleware | Simulator | Platform/controller | Last updated  |
| ------------------- | ----- | ------------------------ | ----------- | ----------| ------------------- | ------------- |
| [Ardupilot ROS](https://github.com/ArduPilot/ardupilot_ros/tree/humble)   | ✓     | LiDAR        | ROS 2 | Gazebo | Iris coptor,Ardupilot | 02/2024 |
| [as2_behaviour_tree](https://github.com/aerostack2/aerostack2/tree/main/as2_behavior_tree)   | ✓     | Unknown | ROS 2 | Gazebo | Crazyflie,DJI,Tello | 02/2024 |
| [Teach-Repeat-Replan](https://github.com/HKUST-Aerial-Robotics/Teach-Repeat-Replan) | ✓     | Stereo camera  | ROS 1 | MockaFly | DJI N3 | 11/2020 |
| [rtabmap](https://github.com/matlabbe/rtabmap_drone_example)    | ✓     | Stereo camera  | ROS 1 | Gazebo | PX4 | 05/2023 |
| [ORB_SLAM_3](https://github.com/arthurfenderbucker/indoor_drone)   | ✓     | Mono/stereo camera | ROS 1 | N/A | Bebop 2 | 06/2023 |
| [relative_nav](https://github.com/rleish/relative_nav) | ✗     | Stereo camera  | ROS 1 | N/A | Rotorcraft | 04/2017 |
| [zephyr](https://github.com/vatanaksoytezer/zephyr)    | ✓     | LiDAR        | ROS 1 | RotorS/Gazebo | AscTec Firefly | 11/2018 |
| [tum_ardrone](https://github.com/tum-vision/tum_ardrone)  | ✓     | Mono camera     | ROS 1 | N/A | AR.Drone | 05/2014 |
| [kr_autonomous_flight](https://github.com/KumarRobotics/kr_autonomous_flight)   | ✓    | Stereo camera/LiDAR/IMU | ROS 1 | Gazebo | Pixhawk | 08/2023 |
| [px4_sim_ros2](https://github.com/ParsaKhaledi/px4_sim_ros2)   | ✓    | Stereo camera | ROS 2 | Gazebo | PX4 | 04/2024 |

