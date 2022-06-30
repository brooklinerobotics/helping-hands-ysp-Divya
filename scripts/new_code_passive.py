import time

import numpy
from nuro_arm import RobotArm
robot = RobotArm()
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

robot.passive_mode()
servo_values = np.array([])


for i in range(10):
    achieved_jpos = robot.get_arm_jpos()
    servo_values.tolist()
    np.append(servo_values, achieved_jpos[0])
    time.sleep(1.0)

print(servo_values)

fig, ax = plt.subplots()
ax.plot(servo_values);
plt.show()


