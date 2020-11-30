import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        

        output = []
        for i in range(num - 1, -1, -1):
            random_num = random.randint(0, len(self.contents) - 1)
            self.contents[random_num], self.contents[-1] = self.contents[-1], self.contents[random_num]
            output.append(self.contents.pop())
        return output




def experiment(hat = None, 
    expected_balls = None, 
    num_balls_drawn = None, 
    num_experiments = None):
    num_success = 0
    for num in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        
        copy_expected_balls = copy.deepcopy(expected_balls)
        for ball in balls_drawn:
            if ball in copy_expected_balls:
                copy_expected_balls[ball] -= 1

        state = True 
        for value in copy_expected_balls.values():
            if value <= 0:
                state = state and True
            else:
                state = False
        if state:
            num_success += 1

    return num_success / num_experiments

