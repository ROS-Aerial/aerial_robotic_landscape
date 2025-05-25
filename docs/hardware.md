# Hardware
The main hardware components of drones can be seperated into processors, sensors, telemetry, and motor drivers (speed controllers). Here we compare the current avalible options for each compenent and further categorize each one of them based on type and functionality. 

![Example of UAV wiring diagram](images/Pixhawk5X.jpg)

Above is an example wiring diagram of a UAV using the [Holybro Pixhawk 5X Flight Controller](https://docs.px4.io/main/en/flight_controller/pixhawk5x.html) in family of Pixhawk® flight controllers. **Note** This a relativly advanced controller, here to illustrate what the wiring diagram of a UAV might look like. Simpler controllers might not be as complex depending on requirments. 

---
## Processors 
Processors are the main component in which computation takes place within a UAV. All electrical components such as sensors and telemetry are connected to this system. A UAV can consist of 1 or multiple processors depending on complexity, typically this is structed into a primary procssor (flight controller) which handles low level operations such as internal pose estimation and navigation, and secondary processors (companion computers) which are used for high level autonomy such as perception sensing or onboard decisions planning. 

### Flight Controllers
Comparison of MCUs, sensors and licenses for Open-Source Hardware (OSH) flight controller platforms.
_All platforms have IMUs. Interfaces: UART, PWM, I2C._ [[1]](#references)

| Platform        | MCU           | Sensors      | Interfaces                          | License             |
|-----------------|---------------|--------------|-------------------------------------|---------------------|
| Pixhawk         | STM32F427     | b, m         | c, s, a, pp, sb, ds                 | BSD-2-Clause        |
| Pixhawk 2       | STM32F427     | b, m         | c, s, a, pp, sb, ds                 | CC-BY-SA-3.0        |
| PixRacer        | STM32F427     | b, m         | c, pp, sb, ds                       | CC-BY-4.0           |
| Pixhawk 3 Pro   | STM32F427     | b, m         | c, s, pp, sb, ds                    | CC-BY-4.0           |
| PX4 FMUv5 & v6  | STM32F427     | b, m         | c, s, a, pp, sb, ds                 | CC-BY-4.0           |
| Sparky2         | STM32F405     | b, m         | c, pp, sb, ds, da                   | CC-BY-NC-SA-4.0     |
| Chimera         | STM32F767     | b, m, p      | c, s, a, da, pp, sb, ds, x, au      | GPL-2.0             |
| CC3D            | STM32F103     | None         | pp, ds, sb                          | GPL-3.0             |
| Atom            | STM32F103     | None         | pp, ds, sb                          | GPL-3.0             |
| APM 2.8         | ATmega2560    | b            | pp, a                               | GPL-3.0             |
| FlyMaple        | STM32F103     | b, m         | –                                   | GPL-3.0             |
| Erle-Brain 3    | Raspberry Pi  | b, m         | a                                   | CC-BY-NC-SA-4.0     |
| PXFmini         | Raspberry Pi  | b, m         | a                                   | CC-BY-NC-SA-4.0     |
| AeroQuad [d]    | STM32F407     | b, m         | –                                   | GPL-2.0             |
| Mikrokopter [d] | ATmega644     | b            | s, pp                               | –                   |
| MatrixPilot [d] | dsPIC33FJ256  | None         | –                                   | GPL-3.0             |

> **Notes:**
> - b: barometer; m: magnetometer; p: pitot tube sensor c: CAN; s: SPI; a: ADC; pp: PPM; sb: S.BUS; ds: DSM; da: DAC; x: XBEE; au: AUX, [d]: discontinued

### Companion Computers
For the drones that can carry it, the companion computers are important since they can do additional computations that the flight controller can not easily do. As these are capable of running some form of Linux, these can handle for instance  computer vision with [OpenCV](https://opencv.org/) or run nodes with [ROS](https://www.ros.org/). 
Some companion computers also integrate flight control (RTOS) hardware in the same package

- [Nvidia Jetson Xavier](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-xavier-nx/) or the [TX2 Module](https://developer.nvidia.com/embedded/jetson-tx2)
- [Nvidia Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
- [ASUS NUC Boards](https://www.asus.com/se/displays-desktops/nucs/nuc-mini-pcs/asus-nuc-14-pro/)
- [Raspberry PI  (A+)](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Khadas Vim3](https://www.khadas.com/vim3)
- [Odroid (various boards)](https://www.hardkernel.com/product-category/odroid-board/)
- [NXP NAVQPlus](https://www.nxp.com/design/designs/navqplus-ai-ml-companion-computer-evk-for-mobile-robotics-ros-ground-stations-and-camera-heads:8MPNAVQ)
- [Qualcomm RB5](https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit)
- [MRD5165 Eagle Kit](https://www.mistralsolutions.com/product/mrd5165-eagle-kit/)
- [VOXL 2 by Model AI](https://www.modalai.com/collections/blue-uas-framework-components/products/voxl-2)
- [EchoPilot AI](https://echomav.com/product/echopilot-ai/)
- [AMD Xilinx Kria Starter Kits](https://www.amd.com/en/products/system-on-modules/kria.html)
- [LattePanda x86 boards](https://www.lattepanda.com/)
- 
### Carrier boards
Several vendors have developed carrier boards that can expose input/output ports of companion computers mentioned above which are packaged in a System-on-Module (SoM) form factor and also offer a standard interface for plugging in popular flight controllers/their own FCs.

- [Mistral MRD5165 Eagle based on Qualcomm RB5](https://www.mistralsolutions.com/mrd5165-eagle-kit/)
- [ARK Electronics Jetson PAB carrier](https://arkelectron.com/product/ark-jetson-pab-carrier/)
- [ARK Electronics Pi6X Flow](https://arkelectron.com/product/ark-pi6x-flow)
- [Holybro Jetson Baseboard](https://holybro.com/products/pixhawk-jetson-baseboard?variant=43818665148605)
- [Dronee Lychee Drone autopilot hardware](https://dronee.aero/pages/lychee)
- [Airvolute DroneCore2 Jetson + Cube](https://airvolute.com/dronecore-2/)

---
## Sensors 
### Navigation and Localization Sensors 
- TO DO

### Perception Sensors
### Depth Cameras
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

### Event Cameras
- [OpenMV N6](https://openmv.io/collections/cameras/products/openmv-n6?variant=41573456576606)

---
## Telemetry
- TO DO

---
## Motor Drivers (Electronic Speed Controllers (ESC))
- TO DO

---
## References
1. Ebeid, E., Skriver, M., Terkildsen, K.H., Jensen, K. and Schultz, U.P. (2018) A Survey of Open-Source UAV Flight Controllers and Flight Simulators. Microprocessors and Microsystems, 61, 11-20.
[https://doi.org/10.1016/j.micpro.2018.05.002.](https://doi.org/10.1016/j.micpro.2018.05.002)

This page was last updated: *{{ git_revision_date_localized }}*

--8<-- "docs/goatcounter.html"

