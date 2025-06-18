import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64  # Change here
import readchar

rclpy.init()
node = rclpy.create_node('wheels')

lwheel_pub = node.create_publisher(Int64, 'lwheel', 10)
rwheel_pub = node.create_publisher(Int64, 'rwheel', 10)

lwspeed = 0
rwspeed = 0
speed = 2

try:
    while rclpy.ok():
        key = readchar.readkey()

        if key == "w":
            lwspeed += speed
            rwspeed += speed

        elif key == "x":
            lwspeed -= speed
            rwspeed -= speed

        elif key == "a":
            lwspeed -= speed
            rwspeed += speed

        elif key == "d":
            lwspeed += speed
            rwspeed -= speed

        # No need to clamp here since Int64 supports a much larger range

        lwheel_pub.publish(Int64(data=lwspeed))
        rwheel_pub.publish(Int64(data=rwspeed))

except KeyboardInterrupt:
    pass

finally:
    node.destroy_node()
    rclpy.shutdown()

