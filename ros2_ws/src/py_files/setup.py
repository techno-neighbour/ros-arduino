from setuptools import find_packages, setup

package_name = 'py_files'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tn',
    maintainer_email='geniusmf8@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'no_oops_talker = py_files.normal.no_oops_pub:main',
            'no_oops_listener = py_files.normal.no_oops_sub:main',
            'oops_talker = py_files.normal.oops_pub:main',
            'oops_listener = py_files.normal.oops_sub:main',

            'led_switch = py_files.pyserial.simple.led_control:main',
            'button_state = py_files.pyserial.simple.button_state:main',
            'dist_pub = py_files.pyserial.simple.dist_pub:main',
            'dist_sub = py_files.pyserial.simple.dist_sub:main',
            'motor_pub = py_files.pyserial.simple.motor_dir_pub:main',
            'motor_sub = py_files.pyserial.simple.motor_dir_sub:main',
            
            'mot_sen_pub = py_files.pyserial.car.mot_sen_pub:main',
            'mot_sub = py_files.pyserial.car.mot_sub:main',
            'sen_sub = py_files.pyserial.car.sen_sub:main',
        ],
    },
)
