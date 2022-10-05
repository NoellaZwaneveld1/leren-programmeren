from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

robotArm.grab()

for x in range(1,10): #9 keer naar rechts
    robotArm.moveRight()

robotArm.drop()

for x in range (9, 7, -1):
    robotArm.moveLeft() #2 keer naar links

robotArm.grab()

for x in range (7, 9):
    robotArm.moveRight() #2 keer naar rechts

robotArm.drop()

for x in range(9, 4, -1):
    robotArm.moveLeft() #5 keer links

robotArm.grab()

for x in range(4, 9):
    robotArm.moveRight() #5 keer rechts

robotArm.drop()
robotArm.wait()

robotArm.reportFlaws = True