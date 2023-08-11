import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial # pyserial 라이브러리를 임포트

class CountSubscriber(Node):
    def __init__(self):
        super().__init__('count_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/class_counts',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Pyserial 통신 설정
        self.arduino_port = "/dev/ttyACM0" # 아두이노 포트 설정 (이 값은 시스템에 따라 다를 수 있음)
        self.baudrate = 9600
        self.serial = serial.Serial(self.arduino_port, self.baudrate)
        self.prev_data = -1

    def listener_callback(self, msg):
        self.get_logger().info(f"Received class counts: {msg.data}")

        if msg.data != self.prev_data:
            self.serial.write(b"TOGGLE")  # 아두이노에 TOGGLE 명령 보내기 (문자열은 byte 형태로 변환)
            self.prev_data = msg.data

def main(args=None):
    rclpy.init(args=args)

    count_subscriber = CountSubscriber()

    rclpy.spin(count_subscriber)

    # 메인함수 종료 전에 Serial 연결을 종료하고, 노드 삭제 및 셧다운
    count_subscriber.serial.close()
    count_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()