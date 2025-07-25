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
            'no_oops_talker = py_files.no_oops_pub:main',
            'no_oops_listener = py_files.no_oops_sub:main',
            'oops_talker = py_files.oops_pub:main',
            'oops_listener = py_files.oops_sub:main'
        ],
    },
)
