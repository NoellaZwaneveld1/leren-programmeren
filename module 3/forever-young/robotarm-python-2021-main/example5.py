from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

for x in range(1, 8):
    robotArm.moveRight()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(8, 6, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(7, 5, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(6, 4, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(5, 3, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(4, 2, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(3, 1, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for x in range(2, 0, -1):
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.wait()
