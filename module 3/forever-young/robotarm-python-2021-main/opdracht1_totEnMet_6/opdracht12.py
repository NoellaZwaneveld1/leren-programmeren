from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 3

y = 9
     
for x in range(0, 9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for z in range(y):
            robotArm.moveRight()
        robotArm.drop() 
        for z in range(y):
            robotArm.moveLeft()
    else:
        robotArm.drop()

    if x != 9:
        robotArm.moveRight()
        y-=1
robotArm.wait()