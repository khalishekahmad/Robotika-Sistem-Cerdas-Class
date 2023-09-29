#Daffa Asyqar Ahmad Khalisheka
#1103200034

#Unit 5 Classes and Object Oriented Programming Python 3 for Robotics The Construct Sim

from robot_control_class import RobotControl

# Import class RobotControl dari modul robot_control_class.

class MoveRobot:
    def __init__(self, motion, clockwise, speed, time):
        # Membuat class MoveRobot dengan constructor (__init__) yang menerima beberapa parameter.
        
        self.robotcontrol = RobotControl(robot_name="summit")
        # Membuat objek 'robotcontrol' dengan menggunakan class RobotControl dan menginisialisasi nama robot sebagai "summit".
        
        self.motion = motion
        # Menyimpan jenis gerakan robot (misalnya, 'forward' untuk maju atau 'backward' untuk mundur).
        
        self.clockwise = clockwise
        # Menyimpan arah putaran robot (misalnya, 'clockwise' untuk searah jarum jam atau 'counter-clockwise' untuk berlawanan arah jarum jam).
        
        self.speed = speed
        # Menyimpan kecepatan gerakan robot.
        
        self.time = time
        # Menyimpan durasi waktu untuk menjalankan gerakan robot.
        
        self.time_turn = 7.0 # Ini adalah perkiraan waktu di mana robot akan berputar 90 derajat.

    def do_square(self):
        # Membuat metode 'do_square' untuk menjalankan robot dalam pola persegi.

        i = 0

        while (i < 4):
            self.move_straight()
            # Memanggil metode 'move_straight' untuk menggerakkan robot maju.
            
            self.turn()
            # Memanggil metode 'turn' untuk memutar robot.
            
            i += 1

    def move_straight(self):
        # Membuat metode 'move_straight' untuk menggerakkan robot maju dengan kecepatan dan waktu yang telah ditentukan.
        
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):
        # Membuat metode 'turn' untuk memutar robot dengan arah dan waktu yang telah ditentukan.
        
        self.robotcontrol.turn(self.clockwise, self.speed, self.time_turn)

mr1 = MoveRobot('forward', 'clockwise', 0.3, 4)
# Membuat objek 'mr1' dengan parameter gerakan maju ("forward"), arah putaran searah jarum jam ("clockwise"), kecepatan 0.3, dan waktu 4 detik.
mr1.do_square()
# Memanggil metode 'do_square' pada objek 'mr1' untuk menjalankan robot dalam pola persegi.

mr2 = MoveRobot('forward', 'clockwise', 0.3, 8)
# Membuat objek 'mr2' dengan parameter gerakan maju ("forward"), arah putaran searah jarum jam ("clockwise"), kecepatan 0.3, dan waktu 8 detik.
mr2.do_square()
# Memanggil metode 'do_square' pada objek 'mr2' untuk menjalankan robot dalam pola persegi yang lebih besar.

# Kode di atas mengorganisasi pergerakan robot dalam pola persegi dengan menggunakan objek 'MoveRobot' yang dapat diatur
# dengan parameter-parameter yang berbeda.

#Command Line Shell
python test_class.py
