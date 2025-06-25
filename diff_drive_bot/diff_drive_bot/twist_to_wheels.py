import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from geometry_msgs.msg import Twist

def main():
    rclpy.init()
    node = rclpy.create_node('wheels')

    lwheel_pub = node.create_publisher(Int64, 'lwheel', 10)
    rwheel_pub = node.create_publisher(Int64, 'rwheel', 10)

    lwspeed = 0
    rwspeed = 0

    def cmd_vel_callback(msg: Twist):
        nonlocal lwspeed, rwspeed

        linear_x = int(msg.linear.x * 10)
        angular_z = int(msg.angular.z * 2)

        # Stop condition: reset speeds to zero if no movement commanded
        if linear_x == 0 and angular_z == 0:
            lwspeed = lwspeed
            rwspeed = rwspeed
            
        if linear_x > 0:
            lwspeed += linear_x
            rwspeed += linear_x
            
        if linear_x < 0:
            lwspeed += linear_x
            rwspeed += linear_x

        if angular_z > 0:
            lwspeed += angular_z
            rwspeed -= angular_z

        if angular_z < 0:
            lwspeed += angular_z
            rwspeed -= angular_z

        lwheel_pub.publish(Int64(data=lwspeed))
        rwheel_pub.publish(Int64(data=rwspeed))

    subscription = node.create_subscription(Twist, 'cmd_vel', cmd_vel_callback, 10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
