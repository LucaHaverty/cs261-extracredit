# Spatial Trees in Python: Quadtree & Octree

Contact havertyl@oregonstate.edu with questions

This project implements two spatial partitioning data structures in Python for a CS162 extra credit assignment:

- 🟩 **Quadtree**: For organizing 2D spatial data.
- 🧊 **Octree**: For organizing 3D spatial data.

These trees are useful for fast spatial queries, collision detection, image representation, LOD (level of detail) management, and more.

---

## 📦 Features

- Efficient insertion and querying of spatial points
- Dynamic subdivision (regions split when they exceed capacity)
- Point removal support
- Boundary checking and flexible querying regions
- Expandable root region (for inserting points outside initial bounds)
- Object-oriented Python code

---

## 🗂️ Structure

```
spatial_trees/
├── quadtree.py # Quadtree implementation (2D)
├── octree.py # Octree implementation (3D)
├── point.py # Point classes for 2D and 3D
├── region.py # Region and boundary classes
├── examples/
│ ├── quadtree_demo.py
│ └── octree_demo.py
└── README.md
```

---

## ▶️ Setup and running

1. Clone the repository with the terminal command `git clone https://github.com/lucahaverty/cs261-extracredit` or downloading as a zip

2. If python is not already installed, [install it](https://www.python.org/downloads/). You can check for a valid python installation by running `python --version` (should be 3.5 or later)

3. From the root project directory, run the terminal command `python test.py` to run unit tests. Results will be printed to the terminal.

---

## 🔧 Usage

### Quadtree (2D)

```python
from quadtree import Quadtree
from region import Rectangle
from point import Point2D

# Create a quadtree with a boundary region and capacity per node
qt = Quadtree(Rectangle(0, 0, 100, 100), capacity=4)

# Insert points
qt.insert(Point2D(10, -20))
qt.insert(Point2D(-30, 40))

# Query for points within a region
found = qt.query(Rectangle(0, 0, 50, 50))
print("Found points:", found)
```

### Octree (3D)
```python
from octree import Octree
from region import Cuboid
from point import Point3D

# Create an octree with a 3D boundary
ot = Octree(Cuboid(0, 0, 0, 100, 100, 100), capacity=4)

# Insert points
ot.insert(Point3D(10, -20, 5))
ot.insert(Point3D(-30, 40, 10))

# Query in 3D space
found = ot.query(Cuboid(0, 0, 0, 50, 50, 50))
print("Found points:", found)
```

## 📚 Concepts

Quadtree: Divides 2D space into four quadrants recursively.

Octree: Divides 3D space into eight octants recursively.

Capacity: Each node holds up to N points before subdividing.

Boundary Regions:

Rectangle: For 2D quadtree bounds.

Cuboid: For 3D octree bounds.

## 📈 Applications

Collision detection in simulations and games

View frustum culling (3D graphics)

Image compression and subdivision

Geographic Information Systems (GIS)

Point cloud visualization and querying

Simulating and/or visualizing the folding of biological proteins

---

<div align="center">Contact havertyl@oregonstate.edu with questions</div>