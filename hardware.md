# Aerial robotics Hardware

This is information compiled from the latest [ICRA 2023 conference](https://www.icra2023.org/) held in London. 
About 75 Aerial robotics papers were found so here is a list of the standard platforms, companion computers and hardware used in the papers.
If some of the hardware is outdated, then an alternative is shown
This is a starting list that can be updated and extended by anyone.

## Standard Commercial Platforms
These are platforms that are currently commercially available for anybody to buy for their research.

- [Holybro X500 - PX4 Developer Kit](https://holybro.com/product/x500-v2-kit)
- [Crazyflie 2.1 - Bitcraze](https://www.bitcraze.io/products/crazyflie-2-1/)
- [Uvify IFO-S](https://www.uvify.com/ifo-s/)providedn included as well.
- [Tricopter voliro AG](https://voliro.com/)
- [DJI M100](https://www.dji.com/se/matrice100) Discontinued, look at:
    - [DJI M300](https://enterprise.dji.com/matrice-300)
- [DJI tello](https://store.dji.com/se/shop/tello-series)
- [NXP HoverGames Kit](https://www.nxp.com/design/designs/nxp-hovergames-drone-kit-including-rddrone-fmuk66-and-peripherals:KIT-HGDRONEK66) official hardware for the yearly [HoverGames Challenge](https://www.hovergames.com)

## Inhouse-developed platforms

These are platforms that are standard within a lab or department, with information of what it contains provided with perhaps build instructions.,

-  [Agilicous - University of Zurich](https://agilicious.readthedocs.io/en/latest/index.html)
-  [ModQuad - Lehigh University](http://swarmslab.com/projects/)
-  [RMF-Owl - Norwegian University of Science and Technology](https://ieeexplore.ieee.org/document/9836115)
-  [MiniHawk-VTOL](https://github.com/StephenCarlson/MiniHawk-VTOL)

## Components

Many of the UAVs are usually built by hand and composed of different components. This usually consists of a drone frame, fligth controller boards, companion computers and of course motors, batteries and ESCs. 

### Drone Frames
Many drone frames are usually built from carbon fiber and custom-made for application or research.
There are some frames that are provided that will provide some base:  
- [DJI Flame wheel ARF kit F550, F450, F330](https://www-v1.dji.com/flame-wheel-arf/feature.html)

### Flight controllers
- [Pixhawk 4](https://docs.px4.io/main/en/flight_controller/pixhawk4.html) discontinued, go look at:
   -  [Holybro's Pixhawk 6C](https://holybro.com/collections/autopilot-flight-controllers/products/pixhawk-6c) 
   -  [CUAV's Pixhawk V6x](https://doc.cuav.net/flight-controller/pixhawk-v6x/en/#building-firmware)
-  [mRo PixRacer R15](https://store.mrobotics.io/product-p/auav-pxrcr-r15-mr.htm)
-  [Crazyflie Bolt 1.1](https://www.bitcraze.io/products/crazyflie-bolt-1-1/)

### Companion Computers
For the drones that can carry it, the companion computers are important since they can do additional computation that the flight controller can not easily do.
As these are capable of running some form of Linux, these can handle for instance  computer vision with [OpenCV](https://opencv.org/) or run nodes with [ROS](https://www.ros.org/)

- [Nvidia Jetson Xavier](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-xavier-nx/) or the [TX2 Module](https://developer.nvidia.com/embedded/jetson-tx2)
- [Intel Nuc Boards](https://www.intel.com/content/www/us/en/products/details/nuc/boards/products.html)
- [Raspberry PI 3 (A+)](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/) or [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [Khadas Vim3](https://www.khadas.com/vim3)
- [Odroid (various boards](https://www.hardkernel.com/product-category/odroid-board/)
- [NXP NAVQPlus](https://www.nxp.com/design/designs/navqplus-ai-ml-companion-computer-evk-for-mobile-robotics-ros-ground-stations-and-camera-heads:8MPNAVQ)
- [Qualcomm RB5](https://developer.qualcomm.com/qualcomm-robotics-rb5-kit)
  
### ESCs Motors batteries
Still to be added!
