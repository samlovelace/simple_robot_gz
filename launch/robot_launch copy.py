from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():

    pkg_path = get_package_share_directory('simple_robot')
    return LaunchDescription([
        # Launch Gazebo with empty world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Launch Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
        ),

        # Spawn Robot Model
        ExecuteProcess(
            cmd=['ros2', 'run', 'gazebo_ros', 'spawn_entity.py',
                 '-entity', 'simple_robot',
                 '-file', os.path.join(pkg_path, 'models', 'simple_robot', 'model.sdf')],
            output='screen'
        ),

        # ROS 2 Bridge for IMU and GPS
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'sensor_timeout': 0.1,
                'publish_tf': True,
                'odom_frame': 'odom',
                'base_link_frame': 'base_link',
                'world_frame': 'odom',
                'imu0': '/robot/imu',
                'gps0': '/robot/gps'
            }]
        )
    ])

