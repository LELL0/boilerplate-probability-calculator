import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.contents = []

        for k, v in colors.items():
            for x in range(v):
                self.contents.append(k)

    def draw(self, numOfBalls):
        balls = []

        if numOfBalls > len(self.contents):
            balls = self.contents
            self.contents = []

        else:
            for _ in range(numOfBalls):
                balls.append(self.contents.pop(
                    random.randint(0, len(self.contents) - 1)))

        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    result = 0

    for _ in range(num_experiments):

        hat_copy = copy.deepcopy(hat)
        drawnBalls = hat_copy.draw(num_balls_drawn)
        check = True

        for i, j in expected_balls.items():
            if drawnBalls.count(i) < j:
                check = False

        if check:
            result += 1

    return result / num_experiments
