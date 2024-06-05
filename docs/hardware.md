# Hardware, Components, and Dev Kits

This is an list of development platforms for aerial robotics. Please start a pull request if you'd like to update these.

## Standard Commercial Research Platforms

These are platforms that are currently commercially available for anybody to buy for their research.

- Holybro:
   - [Holybro X500 V2 - PX4 Developer Kit](https://holybro.com/product/x500-v2-kit)
   - [PX4 Vision Dev Kit V1.5](https://holybro.com/collections/multicopter-kit/products/px4-vision-dev-kit-v1-5)
- ModalAI:
       - [PX4 Autonomy Dev Kit](https://www.modalai.com/products/px4-autonomy-developer-kit?variant=46969885950256)
       - [Starling 2](https://www.modalai.com/products/starling-2?variant=48173890175280) and [Starling 2 Max](https://www.modalai.com/products/starling-2-max?variant=48172375310640)
- [Crazyflie 2.1 - Bitcraze](https://www.bitcraze.io/products/crazyflie-2-1/)
- [NXP HoverGames Kit](https://www.nxp.com/design/designs/nxp-hovergames-drone-kit-including-rddrone-fmuk66-and-peripherals:KIT-HGDRONEK66) official hardware for the yearly [HoverGames Challenge](https://www.hovergames.com)
- Duckietown:
    - [Duckiedrone DD21](https://get.duckietown.com/products/duckiedrone-dd21)
    - [Duckiedrone DD24](https://get.duckietown.com/products/autonomous-raspberrypi-quadcopter-duckiedrone-dd24)
- [Clover by Coex](https://coex.tech/clover)
- [PX4 Autonomy Developer Kit by ModelAI](https://www.modalai.com/collections/drones/products/px4-autonomy-developer-kit)
- [Droneblocks DEXI 5](https://droneblocks.io/program/dexi-5-px4-stem-drone-kit/)
- [3DR Quad Zero Kit](https://store.3dr.com/3dr-quad-zero-kit/)

## Industrial Platforms

- [Uvify IFO-S](https://www.uvify.com/ifo-s/)
- [Tricopter voliro AG](https://voliro.com/)
- [DJI M300](https://enterprise.dji.com/matrice-300)


## Inhouse-developed platforms

These are platforms that are standard within a lab or department, with information of what it contains provided with perhaps build instructions.,

-  [Agilicous - University of Zurich](https://agilicious.readthedocs.io/en/latest/index.html)
-  [ModQuad - Lehigh University](http://swarmslab.com/projects/)
-  [RMF-Owl - Norwegian University of Science and Technology](https://ieeexplore.ieee.org/document/9836115)
-  [MiniHawk-VTOL](https://github.com/StephenCarlson/MiniHawk-VTOL)

## Discontinued Platforms

- DJI M100
- [DJI tello](https://store.dji.com/se/shop/tello-series)


## Components

Many of the UAVs are usually built by hand and composed of different components. This usually consists of a drone frame, flight controller boards, companion computers and of course motors, batteries and ESCs.

### Drone Frames

Many drone frames are usually built from carbon fiber and custom-made for application or research.
There are some frames that are provided that will provide some base:
- [DJI Flame wheel ARF kit F550, F450, F330](https://www-v1.dji.com/flame-wheel-arf/feature.html)
- [Momentum Drones DEV-7](https://momentumdrones.com/products/dev7-frame-kit)

### Flight controllers
- Holybro
   -  [Pixhawk 4](https://docs.px4.io/main/en/flight_controller/pixhawk4.html) 
   -  [Holybro Pixhawk 6C](https://holybro.com/collections/autopilot-flight-controllers/products/pixhawk-6c)
   -  [Holybro Pixhawk 6X](https://holybro.com/products/pixhawk-6x)
   -  [Holybro Pixhawk 6X PRO](https://holybro.com/collections/autopilot-flight-controllers/products/pixhawk-6x-pro)
-  [CUAV's Pixhawk V6x](https://doc.cuav.net/flight-controller/pixhawk-v6x/en/#building-firmware)
-  mRobotics/3DR
   - [mRo PixRacer R15](https://store.mrobotics.io/product-p/auav-pxrcr-r15-mr.htm) discontinued, go look at:
   - [mRo PixRacerPro](https://store.3dr.com/pixracer-pro/)
   - [3DR Control Zero Classic](https://store.3dr.com/control-zero-classic/)
   - [3DR Control Zero H7 OEM](https://store.3dr.com/control-zero-h7-oem/)
   - [3DR Reference Design Carrier Board](https://store.3dr.com/reference-design-carrier-board/)
   - [3DR "Stick" Adapter (Carrier Board)](https://store.3dr.com/stick-adapter-carrier-board/)
- [Crazyflie Bolt 1.1](https://www.bitcraze.io/products/crazyflie-bolt-1-1/)
- ARK Electronics
   - [ARK Electronics ARKV6X](https://arkelectron.com/product/arkv6x)
   - [ARK Electronics Pi6X Flow](https://arkelectron.com/product/ark-pi6x-flow/)



### Companion Computers

For the drones that can carry it, the companion computers are important since they can do additional computations that the flight controller can not easily do.
As these are capable of running some form of Linux, these can handle for instance  computer vision with [OpenCV](https://opencv.org/) or run nodes with [ROS](https://www.ros.org/). 
Some companion computers also integrate flight control (RTOS) hardware in the same package

- [Nvidia Jetson Xavier](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-xavier-nx/) or the [TX2 Module](https://developer.nvidia.com/embedded/jetson-tx2)
- [Nvidia Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
- [Intel Nuc Boards](https://www.intel.com/content/www/us/en/products/details/nuc/boards/products.html)
- [Raspberry PI 3 (A+)](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/) or [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [Khadas Vim3](https://www.khadas.com/vim3)
- [Odroid (various boards)](https://www.hardkernel.com/product-category/odroid-board/)
- [NXP NAVQPlus](https://www.nxp.com/design/designs/navqplus-ai-ml-companion-computer-evk-for-mobile-robotics-ros-ground-stations-and-camera-heads:8MPNAVQ)
- [Qualcomm RB5](https://developer.qualcomm.com/qualcomm-robotics-rb5-kit)
- [MRD5165 Eagle Kit](https://www.mistralsolutions.com/product/mrd5165-eagle-kit/) (coming soon)
- [VOXL 2 by Model AI](https://www.modalai.com/collections/blue-uas-framework-components/products/voxl-2)
- [EchoPilot AI](https://echomav.com/product/echopilot-ai/)
- [AMD Xilinx Kria Starter Kits](https://www.amd.com/en/products/system-on-modules/kria.html)
- [LattePanda x86 boards](https://www.lattepanda.com/)
### Carrier boards
Several vendors have developed carrier boards that can expose input/output ports of companion computers mentioned above which are packaged in a System-on-Module (SoM) form factor and also offer a standard interface for plugging in popular flight controllers/their own FCs.

- [Mistral MRD5165 Eagle based on Qualcomm RB5](https://www.mistralsolutions.com/mrd5165-eagle-kit/)
- [ARK Electronics Jetson PAB carrier](https://arkelectron.com/product/ark-jetson-pab-carrier/)
- [ARK Electronics Pi6X Flow](https://arkelectron.com/product/ark-pi6x-flow)
- [Holybro Jetson Baseboard](https://holybro.com/products/pixhawk-jetson-baseboard?variant=43818665148605)
- [Dronee Lychee Drone autopilot hardware](https://dronee.aero/pages/lychee)
- [Airvolute DroneCore2 Jetson + Cube](https://airvolute.com/dronecore-2/)

### Depth Cameras
- [Intel RealSense T265 ](https://www.intel.com/content/www/us/en/products/sku/192742/intel-realsense-tracking-camera-t265/specifications.html) Discontinued, look at:
  - [RealSense D455](https://www.intelrealsense.com/depth-camera-d455/)
  - [RealSense D435i](https://www.intelrealsense.com/depth-camera-d435i/)
- Oak-d Series like [OAK-D Pro](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9098pro/) or [OAK-D-Lite](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095/)
- [VOXL CAM by ModelAI](https://www.modalai.com/collections/blue-uas-framework-components/products/voxl-cam?variant=39543794565171)

### Monocular Cameras
- [Raspberry PI Cameras](https://www.raspberrypi.com/documentation/accessories/camera.html) Compatible with RPI. IMX219 and IMX477 based cameras compatible with Jetson Xavier, NX, Nano, Orin series (other models may require device tree overlays or source changes).
- [Google Coral Camera](https://coral.ai/products/camera) Compatible with NXP NAVQPLUS

### TOF Cameras
- [Liteon A65 Camera Starter Kit](https://www.emcraft.com/products/1111) Check with vendor for NXP NAVQPLUS compatibility.
- [PMD Flexx2 3D Camera](https://www.emcraft.com/products/1178) USB version should be compatible with most companion computers.
- [VOXL2 TOF Depth Sensor ](https://docs.modalai.com/M0171/) Compatible with VOXL2. Check with vendor for early access product.

### Reference Bill of Materials

#### Holybro S500v2

The [Holybro S500v2](https://holybro.com/collections/s500/products/s500-v2-development-kit) is a popular, relatively low-cost quadcopter. This is a list of the parts used with details of battery, motors, ESCs, and propellers with reference links to guide custom builds.


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
<https://tabletomarkdown.com/convert-spreadsheet-to-markdown/>

--8<-- "docs/goatcounter.html"
