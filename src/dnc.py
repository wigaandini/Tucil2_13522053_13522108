import matplotlib.pyplot as plt

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

def t_point(p1, p2, t):
    return Position(p1.x + (p2.x - p1.x) * t, p1.y + (p2.y - p1.y) * t)

# Define two points
p1 = Position(1, 1)
p2 = Position(5, 4)

# Generate intermediate points
intermediate_points = t_point(p1, p2, 0.7)

# Extract x and y coordinates
x_values = [p1.x, p2.x, intermediate_points.x]
y_values = [p1.y, p2.y, intermediate_points.y]

# Plot the points
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.title('Interpolated Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
