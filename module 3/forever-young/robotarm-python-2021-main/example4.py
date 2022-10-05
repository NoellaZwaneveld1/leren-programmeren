from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.grab()

for x in range(1, 3):
    robotArm.moveRight()

robotArm.drop()

for x in range(3, 1, -1):
    robotArm.moveLeft()

robotArm.grab()

for x in range(1, 3):
    robotArm.moveRight()

robotArm.drop()

for x in range(3, 1, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

robotArm.wait()