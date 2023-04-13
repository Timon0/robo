from pepper_robots import Robot, PepperConfiguration, PepperNames
import qi

# connect to a virtual robot
port = 49600  # start Choregraphe, go to Edit > Preferences > Virtual Robot to see port number
robot = Robot(PepperConfiguration(PepperNames.Simulation, port=port))

# let the robot talk and move in sequence


# let the robot talk and move in parallel
