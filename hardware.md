# Work In Progress

We are still hard at work at mapping the hardware landscape, if you see anything missing please send a PR, we want to encourage manufacturers to help us make this a complete list

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
- [Duckiedrone by Duckietown](https://get.duckietown.com/products/duckiedrone-dd21)
- [Clover by Coex](https://coex.tech/clover)

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
As these are capable of running some form of Linux, these can handle for instance  computer vision with [OpenCV](https://opencv.org/) or run nodes with [ROS](https://www.ros.org/). Some 
companion computers also integrate flight control (RTOS) hardware
in the same package.

- [Nvidia Jetson Xavier](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-xavier-nx/) or the [TX2 Module](https://developer.nvidia.com/embedded/jetson-tx2)
- [Intel Nuc Boards](https://www.intel.com/content/www/us/en/products/details/nuc/boards/products.html)
- [Raspberry PI 3 (A+)](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/) or [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [Khadas Vim3](https://www.khadas.com/vim3)
- [Odroid (various boards](https://www.hardkernel.com/product-category/odroid-board/)
- [NXP NAVQPlus](https://www.nxp.com/design/designs/navqplus-ai-ml-companion-computer-evk-for-mobile-robotics-ros-ground-stations-and-camera-heads:8MPNAVQ)
- [Qualcomm RB5](https://developer.qualcomm.com/qualcomm-robotics-rb5-kit)
- [MRD5165 Eagle Kit](https://www.mistralsolutions.com/product/mrd5165-eagle-kit/) (coming soon)
- [EchoPilot AI](https://echomav.com/product/echopilot-ai/)

### Reference Bill of Materials

#### Holybro S500v2

The [Holybro S500v2](https://holybro.com/collections/s500/products/s500-v2-development-kit) is a popular, relatively low-cost quadcopter. This is a list of the parts used with details of battery, motors, ESCs, propellers with reference links to guide custom builds.


| S.No | Part Name                               | Part category           | Description                                               | Price (USD) | Qty         | Total Cost (USD) | Official/Reference Link                                                                                                                                                              |
| ---- | --------------------------------------- | ----------------------- | --------------------------------------------------------- | ----------- | ----------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | Holybro S500 frame                      | Frame                   | With landing gear, 385x385mm                              | 42          | 1           | 42               | [https://holybro.com/collections/s500/products/s500-v2-kit?variant=42724497391805](https://holybro.com/collections/s500/products/s500-v2-kit?variant=42724497391805)                 |
| 2    | Holybro Pixhawk 6C + GPS + Power module | FC + GPS + Power module | PM02 power module, M9N GPS                                | 290         | 1           | 290              | [https://holybro.com/products/pixhawk-6c?variant=43005243785405](https://holybro.com/products/pixhawk-6c?variant=43005243785405)                                                     |
| 3    | Holybro 2216 920KV CW                   | Motor                   | 19x19 mounting clockwise rotation                         | 20          | 2           | 40               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094608061](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094608061)                           |
| 4    | Holybro 2216 920KV CCW                  | Motor                   | 19x19 mounting counter-clockwise rotation                 | 20          | 2           | 40               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094640829](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094640829)                           |
| 5    | BLHeli S 20A ESC                        | ESC                     | Electronic Speed Controller to drive motors               | 14          | 4           | 56               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094706365](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094706365)                           |
| 6    | 1045 propellers                         | Props                   | 10x4.5" kit of 2 pairs                                    | 12          | 1           | 12               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094313149](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094313149)                           |
| 7    | Radiomaster R81 receiver                | Radio receiver          | Used for manually flying drone Line of Sight/testing\*    | 18          | 1           | 18               | [https://holybro.com/products/radiomaster-r81-receiver](https://holybro.com/products/radiomaster-r81-receiver)                                                                       |
| 8    | Holybro SiK telemetry radio v3          | Telemetry link radio    | 500mW, 433MHz variant, pair of transmitter + receiver\*\* | 63          | 1           | 63               | [https://holybro.com/products/sik-telemetry-radio-v3?variant=42801817485501](https://holybro.com/products/sik-telemetry-radio-v3?variant=42801817485501)                             |
| 9    | Tattu 5200mAh 4S                        | Battery                 | 4S1P XT60 plug 35C                                        | 63          | 1           | 63               | [https://genstattu.com/tattu-5200mah-14-8v-35c-4s1p-lipo-battery-pack-with-xt60-plug.html](https://genstattu.com/tattu-5200mah-14-8v-35c-4s1p-lipo-battery-pack-with-xt60-plug.html) |
|      |                                         |                         |                                                           |             | Grand Total | 624              |                                                   |             |             |                  |

**Notes**:

\*It can be used with Radiomaster Multiprotocol (4 in 1) or CC2500 based Radio Controller like FrSky Taranis X9D or similar<br>
\*\*Used for connecting to ground control station, 915MHz variant also available  

**Useful tool for this page**:
https://tabletomarkdown.com/convert-spreadsheet-to-markdown/
