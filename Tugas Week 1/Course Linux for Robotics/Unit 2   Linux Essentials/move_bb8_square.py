#Daffa Asyqar Ahmad Khalisheka
#1103200034


#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
import math

class MoveBB8():
    
    def __init__(self):
        # Inisialisasi publisher untuk mengirim perintah ke BB-8
        self.bb8_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)
        self.rate = rospy.Rate(10)
    
    def publish_once_in_cmd_vel(self):
        """
        Ini karena terkadang pengiriman ke topic gagal saat pertama kali.
        Pada sistem pengiriman yang berkelanjutan, hal ini tidak menjadi masalah,
        tetapi pada sistem yang hanya mengirim sekali, ini sangat penting.
        """
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                rospy.loginfo("Perintah Dikirim")
                break
            else:
                self.rate.sleep()
        
    def shutdownhook(self):
        # Lebih baik daripada menggunakan rospy.is_shut_down()
        self.stop_bb8()
        self.ctrl_c = True

    def stop_bb8(self):
        rospy.loginfo("Waktu shutdown! Menghentikan robot")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_x_time(self, moving_time, linear_speed=0.2, angular_speed=0.2):
        
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed
        
        self.publish_once_in_cmd_vel()
        time.sleep(moving_time)
    
    def move_square(self):
        
        i = 0
        
        while not self.ctrl_c and i < 4:
            # Bergerak ke Depan
            self.move_x_time(moving_time=4.0, linear_speed=0.2, angular_speed=0.0)
            # Belok, belok tidak dipengaruhi oleh panjang sisi yang diinginkan
            self.move_x_time(moving_time=4.0, linear_speed=0.0, angular_speed=0.2)
            i += 1
            
        self.stop_bb8()
        rospy.loginfo("######## Selesai Bergerak dalam Bentuk Persegi")
            
if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8()
    try:
        movebb8_object.move_square()
    except rospy.ROSInterruptException:
        pass
