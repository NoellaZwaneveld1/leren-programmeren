from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 3

for x in range(0,6):
    robotArm.moveRight()
    for y in range(0,6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        # robotArm.moveRight()
    robotArm.moveRight()

robotArm.wait()