#Daffa Asyqar Ahmad Khalisheka
#1103200034


# Impor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat objek RobotControl yang akan mengendalikan robot
robotcontrol = RobotControl()

# Mengambil nilai dari sensor laser pada sudut 360 derajat
a = robotcontrol.get_laser(360)

# Selama nilai laser lebih besar dari 1, lanjutkan pergerakan robot
while a > 1:
    # Menggerakkan robot maju
    robotcontrol.move_straight()
    
    # Mendapatkan nilai laser kembali untuk pembaruan selanjutnya
    a = robotcontrol.get_laser(360)
    
    # Mencetak jarak saat ini ke dinding
    print("Jarak saat ini ke dinding: %f" % a)

# Setelah loop selesai, menghentikan robot
robotcontrol.stop_robot()

# Mencetak pesan bahwa robot telah berhenti karena dinding terdeteksi
print("Dinding berada pada jarak %f meter! Hentikan robot!" % a)

#Command Line 
python test_while.py
