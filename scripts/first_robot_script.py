from nuro_arm import RobotArm

robot = RobotArm()
grasp_jpos = [-1, 0.3, 0.5, 0, 0]
drop_jpos = [-1, 0.256, 0.591, -.01, 0]
screw_jpos = [0.05, .6, 1.135,0.829,0]

robot.open_gripper()
robot.move_arm_jpos(screw_jpos)
for i in range(2):
    robot.close_gripper()
robot.move_arm_jpos(drop_jpos)
robot.open_gripper()


#for i in range(3):
    #robot.open_gripper()
    #robot.close_gripper()

