# Impor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat objek RobotControl yang akan mengendalikan robot
robotcontrol = RobotControl()

# Mengambil nilai dari sensor laser pada sudut 360 derajat
a = robotcontrol.get_laser(360)

# Memeriksa apakah nilai laser kurang dari 1
if a < 1:
    # Jika iya, menghentikan robot
    robotcontrol.stop_robot()
else:
    # Jika tidak, menggerakkan robot maju
    robotcontrol.move_straight()

# Mencetak nilai laser yang diterima
print("Nilai laser yang diterima adalah: ", a)

#Command Line
python test_if.py

