from region import Cuboid
from point import Point3D

class Octree:
    """Octree for partitioning 3D space."""

    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        """Subdivides the current node into eight child octants."""
        x, y, z = self.boundary.x, self.boundary.y, self.boundary.z
        hw, hh, hd = self.boundary.hw / 2, self.boundary.hh / 2, self.boundary.hd / 2

        def create(dx, dy, dz):
            return Octree(Cuboid(x + dx * hw, y + dy * hh, z + dz * hd, hw, hh, hd), self.capacity)

        self.children = [
            create(1, 1, 1), create(-1, 1, 1),
            create(1, -1, 1), create(-1, -1, 1),
            create(1, 1, -1), create(-1, 1, -1),
            create(1, -1, -1), create(-1, -1, -1)
        ]
        self.divided = True

    def insert(self, point):
        """Inserts a point into the octree."""
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.subdivide()

        for child in self.children:
            if child.insert(point):
                return True

        return False

    def query(self, range, found=None):
        """Finds all points in the given 3D range."""
        if found is None:
            found = []

        if not self.boundary.intersects(range):
            return found

        for p in self.points:
            if range.contains(p):
                found.append(p)

        if self.divided:
            for child in self.children:
                child.query(range, found)

        return found

    def remove(self, point):
        """Removes a point from the octree.
        Returns True if the point was found and removed, False otherwise."""
        if not self.boundary.contains(point):
            return False

        # Try to remove from current node's points
        for i, p in enumerate(self.points):
            if p.x == point.x and p.y == point.y and p.z == point.z:
                self.points.pop(i)
                return True

        # If not found here and we have children, try removing from them
        if self.divided:
            for child in self.children:
                if child.remove(point):
                    return True

        return False