# Middleware and Drivers

The aim for this page is to provide a collection of ROS packages/related libraries which are very useful for aerial ROS projects either to serve as a reference or directly use as a part of a custom software stack. This list aims to address the gap between the flight controller firmware and purely autonomy related packages.

## Middleware libraries

Enabling low overhead publish/subscribe on microcontrollers:

1. [Micro-XRCE-DDS](https://github.com/eProsima/Micro-XRCE-DDS)
2. [Zenoh](https://github.com/eclipse-zenoh/zenoh-plugin-dds)
3. [PX4-FastRTPS](https://github.com/eProsima/px4_to_ros) - superceded by [Micro-XRCE-DDS](https://docs.px4.io/main/en/middleware/uxrce_dds.html)

## Driver packages for drone platforms

ROS packages built atop SDKs from drone vendors to interface to their closed-source flight controller firmwares. Several of these may be for much older ROS1 distros but can have utility in terms of serving as references.

1. [Parrot ARDrone Autonomy](https://github.com/AutonomyLab/ardrone_autonomy)
2. [Parrot Bebop Autonomy](https://github.com/AutonomyLab/bebop_autonomy)
3. [Parrot ANAFI Autonomy](https://github.com/andriyukr/anafi_autonomy)
4. DJI Tello driver [ROS1](https://github.com/anqixu/tello_driver), [ROS2 pre-Jazzy](https://github.com/clydemcqueen/tello_ros), [ROS2 Jazzy and Beyond](https://github.com/arjo129/tello_ros)
5. [Parrot Mambo driver](https://github.com/TOTON95/ros_pyparrot)

This page was last updated: *{{ git_revision_date_localized }}*

--8<-- "docs/goatcounter.html"
