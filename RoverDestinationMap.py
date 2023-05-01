import random
import time

class Map:
    def __init__(self, size):
        self.size = size
        self.map = [[' ' for i in range(self.size)] for j in range(self.size)]
        self.rover_position = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.target_position = None
        self.path = []
        self.map[self.rover_position[0]][self.rover_position[1]] = '+'

    def set_target(self, target_x, target_y):
        self.target_position = (target_x, target_y)
        self.map[self.target_position[0]][self.target_position[1]] = 'T'

    def calculate_speed(self):
        dx = self.target_position[0] - self.rover_position[0]
        dy = self.target_position[1] - self.rover_position[1]
        if dx != 0:
            x_speed = int(dx / abs(dx))
        else:
            x_speed = 0
        if dy != 0:
            y_speed = int(dy / abs(dy))
        else:
            y_speed = 0
        return x_speed, y_speed

    def move(self, x_speed, y_speed):
        self.map[self.rover_position[0]][self.rover_position[1]] = '*'
        self.rover_position = (self.rover_position[0] + x_speed, self.rover_position[1] + y_speed)
        self.map[self.rover_position[0]][self.rover_position[1]] = '+'
        self.path.append(self.rover_position)

    def display_map(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size-1 or j == 0 or j == self.size-1:
                    print('#', end=' ')
                else:
                    print(self.map[i][j], end=' ')
            print()
        print()

    def start(self):
        x_speed, y_speed = self.calculate_speed()
        while self.rover_position != self.target_position:
            self.display_map()
            time.sleep(0.03)
            self.move(x_speed, y_speed)

map = Map(50)
map.set_target(int(input("Enter target x: ")), int(input("Enter target y: ")))
map.start()
