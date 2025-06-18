import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

node = None
path_pub = None
robot_path = Path()

def odom_callback(msg):
    global robot_path, path_pub

    pose_stamped = PoseStamped()
    pose_stamped.header = msg.header
    pose_stamped.pose = msg.pose.pose

    robot_path.header = msg.header
    robot_path.poses.append(pose_stamped)

    path_pub.publish(robot_path)

def main(args=None):
    global node, path_pub

    rclpy.init(args=args)
    node = Node('odom_path_recorder')

    path_pub = node.create_publisher(Path, '/robot_path', 10)
    node.create_subscription(Odometry, '/odom', odom_callback, 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
