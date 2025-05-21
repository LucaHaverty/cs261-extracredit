from point import Point2D, Point3D

class Rectangle:
    """Axis-aligned rectangle defined by center (x, y) and half-width/height."""

    def __init__(self, x, y, hw, hh):
        self.x = x
        self.y = y
        self.hw = hw
        self.hh = hh

    def __str__(self):
        return f"Rectangle: (x: {self.x}, y: {self.y}, hw: {self.hw}, hh: {self.hh})"

    def contains(self, point):
        """Returns True if the point lies within the rectangle."""
        return (self.x - self.hw <= point.x <= self.x + self.hw and
                self.y - self.hh <= point.y <= self.y + self.hh)

    def intersects(self, range):
        """Returns True if this rectangle intersects another rectangle."""
        return not (range.x - range.hw > self.x + self.hw or
                    range.x + range.hw < self.x - self.hw or
                    range.y - range.hh > self.y + self.hh or
                    range.y + range.hh < self.y - self.hh)


class Cuboid:
    """Axis-aligned cuboid defined by center (x, y, z) and half-width/height/depth."""

    def __init__(self, x, y, z, hw, hh, hd):
        self.x = x
        self.y = y
        self.z = z
        self.hw = hw
        self.hh = hh
        self.hd = hd

    def __str__(self):
        return f"Cuboid: (x: {self.x}, y: {self.y}, z: {self.z}, hw: {self.hw}, hh: {self.hh}, hd: {self.hd})"
    
    def contains(self, point):
        """Returns True if the point lies within the cuboid."""
        return (self.x - self.hw <= point.x <= self.x + self.hw and
                self.y - self.hh <= point.y <= self.y + self.hh and
                self.z - self.hd <= point.z <= self.z + self.hd)

    def intersects(self, range):
        """Returns True if this cuboid intersects another cuboid."""
        return not (range.x - range.hw > self.x + self.hw or
                    range.x + range.hw < self.x - self.hw or
                    range.y - range.hh > self.y + self.hh or
                    range.y + range.hh < self.y - self.hh or
                    range.z - range.hd > self.z + self.hd or
                    range.z + range.hd < self.z - self.hd)
