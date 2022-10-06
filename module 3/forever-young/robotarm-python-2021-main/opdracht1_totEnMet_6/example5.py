from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

for x in range(1, 8):
    robotArm.moveRight()

for x in range(1, 9):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if x < 8:
        for y in range(0, 2):
            robotArm.moveLeft()
    else:
        robotArm.moveLeft()
robotArm.wait()
