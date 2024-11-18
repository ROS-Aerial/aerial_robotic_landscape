# Simulation of Aerial Robotics

Simulation is crucial when working with Unmanned Aerial Vehicles (UAVs). Testing different trajectories and control paradigms in a simulator before implementing them on the real platform ensures not only safety but also facilitates development.

This page presents several simulator options for aerial robotics enthusiasts.

## Comparison

The following simulators have their own integrated physics simulation and basic rendering capabilities. They are capable of simulating the aerodynamic forces necessary to keep UAVs airborne:

For the following comparison, we have refered to this article:
> C. A. Dimmig et al., "Survey of Simulators for Aerial Robots: An Overview and In-Depth Systematic Comparisons," in IEEE Robotics & Automation Magazine, doi: 10.1109/MRA.2024.3433171

The Arxiv prepint of the paper can be found [here](https://arxiv.org/abs/2311.02296)

### Features

List migh not be complete. If you see any error or missing components, feel free to open a PR or issue.


| Name | Physics Engine | Rendering | Linux[^1] | Windows[^1] | MacOS[^1] | Interface | (S/H)ITL[^6] | Active[^2] | Hardware requirement[^3] | Licence | Open source[^4] | Interest [^5] |
| -------------------------------------------------- | -------------------------- | --------- | --------- | --------- | ----- | -------------- | ------------------ | ------ | -------------------- | -------- | ----------- | -------------- |
|[Gazebo](https://classic.gazebosim.org/) (<br/>[RotorS](https://github.com/ethz-asl/rotors_simulator), <br/> [CrazyS](https://github.com/gsilano/CrazyS), <br/> [PX4 SITL](https://docs.px4.io/v1.12/en/simulation/gazebo.html#gazebo-simulation)) | ODE/ Bullet/ DART/ Simbody | OGRE | ✓ <br/>( ✓ <br/> ✓ <br/> ✓ )| ✱ <br/>( ✗ <br/> ✗ <br/> ✗)| ✓ <br/>( ✗ <br/> ✗ <br/> ✗ )| ROS 1/2, C++, RL | PX4, ArduPilot, CF[^7] | ✓ <br/>( ✗ <br/> ✱ <br/> ✗ ) | minimal/decent |Apache 2.0| ✓ | High |
|[Gazebo](https://gazebosim.org/) | Bullet/ DART/ TPE | OGRE | ✓ | ✱ | ✓ | ROS 1/2, C++, Python, RL | PX4, ArduPilot, CF | ✓ | minimal/decent |Apache 2.0| ✓ | High |
|[Isaac](https://developer.nvidia.com/isaac-sim) (<br/>[Pegasus](https://pegasussimulator.github.io/), <br/>[Aerial Gym](https://github.com/ntnu-arl/aerial_gym_simulator)) | NVIDIA PhysX/ Flex | Vulkan | ✓ | ✗ | ✗ | ROS 1/2, Python, RL | Pegasus: PX4 | ✓ | high/demanding |[NVIDIA OMNIVERSE](https://docs.omniverse.nvidia.com/isaacsim/latest/common/NVIDIA_Omniverse_License_Agreement.html)<br/>(BSD 3)| ✗ <br/> (✓ <br/> ✓) | User specific |
|[Webots](https://www.cyberbotics.com/)| ODE | OpenGL | ✓ | ✓ | ✓ | ROS 1/2, C/C++, Python, MATLAB, Java | ArduPilot, CF | ✓ | decent/high |Apache 2.0| ✓ | Developing |
|[CoppeliaSim](https://www.coppeliarobotics.com/)| Bullet/ODE/Vortex/Newton/MuJoCo | OpenGL | ✓ | ✓ | ✓ | ROS 1/2, C/C++, Python, MATLAB, Java,Lua,Octave | -- | ✓ | decent/high |GNU GPL/Commercial| ✱ | Decent |
|[AIRsim](https://github.com/microsoft/AirSim)| NVIDIA PhysX | Unreal,Unity | ✓ | ✓ | ✓ | ROS 1, C++, Python, C#, Java,RL | PX4, ArduPilot | ✗ | medium/high |MIT| ✓ | Low |
|[Flightmare](https://github.com/uzh-rpg/flightmare)| Ad hoc, Gazebo classic | Unity | ✓ | ✗ | ✗ | ROS 1, C++, RL | -- | ✗ | -- |MIT| ✓ | Low |
|[FlightGoggles](https://flightgoggles.mit.edu/)| Ad hoc | Unity | ✓ | ✱ | ✗ | ROS 1, C++ | Motion capture | ✗ | -- |MIT| ✓ | Unknown |
|[Gym-pybullet-drones](https://github.com/utiasDSL/gym-pybullet-drones)| [Pybullet](https://pybullet.org/wordpress/) | OpenGL | ✓ | ✱ | ✓ | Python, RL | Betaflight, CF | ✓ | minimal/decent/high |MIT (Pybullet: [zlib](https://github.com/bulletphysics/bullet3/blob/master/LICENSE.txt))| ✓ | High |
|[RotorTM](https://github.com/arplaboratory/RotorTM)| Ad hoc | OpenGL | ✓ | ✗ | ✗ | ROS 1, Python, MATLAB | -- | ✓ | -- |GNU GPL| ✓ | Unknown |
|[MATLAB UAV Toolbox](https://www.mathworks.com/products/uav.html)| MATLAB | Unreal | ✓ | ✓ | ✓ | ROS 2, MATLAB | PX4 | ✓ | -- |Proprietary, Commercial| ✗ | Unknown |
| [O3de](https://o3de.org/) | NVIDIA PhysX/ NVIDIA Cloth/ AMD TressFX | Atom | ✓ | ✓ | ✱ | ROS 2[^8] , C++ | unknown | ✓ | decent/high | Apache-2.0/MIT | ✓ | Developing |
| [Drake](https://drake.mit.edu/) | ad hoc | unknown | ✓ | ✗ | ✓ | C++, Python, ROS 2 | unknown | ✓ | unknown | BSD 3 | ✓ | Developing |
| [Flightgear](https://www.flightgear.org/) | unknown | unknown | ✓ | ✓ | ✓ | C++ | unknown | ✓ | minimal/decent | GNU-GPL | ✓ | Low |
| [RealFlight](https://www.realflight.com/) | unknown | unknown | ✗ | ✓ | ✗ | --  | unknown | ✓ | minimal/decent | non-public | ✗ | Low |
| [RotorPy](https://github.com/spencerfolk/rotorpy) | ad hoc | unknown | ✓ | ✓ | ✓ | Python | -- | ✓ | minimal/decent | MIT | ✓ | Developing |


[^1]: ✓: Full support,  ✱: Partial support,  ✗: No support

[^2]: ✓: Active and maintained,  ✱: Inactive but  responding to issues/ PR,  ✗: Inactive for 2+ years

[^3]: For a referance, a laptop running Intel i5 10th gen (or similar) with 8gb ddr4 ram and NVIDIA T100 4gb (or similar) are considered as minimal requirement.

[^4]: ✓: Yes,  ✱: Yes for non commercial use-case ,  ✗: No

[^5]: Usage in Aerial ROS/Robotics community according to several survey on Discourse and during the meetings.

[^6]: (Software/Hardware) In The Loop

[^7]: Crazyflie

[^8]: It seem under development and there is [some docs](https://docs.o3de.org/docs/user-guide/interactivity/robotics/project-configuration/) out there.


## Vehicle types


| Simulator                             | Multirotor (Basic) | Multirotor (Drag) | Multirotor (Wind) | Fixed-wings | Aerial Manipulators | Swarms     | Cars | Other vehicles |
| ------------------------------------- | ------------------ | ----------------- | ----------------- | ----------- | ------------------- | ---------- | ---- | -------------- |
| Gazebo (Classic & New)                |         ✓          |         ✓         |         ✓         |      ✓      |          ✱          |    ✱       |   ✓  |        ✓       |
| Isaac (Pegasus, Aerial Gym)           |         ✓          |     ✗(✓,✗)        |         ✗         |      ✗      |          ✗          |    ✓       |✓(✗,✗)|     ✓(✗,✗)     |
| Webots                                |         ✓          |         ✗         |         ✗         |      ✗      |          ✗          |    ✱       |   ✓  |        ✓       |
| CoppeliaSim                           |         ✓          |         ✓         |         ✱         |      ✗      |          ✱          |    ✱       |   ✓  |        ✓       |
| AirSim                                |         ✓          |         ✓         |         ✓         |      ✗      |          ✗          |    ✱       |   ✓  |        ✗       |
| Flightmare                            |         ✓          |         ✓         |         ✗         |      ✗      |          ✗          |    ✓       |   ✗  |        ✗       |
| FlightGoggles                         |         ✓          |         ✓         |         ✗         |      ✗      |          ✗          |    ✗       |   ✓  |        ✗       |
| gym-pybullet-drones                   |         ✓          |         ✓         |         ✗         |      ✗      |          ✗          |    ✓       |   ✗  |        ✗       |
| RotorTM                               |         ✓          |         ✗         |         ✗         |      ✗      |          ✓          |    ✓       |   ✗  |        ✗       |
| MATLAB UAV Toolbox                    |         ✓          |         ✓         |         ✓         |      ✓      |          ✗          |    ✱       |   ✗  |        ✗       |
| O3de*                                 |         ~          |         ?         |         ?         |      ?      |          ?          |    ?       |   ~  |        ~       |
| Drake*                                |         ?          |         ?         |         ?         |      ?      |          ?          |    ?       |   ?  |        ?       |
| RotorPy*                              |         ~          |         ~         |         ~         |      ✗      |          ✗          |    ~       |   ✗  |        ✗       |

- [ * ] : Unknown data. If you have information on specific topic, please comment bellow with the referance link.
    - [ ~ ] : Yes according to my knowledge but it needs development.
    - [ ? ] : Unknown
    - [ ✗ ] : No according to my research.
- [ ✓ ] : Yes
- [ ✱ ] : Yes. But not specifically designed for it
- [ ✗ ] : No


## Sensor support

TODO

## Flight dynamics models

Some simulators mostly focus on creating accurate dynamics for aerial vehicles. Here are some options:

* JSBSim (<https://github.com/JSBSim-Team/jsbsim>)
* YASim (<https://wiki.flightgear.org/YASim>)
* More to be added!

## Available UAV Models

Each simulator typically offers a range of ready-to-use aerial vehicle models:

* **Gazebo**: <https://app.gazebosim.org/search;q=uav>

[//]: # ( Wrong link. Unable to find correct link rn. * **Isaac Sim**: https://docs.omniverse.nvidia.com/isaacsim/latest/reference_assets.html#aerial-robots)

* **Webots**: <https://webots.cloud/proto?keyword=robot%2Fflying>

## Autopilot Suites

Several autopilot suites provide instructions for using simulators, often with Software-in-the-Loop (SITL) or Hardware-in-the-Loop (HITL) options:

* **Ardupilot**: <https://ardupilot.org/copter/docs/common-simulation.html>
* **Betaflight**: <https://betaflight.com/docs/development/SITL#sitl-in-realflight-9>
* **Crazyflie**: <https://www.bitcraze.io/documentation/tutorials/getting-started-with-simulation/>
* **DJI**: <https://www.dji.com/se/simulator>
* **Paparazzi UAV**: <https://wiki.paparazziuav.org/wiki/Simulation>
* **PX4**: <https://docs.px4.io/main/en/simulation/#simulation>
* **ROSflight**: <https://docs.rosflight.org/v1.3/user-guide/gazebo_simulation/>

This page was last updated: *{{ git_revision_date_localized }}*

--8<-- "docs/goatcounter.html"
