from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 3

for x in range(0,8):
    robotArm.moveRight()
    for y in range(0,7):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()

robotArm.wait()