import random
import math
import utils

class Environment:
    def __init__(self):
        self.dt = 0.1
        self.lengths = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        self.n_joints = 7
        self.accel_limit = 10.0 # radian


    def start(self):
        self.joints = []
        sum_alpha = 0.0
        prev_position = {'x': 0.0, 'y': 0.0}
        for i in range(self.n_joints):
            joint = {}
            alpha = random() * 2 * math.pi
            sum_alpha = sum_alpha + alpha
            cur_position = {'x': prev_position['x'] + self.lengths[i] * math.cos(sum_alpha), 'y': prev_position['y'] + self.lengths[i] * math.sin(sum_alpha)}
            self.joints.append({'position': cur_position, 'theta': alpha, 'omega': 0.0})
            prev_position = cur_position

    def update(self):


    def doAction(self, actions):
        """
        actions : action is a list of gaussian distribution form
        each element of actions represents angular acceleration of the corresponding joint 
        for preventing large angular acceleration, limit its absolute value to accel_limit
        """
        for i in range(self.n_joints):
            mu = actions[i]['mean']
            sigma = actions[i]['var']
            


