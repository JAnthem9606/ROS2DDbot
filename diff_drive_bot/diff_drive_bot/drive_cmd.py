import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import readchar

def main():
    rclpy.init()
    node = rclpy.create_node('teleop_cmd')

    publisher = node.create_publisher(Twist, 'cmd_vel', 10)

    print("Teleop started. Use keys:")
    print("  w: forward")
    print("  x: backward")
    print("  a: turn left")
    print("  d: turn right")
    print("  s: stop")
    print("Press Ctrl+C to quit.\n")

    try:
        while rclpy.ok():
            key = readchar.readkey()
            twist = Twist()

            if key == 'w':
                twist.linear.x = 1.0
            if key == 'x':
                twist.linear.x = -1.0
            if key == 'a':
                twist.angular.z = -1.0
            if key == 'd':
                twist.angular.z = 1.0
            if key == 's':
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            publisher.publish(twist)

    except KeyboardInterrupt:
        print("\nShutting down teleop_cmd node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
