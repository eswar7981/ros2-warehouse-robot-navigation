from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import (PythonLaunchDescriptionSource,AnyLaunchDescriptionSource)
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_dir = get_package_share_directory('warehouse_robot')
    launch_dir = os.path.join(pkg_dir, 'launch')

    gazebo = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            os.path.join(launch_dir, 'display.launch.xml')
        )
    )

    localization = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            os.path.join(launch_dir, 'localization.launch.xml')
        )
    )

    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'navigation_custom.launch.py')
        )
    )

    return LaunchDescription([
        gazebo,
        localization,
        navigation,
    ])