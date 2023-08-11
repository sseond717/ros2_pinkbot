import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
 
class MarkerPublisherNode(Node):
    def __init__(self):
        super().__init__('marker_publisher')
        self.publisher_a = self.create_publisher(Marker, '/a_region_marker', 10)
        self.publisher_b = self.create_publisher(Marker, '/a_region_marker', 10)
        self.timer = self.create_timer(1.0, self.publish_marker)
 
    def publish_marker(self):
        marker_a = Marker()
        marker_a.header.frame_id = "map"
        marker_a.ns = "a_region"
        marker_a.id = 0
        marker_a.type = Marker.CUBE
        marker_a.action = Marker.ADD
        marker_a.pose.position.x = 0.9
        marker_a.pose.position.y = -0.55
        marker_a.pose.position.z = 0.0
        marker_a.pose.orientation.x = 0.0
        marker_a.pose.orientation.y = 0.0
        marker_a.pose.orientation.z = 0.0
        marker_a.pose.orientation.w = 1.0
        marker_a.scale.x = 0.5
        marker_a.scale.y = 0.5
        marker_a.scale.z = 0.1
        marker_a.color.r = 1.0
        marker_a.color.g = 0.0
        marker_a.color.b = 0.0
        marker_a.color.a = 0.5
        self.publisher_a.publish(marker_a)


        marker_b = Marker()
        marker_b.header.frame_id = "map"
        marker_b.ns = "b_region"
        marker_b.id = 1
        marker_b.type = Marker.CUBE
        marker_b.action = Marker.ADD
        marker_b.pose.position.x = 0.65
        marker_b.pose.position.y = 1.3
        marker_b.pose.position.z = 0.0
        marker_b.pose.orientation.x = 0.0
        marker_b.pose.orientation.y = 0.0
        marker_b.pose.orientation.z = 0.0
        marker_b.pose.orientation.w = 1.0
        marker_b.scale.x = 0.5
        marker_b.scale.y = 0.5
        marker_b.scale.z = 0.1
        marker_b.color.r = 0.0
        marker_b.color.g = 0.0
        marker_b.color.b = 1.0
        marker_b.color.a = 0.5
        self.publisher_b.publish(marker_b)

def main(args=None):
    rclpy.init(args=args)
    marker_publisher = MarkerPublisherNode()
    rclpy.spin(marker_publisher)
 
    marker_publisher.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
