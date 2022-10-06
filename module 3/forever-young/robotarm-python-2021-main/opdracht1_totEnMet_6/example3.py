from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

for x in range(0,4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

robotArm.wait()