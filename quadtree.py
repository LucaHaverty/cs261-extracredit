class Quadtree:
    """Quadtree for partitioning 2D space using tuples for rectangle representation."""

    def __init__(self, boundary, capacity=4):
        # boundary = (center_x, center_y, half_width, half_height)
        self.boundary = boundary
      
        self.capacity = capacity
        self.points = []  # List of (x, y) point tuples
        self.divided = False
        # Child quadrants will be stored as: northeast, northwest, southeast, southwest

    def __len__(self):
        return len(self.points)

    def __str__(self):
        return f"Quadtree: (Capacity: {self.capacity}, Num points: {len(self)})"

    def _rectangle_contains(self, rect, point):
        """Returns True if the (x, y) point tuple lies within the rectangle tuple."""
        # rect = (center_x, center_y, half_width, half_height)
        # point = (x, y)
        return (rect[0] - rect[2] <= point[0] <= rect[0] + rect[2] and
                rect[1] - rect[3] <= point[1] <= rect[1] + rect[3])

    def _rectangles_intersect(self, rect1, rect2):
        """Returns True if rect1 intersects rect2. Both are rectangle tuples."""
        # rect1 = (center_x, center_y, half_width, half_height)
        # rect2 = (center_x, center_y, half_width, half_height)
        return not (rect2[0] - rect2[2] > rect1[0] + rect1[2] or
                    rect2[0] + rect2[2] < rect1[0] - rect1[2] or
                    rect2[1] - rect2[3] > rect1[1] + rect1[3] or
                    rect2[1] + rect2[3] < rect1[1] - rect1[3])

    def subdivide(self):
        """Subdivides the current node into four child quadrants."""
        # Extract boundary components: (center_x, center_y, half_width, half_height)
        x, y, hw, hh = self.boundary[0], self.boundary[1], self.boundary[2] / 2, self.boundary[3] / 2
        
        # Create child quadrants as tuples: (center_x, center_y, half_width, half_height)
        self.northeast = Quadtree((x + hw, y - hh, hw, hh), self.capacity)
        self.northwest = Quadtree((x - hw, y - hh, hw, hh), self.capacity)
        self.southeast = Quadtree((x + hw, y + hh, hw, hh), self.capacity)
        self.southwest = Quadtree((x - hw, y + hh, hw, hh), self.capacity)
        self.divided = True

    def insert(self, point):
        """Inserts a (x, y) point tuple into the quadtree."""
        if not self._rectangle_contains(self.boundary, point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)  # point is (x, y) tuple
            return True

        if not self.divided:
            self.subdivide()

        return (self.northeast.insert(point) or
                self.northwest.insert(point) or
                self.southeast.insert(point) or
                self.southwest.insert(point))

    def query(self, range_rect, found=None):
        """Finds all points in the given range rectangle tuple."""
        if found is None:
            found = []

        # range_rect is a rectangle tuple: (center_x, center_y, half_width, half_height)
        if not self._rectangles_intersect(self.boundary, range_rect):
            return found

        # Check each point tuple (x, y) in this node
        for p in self.points:
            if self._rectangle_contains(range_rect, p):
                found.append(p)

        if self.divided:
            self.northwest.query(range_rect, found)
            self.northeast.query(range_rect, found)
            self.southwest.query(range_rect, found)
            self.southeast.query(range_rect, found)

        return found

    def remove(self, point):
        """Removes a point tuple (x, y) from the quadtree."""
        if not self._rectangle_contains(self.boundary, point):
            return False

        # Search through points list for matching (x, y) tuple
        for i, p in enumerate(self.points):
            if p[0] == point[0] and p[1] == point[1]:  # Compare x and y coordinates
                self.points.pop(i)
                return True

        if self.divided:
            return (self.northeast.remove(point) or
                    self.northwest.remove(point) or
                    self.southeast.remove(point) or
                    self.southwest.remove(point))

        return False
