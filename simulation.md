# Simulation of Aerial Robotics

Simulation is crucial when working with Unmanned Aerial Vehicles (UAVs). Testing different trajectories and control paradigms in a simulator before implementing them on the real platform ensures not only safety but also facilitates development.

This page presents several simulator options for aerial robotics enthusiasts.

## Simulators

The following simulators have their own integrated physics simulation and basic rendering capabilities. They are capable of simulating the aerodynamic forces necessary to keep UAVs airborne:

* **AIRsim** (https://github.com/microsoft/AirSim): An open-source project for aerial vehicle simulation by Microsoft.
* **Flightgear** (https://www.flightgear.org/) This open source simulator is mostly meant for training pilots but have been used for UAvs as well. This simulator JBSsim with unreal engine
* **Gazebo** (https://gazebosim.org/): A staple simulation widely used by the robotics and ROS (Robot Operating System) community.
* **Isaac Sim** (https://developer.nvidia.com/isaac-sim): A simulator built by Nvidia for robotics with a strong focus on rendering.
* **Pybullet** (https://pybullet.org/wordpress/): A real-time physics simulation that easily interfaces with Python.
* **RealFlight** (https://www.realflight.com/): A simulator heavily used in the RC (Remote Control) community.
* **Webots** (https://www.cyberbotics.com/): Another versatile robotics simulator with excellent ROS support.
* **XPlane** (https://www.x-plane.com/) Similar to Flightgear (but then with a commercial license) this simulator was initially made for realistically flying planes for pilots, although it have been used for UAV flight.
* **Drake** (https://drake.mit.edu/): Drake, a C++ toolbox originally designed as a simulation tool for armed robots, Drake also provides physics capabilities for aerial robotics.
* **Rotorpy** (https://github.com/spencerfolk/rotorpy): RotorPy, a Python-based multirotor simulation, designed for UAV dynamics research, now prioritizes scalability for deep learning applications with a lightweight engine for easy installatio


## Simulation Packages

Some simulation packages combine physics-based robotics simulators with a rendering engine, often offering modularity and control packages:

* **RotorS** (https://github.com/ethz-asl/rotors_simulator): This package uses Gazebo and includes separate sensor and control modules.
* **Flightmare** (https://github.com/uzh-rpg/flightmare): Flightmare uses Unity for rendering and provides flexibility in the dynamics simulator, allowing the use of Gazebo.
* **Gym-pybullet-drones** (https://github.com/utiasDSL/gym-pybullet-drones): This package uses the PyBullet simulator as a base and includes several quadcopter models and control options.
* **Pegasus Simulator** (https://pegasussimulator.github.io/): The Pegasus simualator is build on top of Isaac Sim to simulate dynamics of multirotor vehicles.

## Flight dynamics models

Some simulators mostly focus on creating accurate dynamics for aerial vehicles. Here are some options:

* JSBSim (https://github.com/JSBSim-Team/jsbsim)
* YASim (https://wiki.flightgear.org/YASim)
* More to be added!

## Available UAV Models

Each simulator typically offers a range of ready-to-use aerial vehicle models:

* **Gazebo**: https://app.gazebosim.org/search;q=uav
* **Isaac Sim**: https://docs.omniverse.nvidia.com/isaacsim/latest/reference_assets.html#aerial-robots
* **Webots**: https://webots.cloud/proto?keyword=robot%2Fflying

## Autopilot Suites

Several autopilot suites provide instructions for using simulators, often with Software-in-the-Loop (SITL) or Hardware-in-the-Loop (HITL) options:

* **Ardupilot**: https://ardupilot.org/copter/docs/common-simulation.html
* **Betaflight**: https://betaflight.com/docs/development/SITL#sitl-in-realflight-9
* **Crazyflie**: https://www.bitcraze.io/documentation/tutorials/getting-started-with-simulation/
* **DJI**: https://www.dji.com/se/simulator
* **Paparazzi UAV**: https://wiki.paparazziuav.org/wiki/Simulation
* **PX4**: https://docs.px4.io/main/en/simulation/#simulation
* **ROSflight**: https://docs.rosflight.org/v1.3/user-guide/gazebo_simulation/
