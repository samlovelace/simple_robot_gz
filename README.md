## Dependencies

Ubuntu 22.04, ROS2 Humble, Gazebo 11.10.2 (probably works on other versions of stuff but this is what I am using)

## Workspace Setup

Clone this repo in the src folder of a workspace such that

- robot_ws
  - src
    - simple_robot_gz

## Build

Navigate to the root of the workspace

```bash
$ colcon build
```

## Install

```bash
$ source install/setup.bash
```

## Launch

```bash
$ ros2 launch simple_robot robot_launch.py
```
