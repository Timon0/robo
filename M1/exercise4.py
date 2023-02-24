default_speed = 300
default_turn_speed = 50
turn_multiplier = 1
direction = 0

def set_speed(speed_left, speed_right):
    global motor_left_target, motor_right_target, direction
    motor_left_target = direction * speed_left
    motor_right_target = direction * speed_right

@onevent
def rc5():
    global default_speed, default_turn_speed, direction, turn_multiplier
    if rc5_command == 80 and direction != 0:
        direction = 1
        set_speed(default_speed, default_speed)
    if rc5_command == 81 and direction != 0:
        direction = -1
        set_speed(default_speed, default_speed)
    if rc5_command == 85:
        set_speed(default_speed - default_turn_speed * turn_multiplier, default_speed + default_turn_speed * turn_multiplier)
    if rc5_command == 86:
        set_speed(default_speed + default_turn_speed * turn_multiplier, default_speed - default_turn_speed * turn_multiplier)
    if rc5_command == 87:
        direction = 0
        set_speed(0,0)
    if rc5_command == 53:
        direction = 1
    if rc5_command <= 9 and rc5_command != 0:
        turn_multiplier = rc5_command