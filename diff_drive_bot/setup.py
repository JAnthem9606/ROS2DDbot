from setuptools import setup

package_name = 'diff_drive_bot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='craibuntu',
    maintainer_email='bilal.mscss21@iba-suk.edu.pk',
    description='Differential drive robot control nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive_cmd = diff_drive_bot.drive_cmd:main',
            'drive_wheels = diff_drive_bot.drive_wheels:main',
            'twist_to_wheels = diff_drive_bot.twist_to_wheels:main',
            'trajectory_publisher = diff_drive_bot.trajectory_publisher:main',
            'diff_tf = diff_drive_bot.diff_tf:main',
        ],
    },
)
