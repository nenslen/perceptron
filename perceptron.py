import numpy as np
import matplotlib.pyplot as plt
import random

class Line:
    # Represents a line as ax + by + c = 0
    def __init__(self, a = 1, b = 1, c = 0):
        self.a = a
        self.b = b
        self.c = c
        
    def value(self, point):
        # Calculates the value of the line at the given point
        return (self.a * point.x) + (self.b * point.y) + self.c


class Colors():
    RED = 1
    BLUE = 2
    NONE = 3
    
    
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    
def plot_line(line):
    # Draws a line and outputs it
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = (-line.c - line.a * x_vals) / line.b
    plt.plot(x_vals, y_vals, '--')

    
class Perceptron:
    def __init__(self, line, red_points, blue_points, epochs, learning_rate):
        self.line = line
        self.red_points = red_points
        self.blue_points = blue_points
        self.epochs = epochs
        self.learning_rate = learning_rate

    def train(self, show_info = False):
        '''
        Calculates the line of best fit for the given points
        '''
        
        for i in range(1, self.epochs):
            point = self.get_random_point()
            
            if point.color == Colors.BLUE and self.point_is_in_area(point, Colors.RED):
                self.line.a -= self.learning_rate * point.x
                self.line.b -= self.learning_rate * point.y
                self.line.c -= self.learning_rate
                
            if point.color == Colors.RED and self.point_is_in_area(point, Colors.BLUE):
                self.line.a += self.learning_rate * point.x
                self.line.b += self.learning_rate * point.y
                self.line.c += self.learning_rate
                
            if i % 10 == 0 and show_info:
                self.show_error()
                
    def get_random_point(self):
        '''
        Selects a random point from the red or blue points and returns it
        '''
        
        color = random.choice([Colors.RED, Colors.BLUE])
        
        if color == Colors.RED:
            point = random.choice(self.red_points)
        
        if color == Colors.BLUE:
            point = random.choice(self.blue_points)
            
        return Point(point[0], point[1], color)
        
    def point_is_in_area(self, point, area):
        '''
        Checks if a given point is in the given area
        '''
        
        ax = self.line.a * point.x
        by = self.line.b * point.y
        c = self.line.c
        point_location = Colors.NONE
        
        # Find out which area the point is in (red or blue)
        if ax + by + c > 0:
            point_location = Colors.RED
        
        if ax + by + c < 0:
            point_location = Colors.BLUE
            
        return point_location == area
    
    def get_points_x(self, color):
        '''
        Returns a list of x coordinates for points of a given color
        '''
        
        if color == Colors.RED:
            return [point[0] for point in self.red_points]
        
        if color == Colors.BLUE:
            return [point[0] for point in self.blue_points]
        
    def get_points_y(self, color):
        '''
        Returns a list of x coordinates for points of a given color
        '''
        
        if color == Colors.RED:
            return [point[1] for point in self.red_points]
        
        if color == Colors.BLUE:
            return [point[1] for point in self.blue_points]
        
    def incorrect_point_count(self):
        incorrect_points = 0
        
        for point in self.red_points:
            if self.point_is_in_area(Point(point[0], point[1], Colors.RED), Colors.BLUE):
                incorrect_points += 1
                
        for point in self.blue_points:
            if self.point_is_in_area(Point(point[0], point[1], Colors.BLUE), Colors.RED):
                incorrect_points += 1
                
        return incorrect_points
        
    def show_error(self):
        '''
        Displays to the user how many points are incorrect
        '''
        
        incorrect = self.incorrect_point_count()
        total = len(self.red_points) + len(self.blue_points)
        
        print('Incorrect points: ' + str(incorrect) + ' of ' + str(total) + ' (' + str(incorrect / total * 100) + '%)')
        
    def draw(self):
        xlim = 8
        ylim = 16
        
        axis = plt.gca()
        axis.set_xlim([-xlim/2, xlim])
        axis.set_ylim([-ylim/2, ylim])
        
        # Show horizontal and vertical lines
        plt.axhline(0, color='r', zorder=-1)
        plt.axvline(0, color='r', zorder=-1)
        
        # Plot points and line
        x_red = self.get_points_x(Colors.RED)
        y_red = self.get_points_y(Colors.RED)
        
        x_blue = self.get_points_x(Colors.BLUE)
        y_blue = self.get_points_y(Colors.BLUE)
        
        plt.scatter(x_red, y_red, color='r', s=9)
        plt.scatter(x_blue, y_blue, color='b', s=9)
        plot_line(self.line)
        
        # Draw
        figure = plt.figure()
        figure.clear()
        figure.canvas.draw()
        

pointCount = 50
line = Line(2, 3, -6) # 2x + 3y - 6 = 0
epochs = 1500
learningRate = 0.01

xRed = np.random.randn(pointCount, 1) + 1
yRed = xRed * 0.2 + np.random.randn(pointCount, 1) * 1.6 + 6
xBlue = np.random.randn(pointCount, 1) + 0.5
yBlue = xBlue * 3.2 + np.random.randn(pointCount, 1) * 1.6

redPoints = list(zip(xRed, yRed))
bluePoints = list(zip(xBlue, yBlue))

perceptron = Perceptron(line, redPoints, bluePoints, epochs, learningRate) 
perceptron.draw()
perceptron.train()
perceptron.draw()
