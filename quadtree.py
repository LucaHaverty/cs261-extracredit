from region import Rectangle
from point import Point2D

class Quadtree:
    """Quadtree for partitioning 2D space."""

    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        """Subdivides the current node into four child quadrants."""
        x, y, hw, hh = self.boundary.x, self.boundary.y, self.boundary.hw / 2, self.boundary.hh / 2
        self.northeast = Quadtree(Rectangle(x + hw, y - hh, hw, hh), self.capacity)
        self.northwest = Quadtree(Rectangle(x - hw, y - hh, hw, hh), self.capacity)
        self.southeast = Quadtree(Rectangle(x + hw, y + hh, hw, hh), self.capacity)
        self.southwest = Quadtree(Rectangle(x - hw, y + hh, hw, hh), self.capacity)
        self.divided = True

    def insert(self, point):
        """Inserts a point into the quadtree."""
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.subdivide()

        return (self.northeast.insert(point) or
                self.northwest.insert(point) or
                self.southeast.insert(point) or
                self.southwest.insert(point))

    def query(self, range, found=None):
        """Finds all points in the given range."""
        if found is None:
            found = []

        if not self.boundary.intersects(range):
            return found

        for p in self.points:
            if range.contains(p):
                found.append(p)

        if self.divided:
            self.northwest.query(range, found)
            self.northeast.query(range, found)
            self.southwest.query(range, found)
            self.southeast.query(range, found)

        return found

    def remove(self, point):
        """Removes a point from the quadtree.
        Returns True if the point was found and removed, False otherwise."""
        if not self.boundary.contains(point):
            return False

        # Try to remove from current node's points
        for i, p in enumerate(self.points):
            if p.x == point.x and p.y == point.y:
                self.points.pop(i)
                return True

        # If not found here and we have children, try removing from them
        if self.divided:
            return (self.northeast.remove(point) or
                    self.northwest.remove(point) or
                    self.southeast.remove(point) or
                    self.southwest.remove(point))

        return False