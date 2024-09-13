import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    nav_dir = get_package_share_directory('orne_box_navigation_executor')
    config_dir = os.path.join(nav_dir, 'config')
    default=os.path.join(
            config_dir,
            'maps',
            '3F-map.pcd')
    
    return LaunchDescription([
        Node(
            package='pcl_ros',
            executable='pcd_to_pointcloud',
            name='pcd_to_pointcloud',
            output='screen',
            parameters=[
                {'file_name': '/home/kyo/orne_ws/src/orne-box/orne_box_navigation_executor/config/maps/3F_map.pcd'}  # PCDファイルのパスを指定
            ],
            remappings=[
                ('/cloud_pcd', '/map')
            ]
        ),
    ])
