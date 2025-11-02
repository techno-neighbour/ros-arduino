from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    main = Node(
        package="py_files",
        executable="mot_sen_pub",
        output='screen',
        prefix='xterm -e'
    )

    motor = Node(
        package="py_files",
        executable="mot_sub",
        output='screen',
        prefix='xterm -e'
    )

    sensor = Node(
        package="py_files",
        executable="sen_sub",
        output='screen',
        prefix='xterm -e'
    )
    ld.add_action(main)
    ld.add_action(motor)
    ld.add_action(sensor)
    return ld