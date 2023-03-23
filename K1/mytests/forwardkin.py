import numpy as np
from math import pi, cos, sin

measurements = {
    'j0z': 3,
    'j1z': 71,
    'j2z': 126,
    'j3z': 124,
    'j4z': 197
}

def forward_kinematic_braccio(joints):
    ''' param: joints: current position of all the joints of the braccio '''
    ''' return: current position'''
    x = 0
    y = 0
    z = 0

    x = (measurements['j1z'] * cos(joints[1]) * cos(joints[0]) + measurements['j2z'] * cos(joints[1] + joints[2]) * cos(joints[0]) + 
         measurements['j3z'] * cos(joints[1] + joints[2] + joints[3]) * cos(joints[0]))
    y = (measurements['j1z'] * cos(joints[1])  * cos(joints[0]) + measurements['j2z'] * cos(joints[1] + joints[2])  * cos(joints[0]) + 
         measurements['j3z'] * cos(joints[1] + joints[2] + joints[3])  * cos(joints[0]))
    z = (measurements['j1z'] * sin(joints[1]) + measurements['j2z'] * sin(joints[1] + joints[2]) + 
        measurements['j3z'] * sin(joints[1] + joints[2] + joints[3]) + measurements['j0z'])

    return [x, y, z]