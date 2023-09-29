#Daffa Asyqar Ahmad Khalisheka
#1103200034

#Unit 4 Methods Python 3 For Robotics The Construct Sim

from robot_control_class import RobotControl

# Import class RobotControl dari modul robot_control_class.

robotcontrol = RobotControl(robot_name="summit")

# Membuat objek 'robotcontrol' dengan menggunakan class RobotControl dan menginisialisasi nama robot sebagai "summit".

robotcontrol.turn("counter-clockwise", 0.3, 4)

# Memanggil metode 'turn' pada objek 'robotcontrol'.
# Metode ini memutar robot berlawanan arah jarum jam ("counter-clockwise") dengan kecepatan 0.3 rad/s selama 4 detik.

robotcontrol.move_straight_time("forward", 0.3, 6)

# Memanggil metode 'move_straight_time' pada objek 'robotcontrol'.
# Metode ini menggerakkan robot ke depan ("forward") dengan kecepatan 0.3 m/s selama 6 detik.

robotcontrol.turn("counter-clockwise", 0.3, 4)

# Memanggil metode 'turn' pada objek 'robotcontrol'.
# Metode ini kembali memutar robot berlawanan arah jarum jam ("counter-clockwise") dengan kecepatan 0.3 rad/s selama 4 detik.

robotcontrol.move_straight_time("forward", 0.3, 7)

# Memanggil metode 'move_straight_time' pada objek 'robotcontrol'.
# Metode ini sekali lagi menggerakkan robot ke depan ("forward") dengan kecepatan 0.3 m/s selama 7 detik.

# Kode di atas mengatur sejumlah pergerakan untuk robot "summit", termasuk dua putaran berlawanan arah jarum jam
# dan dua pergerakan maju ke depan dengan kecepatan 0.3 m/s.

#Command Line 
python test_methods4.py
