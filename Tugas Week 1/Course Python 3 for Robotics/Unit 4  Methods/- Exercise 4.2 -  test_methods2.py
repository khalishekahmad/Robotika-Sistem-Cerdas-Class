from robot_control_class import RobotControl

# Import class RobotControl dari modul robot_control_class.

robotcontrol = RobotControl(robot_name="summit")

# Membuat objek 'robotcontrol' dengan menggunakan class RobotControl dan menginisialisasi nama robot sebagai "summit".

def get_laser_values(a, b, c):
    # Membuat fungsi 'get_laser_values' yang menerima tiga parameter: a, b, dan c.

    r1 = robotcontrol.get_laser_summit(a)
    # Mengambil bacaan laser dari robot 'summit' pada posisi 'a' dan menyimpannya dalam variabel 'r1'.

    r2 = robotcontrol.get_laser_summit(b)
    # Mengambil bacaan laser dari robot 'summit' pada posisi 'b' dan menyimpannya dalam variabel 'r2'.

    r3 = robotcontrol.get_laser_summit(c)
    # Mengambil bacaan laser dari robot 'summit' pada posisi 'c' dan menyimpannya dalam variabel 'r3'.

    return [r1, r2, r3]
    # Mengembalikan daftar yang berisi tiga nilai bacaan laser.

l = get_laser_values(0, 500, 1000)
# Memanggil fungsi 'get_laser_values' dengan tiga argumen: 0, 500, dan 1000, lalu menyimpan hasilnya dalam variabel 'l'.

print("Reading 1: ", l[0])
# Mencetak nilai bacaan laser pertama (indeks 0) ke layar.

print("Reading 2: ", l[1])
# Mencetak nilai bacaan laser kedua (indeks 1) ke layar.

print("Reading 3: ", l[2])
# Mencetak nilai bacaan laser ketiga (indeks 2) ke layar.

# Kode di atas digunakan untuk mengambil bacaan laser dari robot 'summit' pada tiga posisi yang berbeda (a, b, dan c)
# dan mencetak nilai-nilainya ke layar.

#Command Line
python test_methods2.py
