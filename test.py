from point import Point2D, Point3D
from region import Rectangle, Cuboid
from quadtree import Quadtree
from octree import Octree

def test_quadtree():
    print("\n----- Testing Quadtree -----\n")
    
    # Initialize quadtree
    boundary = Rectangle(0, 0, 50, 50)
    capacity = 2
    qt = Quadtree(boundary, capacity)
    print(f"✅ Created Quadtree with boundary {boundary} and capacity {capacity}")
    
    # Test initial state
    results = qt.query(Rectangle(0, 0, 100, 100))
    print(f"Initial query results count: {len(results)}")
    print("✅ PASS" if len(results) == 0 else "❌ FAIL: Expected empty results")
    
    # Test insertion
    points = [
        Point2D(10, 10),
        Point2D(20, 20),
        Point2D(25, 25),  # This should cause subdivision
        Point2D(40, 40),
        Point2D(-10, -10),
        Point2D(5, 45)
    ]
    
    print("\nTesting insertion...")
    for p in points:
        qt.insert(p)
        print(f"Inserted point {p}")
    
    # Test query after insertions
    test_cases = [
        {"region": Rectangle(0, 0, 30, 30), "expected": 4},
        {"region": Rectangle(-20, -20, 20, 20), "expected": 1},
        {"region": Rectangle(30, 30, 15, 15), "expected": 3},
        {"region": Rectangle(-50, -50, 100, 100), "expected": 6}
    ]
    
    print("\nTesting queries...")
    for i, test in enumerate(test_cases):
        results = qt.query(test["region"])
        found = len(results)
        expected = test["expected"]
        print(f"Query {i+1}: Region {test['region']}")
        print(f"  Found {found} points, expected {expected}")
        print(f"  {'✅ PASS' if found == expected else '❌ FAIL'}")
    
    # Test removal
    print("\nTesting removal...")
    to_remove = [Point2D(20, 20), Point2D(40, 40)]
    for p in to_remove:
        qt.remove(p)
        print(f"Removed point {p}")
    
    # Test query after removals
    remaining = len(qt.query(Rectangle(-50, -50, 100, 100)))
    expected_remaining = len(points) - len(to_remove)
    print(f"After removal, found {remaining} points, expected {expected_remaining}")
    print(f"{'✅ PASS' if remaining == expected_remaining else '❌ FAIL'}")
    
    # Test removing non-existent point
    print("\nTesting removal of non-existent point...")
    non_existent = Point2D(99, 99)
    before_count = len(qt.query(Rectangle(-100, -100, 200, 200)))
    qt.remove(non_existent)
    after_count = len(qt.query(Rectangle(-100, -100, 200, 200)))
    print(f"Before: {before_count}, After: {after_count}")
    print(f"{'✅ PASS' if before_count == after_count else '❌ FAIL'}")
    

def test_octree():
    print("\n----- Testing Octree -----\n")
    
    # Initialize octree
    boundary = Cuboid(0, 0, 0, 50, 50, 50)
    capacity = 2
    ot = Octree(boundary, capacity)
    print(f"✅ Created Octree with boundary {boundary} and capacity {capacity}")
    
    # Test initial state
    results = ot.query(Cuboid(-100, -100, -100, 200, 200, 200))
    print(f"Initial query results count: {len(results)}")
    print("✅ PASS" if len(results) == 0 else "❌ FAIL: Expected empty results")
    
    # Test insertion
    points = [
        Point3D(10, 10, 10),
        Point3D(20, 20, 20),
        Point3D(25, 25, 25),  # This should cause subdivision
        Point3D(40, 40, 40),
        Point3D(-10, -10, -10),
        Point3D(5, 45, 30)
    ]
    
    print("\nTesting insertion...")
    for p in points:
        ot.insert(p)
        print(f"Inserted point {p}")
    
    # Test query after insertions
    test_cases = [
        {"region": Cuboid(0, 0, 0, 30, 30, 30), "expected": 4},
        {"region": Cuboid(-20, -20, -20, 20, 20, 20), "expected": 1},
        {"region": Cuboid(30, 30, 30, 30, 35, 35), "expected": 5},
        {"region": Cuboid(-50, -50, -50, 100, 100, 100), "expected": 6}
    ]
    
    print("\nTesting queries...")
    for i, test in enumerate(test_cases):
        results = ot.query(test["region"])
        found = len(results)
        expected = test["expected"]
        print(f"Query {i+1}: Region {test['region']}")
        print(f"  Found {found} points, expected {expected}")
        print(f"  {'✅ PASS' if found == expected else '❌ FAIL'}")
    
    # Test removal
    print("\nTesting removal...")
    to_remove = [Point3D(20, 20, 20), Point3D(40, 40, 40)]
    for p in to_remove:
        ot.remove(p)
        print(f"Removed point {p}")
    
    # Test query after removals
    remaining = len(ot.query(Cuboid(-50, -50, -50, 100, 100, 100)))
    expected_remaining = len(points) - len(to_remove)
    print(f"After removal, found {remaining} points, expected {expected_remaining}")
    print(f"{'✅ PASS' if remaining == expected_remaining else '❌ FAIL'}")
    
    # Test removing non-existent point
    print("\nTesting removal of non-existent point...")
    non_existent = Point3D(99, 99, 99)
    before_count = len(ot.query(Cuboid(-100, -100, -100, 200, 200, 200)))
    ot.remove(non_existent)
    after_count = len(ot.query(Cuboid(-100, -100, -100, 200, 200, 200)))
    print(f"Before: {before_count}, After: {after_count}")
    print(f"{'✅ PASS' if before_count == after_count else '❌ FAIL'}")

if __name__ == "__main__":
    print("=== Starting Tests ===")
    test_quadtree()
    test_octree()
    print("\n=== All Tests Completed ===")