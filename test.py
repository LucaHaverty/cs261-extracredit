from point import Point2D, Point3D
from region import Rectangle, Cuboid
from quadtree import Quadtree
from octree import Octree

def test_quadtree():
    print("Testing Quadtree...")
    qt = Quadtree(Rectangle(0, 0, 50, 50), 2)
    qt.insert(Point2D(10, 10))
    qt.insert(Point2D(-20, -20))
    qt.insert(Point2D(25, 25))  
    qt.insert(Point2D(20, 20))
    qt.insert(Point2D(40, -40))

    results = qt.query(Rectangle(0, 0, 30, 30))
    assert len(results) == 4
    print("✅ Quadtree test passed.")


def test_octree():
    print("Testing Octree...")
    ot = Octree(Cuboid(0, 0, 0, 50, 50, 50), 2)
    ot.insert(Point3D(10, 10, 10))
    ot.insert(Point3D(-20, -20, -20))
    ot.insert(Point3D(25, 25, 25))  # causes subdivision

    results = ot.query(Cuboid(0, 0, 0, 20, 20, 20))
    assert len(results) == 2
    print("✅ Octree test passed.")


test_quadtree()
test_octree()
