import os
import xacro
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    ur_desc_path = get_package_share_directory('ur_description')

    env = {
        'GZ_SIM_SYSTEM_PLUGIN_PATH': ':'.join([
            os.environ.get('GZ_SIM_SYSTEM_PLUGIN_PATH', ''),
            os.path.join(get_package_share_directory('ros_gz_sim'), 'lib')
        ]),
        'IGN_GAZEBO_SYSTEM_PLUGIN_PATH': ':'.join([
            os.environ.get('IGN_GAZEBO_SYSTEM_PLUGIN_PATH', ''),
            os.path.join(get_package_share_directory('ros_gz_sim'), 'lib')
        ]),
        'GZ_SIM_RESOURCE_PATH': ':'.join([
            os.environ.get('GZ_SIM_RESOURCE_PATH', ''),
            os.path.dirname(ur_desc_path)
        ])
    }

    robot_desc_pkg_dir = get_package_share_directory('ur_description')
    gazebo_pkg_dir = get_package_share_directory('gazebo')
    
    urdf_xacro_path = os.path.join(robot_desc_pkg_dir, 'urdf', 'ur.urdf.xacro')
    urdf_output_path = os.path.join(robot_desc_pkg_dir, 'urdf', 'generated.urdf')
    
    xacro_args = {
    'name': 'ur',
    'ur_type': 'ur10e', 
    'tf_prefix': '',
    'force_abs_paths': 'true'
    }

    xacro_cmd = [urdf_xacro_path]
    for key, value in xacro_args.items():
        xacro_cmd.extend([f'{key}:={value}'])

    urdf_content = xacro.process_file(
        urdf_xacro_path,
        mappings={
            'name': 'ur',
            'ur_type': 'ur10e',
            'tf_prefix': '',
            'force_abs_paths': 'true'
        }
    ).toxml()
    os.makedirs(os.path.dirname(urdf_output_path), exist_ok=True)
    with open(urdf_output_path, 'w') as urdf_file:
        urdf_file.write(urdf_content)

    world_file_path = os.path.join(gazebo_pkg_dir, 'worlds', 'bin_picking_world.sdf')

    robot_description = {'robot_description': urdf_content}

    robot_state_pub_node = Node(                                                                                
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description],
        # namespace='robot_arm',
        # remappings=[('/tf', '/robot_arm/tf'), ('/tf_static', '/robot_arm/tf_static'),]
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
        # namespace='robot_arm',
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_trajectory_controller", "--controller-manager", "/controller_manager"],
        # namespace='robot_arm',
    )

    gazebo_process = ExecuteProcess(
    cmd=['gz', 'sim', '-r', world_file_path],
    output='screen',
    additional_env=env,
    )

    spawn_robot_arm = ExecuteProcess(
        cmd=['gz', 'service', '-s', '/world/empty/create',
             '--reqtype', 'gz.msgs.EntityFactory',
             '--reptype', 'gz.msgs.Boolean',
             '--timeout', '2000',
             '--req', f'sdf_filename: "{urdf_output_path}", name: "bin_picking_robot", pose: {{position: {{x: 0.84217500000000001, y: -0.50013799999999997, z: 0.6}}}}'],
        output='screen'
    )

    return LaunchDescription([
        gazebo_process,
        TimerAction(
            period=3.0,
            actions=[robot_state_pub_node]
        ),
        TimerAction(
            period=5.0,
            actions=[spawn_robot_arm]
        ),
        # TimerAction(
        #     period=7.0,
        #     actions=[controller_manager_node]
        # ),
        TimerAction(
            period=7.0,
            actions=[joint_state_broadcaster_spawner]
        ),
        TimerAction(
            period=9.0,
            actions=[robot_controller_spawner]
        ),
    ])