def fight(robot_1, robot_2, tactics):
    class My_robot:
        """ represents a robot
        this class is mutable

        attributes:
        name: string
        health: integer
        speed: integer
        tactics: list of strings
        """

        def __init__(self, name = "", health = 0, speed = 0, tactics = []):
            self.name = name
            self.health = health
            self.speed = speed
            self.tactics = tactics

        def __str__(self):
            s = "robot: " + self.name + " with health " + str(self.health) + ", speed " + str(self.speed)
            s += ", and tactics " + str(self.tactics)
            return s

    def fight(first_robot, second_robot):
        while True:
            if len(first_robot.tactics) > 0:
                attack = first_robot.tactics.pop(0)
                second_robot.health -= tactics[attack]
                if second_robot.health <= 0:
                    winner = first_robot.name
                    break
            if len(second_robot.tactics) > 0:
                attack = second_robot.tactics.pop(0)
                first_robot.health -= tactics[attack]
                if first_robot.health <= 0:
                    winner = second_robot.name
                    break
            if len(first_robot.tactics) == 0 and len(second_robot.tactics) == 0:
                if first_robot.health > second_robot.health:
                    winner = first_robot.name
                    break
                elif first_robot.health < second_robot.health:
                    winner = second_robot.name
                    break
                else:
                    winner = "'draw'"
                    break
        return winner


    my_robot_1 = My_robot(robot_1["name"], robot_1["health"], robot_1["speed"], robot_1["tactics"])
    my_robot_2 = My_robot(robot_2["name"], robot_2["health"], robot_2["speed"], robot_2["tactics"])

#     print(my_robot_1)
#     print(my_robot_2)
#     print(tactics)
    if my_robot_1.speed >= my_robot_2.speed:
        winner = fight(my_robot_1, my_robot_2)
    else:
        winner = fight(my_robot_2, my_robot_1)
    # print(winner)
    if winner == "'draw'":
        return "The fight was a draw."
    else:
        return winner + " has won the fight."
