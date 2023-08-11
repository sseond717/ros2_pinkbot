import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
import math
class RotateWhenReachMarkerNode(Node):
    def __init__(self, target_x, target_y, marker_size):
        super().__init__('rotate_when_reach_marker')
        self.publisher = self.create_publisher(Twist, '/base_controller/cmd_vel_unstamped', 10)
        self.target_x = target_x
        self.target_y = target_y
        self.marker_size = marker_size
        self.subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)
        self.timer = None
        self.rotate_counter = 0
        self.rotating = False #

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        distance = math.sqrt((x - self.target_x)**2 + (y - self.target_y)**2)
        
        if not self.rotating and distance <= self.marker_size / 2:
            self.rotating = True # 회전 중 플래그 설정
            self.timer = self.create_timer(1.0, self.rotate_for_seconds) # 1초마다 회전
    def rotate_for_seconds(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.linear.y = 0.0
        twist_msg.linear.z = 0.0
        twist_msg.angular.x = 0.0
        twist_msg.angular.y = 0.0
        twist_msg.angular.z = 3.0
        self.publisher.publish(twist_msg)
        self.rotate_counter += 1

        if self.rotate_counter >= 20:
            self.timer.cancel()
            self.timer = None
            self.rotate_counter = 0
            self.destroy_node() # 노드 종료
            rclpy.shutdown() # rclpy 종료

def main(args=None):
    rclpy.init(args=args)
    rotate_when_reach_marker = RotateWhenReachMarkerNode(0.9,-0.55, 0.5) # 마커 위치 및 크기
    rclpy.spin(rotate_when_reach_marker)
    rotate_when_reach_marker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
