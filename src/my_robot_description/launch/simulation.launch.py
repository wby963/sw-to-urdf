import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    pkg_share = get_package_share_directory('my_robot_description')  # 包名改成你的
    urdf_path = os.path.join(pkg_share, 'urdf', 'robot.urdf')

    with open(urdf_path, 'r') as file:
        robot_desc = file.read()

    # Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]
        ),
        launch_arguments={'verbose': 'true'}.items()
    )

    # robot_state_publisher
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # spawn（已修正）
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-file', urdf_path,
            '-entity', 'urdf_SLDASM',
            '-x', '0.0', '-y', '0.0', '-z', '0.0',
            '-spawn_service_timeout', '30'
        ],
        output='screen'
    )

    # joint_state_publisher_gui
    joint_state_pub_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        gazebo,
        robot_state_pub,
        spawn_entity,
        joint_state_pub_gui
    ])