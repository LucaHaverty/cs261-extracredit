from quadtree import Quadtree
from octree import Octree

def test_quadtree():
    print("\n----- Testing Quadtree -----\n")
    
    # boundary tuple: (center_x, center_y, half_width, half_height)
    boundary = (0, 0, 50, 50)
    capacity = 2
    qt = Quadtree(boundary, capacity)
    print(f"✅ Created Quadtree with boundary {boundary} and capacity {capacity}")
    
    # Query using rectangle tuple: (center_x, center_y, half_width, half_height)
    results = qt.query((0, 0, 100, 100))
    print(f"Initial query results count: {len(results)}")
    print("✅ PASS" if len(results) == 0 else "❌ FAIL: Expected empty results")
    
    points = [
        (10, 10),
        (20, 20),
        (25, 25),
        (40, 40),
        (-10, -10),
        (5, 45)
    ]
    
    print("\nTesting insertion...")
    for p in points:
        qt.insert(p)
        print(f"Inserted point {p}")
    
    # Test cases with rectangle tuples: (center_x, center_y, half_width, half_height)
    test_cases = [
        {"region": (0, 0, 30, 30), "expected": 4},      # Rectangle from (-30,-30) to (30,30)
        {"region": (-20, -20, 20, 20), "expected": 1},  # Rectangle from (-40,-40) to (0,0)
        {"region": (30, 30, 15, 15), "expected": 3},    # Rectangle from (15,15) to (45,45)
        {"region": (-50, -50, 100, 100), "expected": 6} # Rectangle from (-150,-150) to (50,50)
    ]
    
    print("\nTesting queries...")
    for i, test in enumerate(test_cases):
        results = qt.query(test["region"])
        found = len(results)
        expected = test["expected"]
        region_desc = f"center({test['region'][0]},{test['region'][1]}) half-size({test['region'][2]},{test['region'][3]})"
        print(f"Query {i+1}: Region {region_desc}")
        print(f"  Found {found} points, expected {expected}")
        print(f"  Points found: {results}")
        print(f"  {'✅ PASS' if found == expected else '❌ FAIL'}")
    
    print("\nTesting removal...")
    to_remove = [(20, 20), (40, 40)]
    for p in to_remove:
        removed = qt.remove(p)
        print(f"Removed point {p}: {'Success' if removed else 'Failed'}")
    
    remaining = len(qt.query((-50, -50, 100, 100)))
    expected_remaining = len(points) - len(to_remove)
    print(f"After removal, found {remaining} points, expected {expected_remaining}")
    print(f"{'✅ PASS' if remaining == expected_remaining else '❌ FAIL'}")
    
    print("\nTesting removal of non-existent point...")
    non_existent = (99, 99)
    before_count = len(qt.query((-100, -100, 200, 200)))
    removed = qt.remove(non_existent)
    after_count = len(qt.query((-100, -100, 200, 200)))
    print(f"Before: {before_count}, After: {after_count}, Removal result: {removed}")
    print(f"{'✅ PASS' if before_count == after_count and not removed else '❌ FAIL'}")

def test_octree():
    print("\n----- Testing Octree -----\n")
    
    # boundary tuple: (center_x, center_y, center_z, half_width, half_height, half_depth)
    boundary = (0, 0, 0, 50, 50, 50)
    capacity = 2
    ot = Octree(boundary, capacity)
    print(f"✅ Created Octree with boundary {boundary} and capacity {capacity}")
    
    # Query using cuboid tuple: (center_x, center_y, center_z, half_width, half_height, half_depth)
    results = ot.query((-100, -100, -100, 200, 200, 200))
    print(f"Initial query results count: {len(results)}")
    print("✅ PASS" if len(results) == 0 else "❌ FAIL: Expected empty results")
    
    points = [
        (10, 10, 10),
        (20, 20, 20),
        (25, 25, 25),
        (40, 40, 40),
        (-10, -10, -10),
        (5, 45, 30)
    ]
    
    print("\nTesting insertion...")
    for p in points:
        ot.insert(p)
        print(f"Inserted point {p}")
    
    # Test cases with cuboid tuples: (center_x, center_y, center_z, half_width, half_height, half_depth)
    test_cases = [
        {"region": (0, 0, 0, 30, 30, 30), "expected": 4},         # Cuboid from (-30,-30,-30) to (30,30,30)
        {"region": (-20, -20, -20, 20, 20, 20), "expected": 1},   # Cuboid from (-40,-40,-40) to (0,0,0)
        {"region": (30, 30, 30, 30, 35, 35), "expected": 5},     # Cuboid from (0,-5,-5) to (60,65,65)
        {"region": (-50, -50, -50, 100, 100, 100), "expected": 6} # Cuboid from (-150,-150,-150) to (50,50,50)
    ]
    
    print("\nTesting queries...")
    for i, test in enumerate(test_cases):
        results = ot.query(test["region"])
        found = len(results)
        expected = test["expected"]
        region_desc = f"center({test['region'][0]},{test['region'][1]},{test['region'][2]}) half-size({test['region'][3]},{test['region'][4]},{test['region'][5]})"
        print(f"Query {i+1}: Region {region_desc}")
        print(f"  Found {found} points, expected {expected}")
        print(f"  Points found: {results}")
        print(f"  {'✅ PASS' if found == expected else '❌ FAIL'}")
    
    print("\nTesting removal...")
    to_remove = [(20, 20, 20), (40, 40, 40)]
    for p in to_remove:
        removed = ot.remove(p)
        print(f"Removed point {p}: {'Success' if removed else 'Failed'}")
    
    remaining = len(ot.query((-50, -50, -50, 100, 100, 100)))
    expected_remaining = len(points) - len(to_remove)
    print(f"After removal, found {remaining} points, expected {expected_remaining}")
    print(f"{'✅ PASS' if remaining == expected_remaining else '❌ FAIL'}")
    
    print("\nTesting removal of non-existent point...")
    non_existent = (99, 99, 99)
    before_count = len(ot.query((-100, -100, -100, 200, 200, 200)))
    removed = ot.remove(non_existent)
    after_count = len(ot.query((-100, -100, -100, 200, 200, 200)))
    print(f"Before: {before_count}, After: {after_count}, Removal result: {removed}")
    print(f"{'✅ PASS' if before_count == after_count and not removed else '❌ FAIL'}")

if __name__ == "__main__":
    print("=== Starting Tests ===")
    test_quadtree()
    test_octree()
    print("\n=== All Tests Completed ===")