# Spatial Trees in Python: Quadtree & Octree

Contact havertyl@oregonstate.edu with questions

This project implements two spatial partitioning data structures in Python for a CS162 extra credit assignment:

- 🟩 **Quadtree**: For organizing 2D spatial data.
- 🧊 **Octree**: For organizing 3D spatial data.

These trees are useful for fast spatial queries, collision detection, image representation, LOD (level of detail) management, and more.

---

## ▶️ Setup and running

1. Clone the repository with the terminal command `git clone https://github.com/lucahaverty/cs261-extracredit` or downloading as a zip

2. If python is not already installed, [install it](https://www.python.org/downloads/). You can check for a valid python installation by running `python --version` (should be 3.5 or later)

3. From the root project directory, run the terminal command `python test.py` to run unit tests. Results will be printed to the terminal.

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
cs261-extracredit/
├── quadtree.py # Quadtree implementation (2D)
├── octree.py # Octree implementation (3D)
├── test.py # Unit tests for Quadtree and Octree
└── README.md
```

---

## 🔧 Usage

### Quadtree (2D)

```python
from quadtree import Quadtree

# Create a quadtree with a boundary region and capacity per node
qt = Quadtree((0, 0, 100, 100), capacity=4)

# Insert points
qt.insert((10, -20))
qt.insert((-30, 40))

# Query for points within a region
found = qt.query((0, 0, 50, 50))
print("Found points:", found)

# Get the number of points found in the quadtree
len(qt)

```

### Octree (3D)
```python
from octree import Octree

# Create an octree with a 3D boundary
ot = Octree((0, 0, 0, 100, 100, 100), capacity=4)

# Insert points
ot.insert((10, -20, 5))
ot.insert((-30, 40, 10))

# Query in 3D space
found = ot.query((0, 0, 0, 50, 50, 50))
print("Found points:", found)

# Get the number of points found in the octree
len(qt)

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
