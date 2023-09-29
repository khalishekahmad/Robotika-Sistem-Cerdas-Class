#Daffa Asyqar Ahmad Khalisheka
#1103200034

#Project: Help the TurtleBot Robot get out of the maze (by using Python)

import time 
from robot_control_class import RobotControl

# Inisialisasi objek RobotControl
robotcontrol = RobotControl()

# Daffa Asyqar Ahmad Khalisheka
# 1103200034
# Mata Kuliah Robotika dan Sistem Cerdas

class Robo:

    def __init__(self):
        # Inisialisasi
        print("INISIALISASI")
        self.laser1 = robotcontrol.get_laser(360)
        self.robotmove_speed = 5
        self.robotmove_time = 1
        self.robotturn_clokwise = "clockwise"
        self.robotturn_speed = 0.8
        self.robotturn_time = 1

    def robotmove(self):
        # Robot bergerak maju selama jarak laser > 1
        while self.laser1 > 1:
            robotcontrol.move_straight()
            self.laser1 = robotcontrol.get_laser(360)
            print("JARAK: ", self.laser1)
        
        # Berhenti jika terlalu dekat dengan dinding
        robotcontrol.stop_robot()
        print("TERLALU DEKAT DENGAN DINDING!")

    def robotturn(self):
        # Mendapatkan jarak laser di sebelah kanan dan kiri
        distance_kanan = robotcontrol.get_laser(360)
        distance_kiri = robotcontrol.get_laser(180)
        print("KANAN", distance_kanan, "KIRI", distance_kiri)
        if distance_kanan > distance_kiri:
            # Putar robot searah jarum jam jika jarak kanan > jarak kiri
            while self.laser1 < 1:
                robotcontrol.turn(self.robotturn_clokwise,
                                  self.robotturn_speed, self.robotturn_time)
                self.laser1 = robotcontrol.get_laser(360)
                print("kanan: jarak: ", self.laser1)
        else:
            # Putar robot berlawanan arah jarum jam jika jarak kiri > jarak kanan
            while self.laser1 < 1:
                robotcontrol.turn(
                    "aclokwise", self.robotturn_speed, self.robotturn_time)
                self.laser1 = robotcontrol.get_laser(360)
                print("kiri: jarak: ", self.laser1)

        # Berhenti setelah selesai berputar
        robotcontrol.stop_robot()
        print("FINISH")

if __name__ == '__main__':
    # Membuat objek Robo
    robo = Robo()

    while not robotcontrol.ctrl_c:
        # Memanggil metode robotmove dan robotturn secara berulang
        robo.robotmove()
        robo.robotturn()

#Command File Shell
python mazerobotdaffasyqar.py
