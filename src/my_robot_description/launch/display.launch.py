from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_dir = get_package_share_directory('my_robot_description')
    #urdf_file = os.path.join(pkg_dir, 'urdf', 'test.urdf')
    urdf_file = os.path.join(pkg_dir, 'urdf', 'urdf_SLDASM.urdf')

    with open(urdf_file, 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([
        # 发布静态 robot_description 话题
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        # 手动关节控制（带 GUI 滑块）
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        # 打开 RViz2（可选，建议手动运行以便灵活调整）
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(pkg_dir, 'rviz', 'swgo.rviz')]
        )
    ])
   
