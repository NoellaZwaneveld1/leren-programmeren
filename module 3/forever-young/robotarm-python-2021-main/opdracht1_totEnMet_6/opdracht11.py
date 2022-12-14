from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3

y = 1

for x in range(0,8):
    robotArm.moveRight()        	
for x in range(9, 0, -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        for z in range(y):
            robotArm.moveRight()
            robotArm.drop() 
            robotArm.moveLeft()
    else:
        robotArm.drop()
    if x != 1:
        robotArm.moveLeft()
robotArm.wait()
