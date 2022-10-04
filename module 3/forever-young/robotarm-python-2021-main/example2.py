from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

robotArm.grab()

for x in range(1,10):
    robotArm.moveRight()

robotArm.drop()

for x in range (9, 7, -1):
    robotArm.moveLeft()

robotArm.grab()

for x in range (7, 9):
    robotArm.moveRight()

robotArm.drop()

for x in range(9, 4, -1):
    robotArm.moveLeft()

robotArm.grab()

for x in range(4, 9):
    robotArm.moveRight()

robotArm.drop()
robotArm.wait()

robotArm.reportFlaws = True