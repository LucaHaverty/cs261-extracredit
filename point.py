class Point2D:
    """Represents a point in 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Point2D: ({self.x}, {self.y})"

class Point3D:
    """Represents a point in 3D space."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point3D: ({self.x}, {self.y}, {self.z})"