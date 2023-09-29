#Daffa Asyqar Ahmad Khalisheka
#1103200034


#Unit 4   Methods 
#Python

# Mengimpor kelas RobotControl dari file robot_control_class
from robot_control_class import RobotControl
# Mengimpor modul time
import time

# Membuat objek RobotControl dengan nama robot "summit"
robotcontrol = RobotControl(robot_name="summit")

# Fungsi untuk menggerakkan robot selama beberapa detik
def move_x_seconds(secs):
    # Memerintahkan robot untuk bergerak lurus
    robotcontrol.move_straight()
    # Menghentikan eksekusi selama beberapa detik sesuai dengan nilai 'secs'
    time.sleep(secs)
    # Menghentikan robot
    robotcontrol.stop_robot()

# Memanggil fungsi 'move_x_seconds' untuk menggerakkan robot selama 5 detik
move_x_seconds(5)

#Command Line Shell
python test_methods1.py
