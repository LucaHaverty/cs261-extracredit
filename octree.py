class Octree:
    """Octree for partitioning 3D space using tuples for cuboid representation."""

    def __init__(self, boundary, capacity=4):
        # boundary = (center_x, center_y, center_z, half_width, half_height, half_depth)
        self.boundary = boundary  
       
        self.capacity = capacity
        self.points = []  # List of (x, y, z) point tuples
        self.divided = False
        # Child octants will be stored in self.children list (8 octants)

    def __len__(self):
        return len(self.points)

    def __str__(self):
        return f"Octree: (Capacity: {self.capacity}, Num points: {len(self)})"
    
    def _cuboid_contains(self, cuboid, point):
        """Returns True if the (x, y, z) point tuple lies within the cuboid tuple."""
        # cuboid = (center_x, center_y, center_z, half_width, half_height, half_depth)
        # point = (x, y, z)
        return (cuboid[0] - cuboid[3] <= point[0] <= cuboid[0] + cuboid[3] and
                cuboid[1] - cuboid[4] <= point[1] <= cuboid[1] + cuboid[4] and
                cuboid[2] - cuboid[5] <= point[2] <= cuboid[2] + cuboid[5])

    def _cuboids_intersect(self, cuboid1, cuboid2):
        """Returns True if cuboid1 intersects cuboid2. Both are cuboid tuples."""
        # cuboid1 = (center_x, center_y, center_z, half_width, half_height, half_depth)
        # cuboid2 = (center_x, center_y, center_z, half_width, half_height, half_depth)
        return not (cuboid2[0] - cuboid2[3] > cuboid1[0] + cuboid1[3] or
                    cuboid2[0] + cuboid2[3] < cuboid1[0] - cuboid1[3] or
                    cuboid2[1] - cuboid2[4] > cuboid1[1] + cuboid1[4] or
                    cuboid2[1] + cuboid2[4] < cuboid1[1] - cuboid1[4] or
                    cuboid2[2] - cuboid2[5] > cuboid1[2] + cuboid1[5] or
                    cuboid2[2] + cuboid2[5] < cuboid1[2] - cuboid1[5])

    def subdivide(self):
        """Subdivides the current node into eight child octants."""
        # Extract boundary components: (center_x, center_y, center_z, half_width, half_height, half_depth)
        x, y, z = self.boundary[0], self.boundary[1], self.boundary[2]
        hw, hh, hd = self.boundary[3] / 2, self.boundary[4] / 2, self.boundary[5] / 2

        def create_child(dx, dy, dz):
            """Helper function to create child octant at relative position (dx, dy, dz)"""
            return Octree((x + dx * hw, y + dy * hh, z + dz * hd, hw, hh, hd), self.capacity)

        # Create 8 child octants:  (±1, ±1, ±1) combinations
        # Order: front-top-right, front-top-left, front-bottom-right, front-bottom-left,
        #        back-top-right, back-top-left, back-bottom-right, back-bottom-left
        self.children = [
            create_child(1, 1, 1),   create_child(-1, 1, 1),
            create_child(1, -1, 1),  create_child(-1, -1, 1),
            create_child(1, 1, -1),  create_child(-1, 1, -1),
            create_child(1, -1, -1), create_child(-1, -1, -1)
        ]
        self.divided = True

    def insert(self, point):
        """Inserts a (x, y, z) point tuple into the octree."""
        if not self._cuboid_contains(self.boundary, point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)  # point is (x, y, z) tuple
            return True

        if not self.divided:
            self.subdivide()

        # Try to insert into one of the child octants
        for child in self.children:
            if child.insert(point):
                return True

        return False

    def query(self, range_cuboid, found=None):
        """Finds all points in the given range cuboid tuple."""
        if found is None:
            found = []

        # range_cuboid is a cuboid tuple: (center_x, center_y, center_z, half_width, half_height, half_depth)
        if not self._cuboids_intersect(self.boundary, range_cuboid):
            return found

        # Check each point tuple (x, y, z) in this node
        for p in self.points:
            if self._cuboid_contains(range_cuboid, p):
                found.append(p)

        if self.divided:
            for child in self.children:
                child.query(range_cuboid, found)

        return found

    def remove(self, point):
        """Removes a point tuple (x, y, z) from the octree."""
        if not self._cuboid_contains(self.boundary, point):
            return False

        # Search through points list for matching (x, y, z) tuple
        for i, p in enumerate(self.points):
            if p[0] == point[0] and p[1] == point[1] and p[2] == point[2]:  # Compare x, y, z coordinates
                self.points.pop(i)
                return True

        if self.divided:
            for child in self.children:
                if child.remove(point):
                    return True

        return False