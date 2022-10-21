from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 3

y = 9
for x in range(0,5):
    robotArm.grab()
    for z in range(y):
        robotArm.moveRight()
    y-=1
    robotArm.drop()
    for z in range(y):
        robotArm.moveLeft()
    y-=1
robotArm.wait()