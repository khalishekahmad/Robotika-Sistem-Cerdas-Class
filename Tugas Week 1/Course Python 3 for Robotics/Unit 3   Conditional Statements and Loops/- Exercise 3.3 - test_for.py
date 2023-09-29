# Impor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat objek RobotControl yang akan mengendalikan robot
robotcontrol = RobotControl()

# Mengambil daftar nilai dari sensor laser secara lengkap
l = robotcontrol.get_laser_full()

# Inisialisasi variabel maksimum dengan nilai awal 0
maxim = 0

# Melakukan perulangan untuk mencari nilai maksimum dalam daftar
for value in l:
    # Memeriksa apakah nilai saat ini lebih besar dari nilai maksimum yang telah ditemukan sejauh ini
    if value > maxim:
        # Jika iya, perbarui nilai maksimum
        maxim = value

# Mencetak nilai tertinggi yang ditemukan dalam daftar
print("Nilai tertinggi dalam daftar adalah: ", maxim)

#Command Line Shell
 python test_for.py

