from controller import Robot

# Inisialisasi robot
robot = Robot()

# Inisialisasi motor
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set kecepatan maksimum
max_velocity = 6.28  # Angka ini sesuaikan dengan kecepatan maksimum yang diizinkan

# Set kecepatan
velocity = 2.0  # Ganti dengan kecepatan yang diinginkan
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(velocity)
right_motor.setVelocity(velocity)

# Simulasi berjalan dalam lingkaran dengan radius R1
R1 = 10  # Ganti dengan radius lingkaran yang diinginkan
while robot.step(32) != -1:
    left_wheel_distance = left_motor.getPosition()
    right_wheel_distance = right_motor.getPosition()

    # Hitung sudut yang sudah ditempuh oleh roda kiri dan kanan
    left_wheel_angle = left_wheel_distance / R1
    right_wheel_angle = right_wheel_distance / R1

    # Hitung sudut putaran robot
    theta = (right_wheel_angle - left_wheel_angle) * R1

    # Hitung jarak yang sudah ditempuh oleh robot
    arc_length = R1 * theta

    # Cek jika robot telah menyelesaikan satu putaran (360 derajat)
    if abs(arc_length) >= (2 * 3.1415 * R1):
        break

# Menghentikan robot
left_motor.setVelocity(0)
right_motor.setVelocity(0)

# Simulasi selesai
