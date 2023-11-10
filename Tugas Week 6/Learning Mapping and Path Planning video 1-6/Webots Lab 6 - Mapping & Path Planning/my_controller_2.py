from controller import Robot, DistanceSensor, Motor

# Create the robot instance
robot = Robot()

# Get the devices
ds_left = robot.getDevice("ps7")  # Left proximity sensor
ds_right = robot.getDevice("ps0")  # Right proximity sensor
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Enable devices
ds_left.enable(10)
ds_right.enable(10)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.5)
right_motor.setVelocity(0.5)

# Initialize variables for wall mapping
map_size = 10
cell_size = 0.1
robot_position = [0, 0]
robot_orientation = 0
wall_map = [[0] * map_size for _ in range(map_size)]

def update_map():
    global robot_position, robot_orientation, wall_map

    # Update map based on sensor readings
    left_distance = ds_left.getValue()
    right_distance = ds_right.getValue()

    # Update robot position and orientation
    robot_position[0] += cell_size * (left_distance + right_distance) / 2 * cos(robot_orientation)
    robot_position[1] += cell_size * (left_distance + right_distance) / 2 * sin(robot_orientation)

    # Update wall map
    x = int(robot_position[0] / cell_size)
    y = int(robot_position[1] / cell_size)
    wall_map[x][y] = 1

# Main control loop
while robot.step(64) != -1:
    update_map()

# Print the final wall map
for row in wall_map:
    print(row)
