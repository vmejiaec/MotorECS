class Velocity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Velocity(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Velocity):
            return Velocity(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Velocity):
            return Velocity(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    # Multiply velocity by a scalar
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Velocity(self.x * scalar, self.y * scalar)
        return NotImplemented