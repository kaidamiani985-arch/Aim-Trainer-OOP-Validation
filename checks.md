# Test Data

## Data Store: Shapes
| Shape Types: 
- Circle
- Square
- Triangle
- Octagon

## Data Store: Shapes List (active shapes on screen)
| Shape ID | Type     | X   | Y   |
|----------|----------|-----|-----|
| 1        | Circle   | 100 | 200 |
| 2        | Square   | 300 | 150 |


### Test to Spawn a Triangle
- **Input:** User clicks mouse
- Choose random shape
- Choose random X and Y
- **Expected result:** A Triangle appears on the canvas at a random spot

# Desk Check

## Walkthrough

**User clicks mouse.**

### Step 1 — Spawn Shape runs
- Looks at the **Shapes** data store
- Available types: Circle, Square, Triangle, Octagon
- Randomly picks

### Step 2 — Create the shape
- A new Triangle object is created
- It gets a random X and Y position

### Step 3 — Store in Shapes List
- The new Triangle is added to the **Shapes List** data store

| Shape ID | Type     | X   | Y   |
|----------|----------|-----|-----|
| 1        | Circle   | 100 | 200 |
| 2        | Square   | 300 | 150 |
| 3        | Triangle | 250 | 180 |

### Step 4 — Send to Canvas
- Spawn Shape reads the **Shapes List**
- Sends all active shapes to the **Canvas Display**
- Canvas draws them all on screen

### Result
User sees the existing Circle and Square, plus the new Triangle.

---

## Second Run — Spawn an Octagon

**User clicks again.**

| Step | What Happens |
|------|--------------|
| 1 | Spawn Shape picks **Octagon** from Shapes list |
| 2 | Creates Octagon at X = 400, Y = 100 |
| 3 | Adds it to Shapes List (now 4 shapes) |
| 4 | Sends all 4 shapes to Canvas |

**Result:** Circle, Square, Triangle, and Octagon all on screen.

# Desk Check

**Test:** User clicks mouse to spawn a shape.

| Step | Action | Shapes (available) | Shapes List (on screen) | Canvas shows |
|------|--------|---------------------|--------------------------|--------------|
| 1 | Start | Circle, Square, Triangle, Octagon | Circle, Square | Circle, Square |
| 2 | Spawn Shape picks random type → Triangle | Circle, Square, Triangle, Octagon | Circle, Square | Circle, Square |
| 3 | Create Triangle object at random X,Y | Circle, Square, Triangle, Octagon | Circle, Square, Triangle | Circle, Square |
| 4 | Send Shapes List to Canvas | Circle, Square, Triangle, Octagon | Circle, Square, Triangle | Circle, Square, Triangle |

---

**Test:** User clicks again.

| Step | Action | Shapes (available) | Shapes List (on screen) | Canvas shows |
|------|--------|---------------------|--------------------------|--------------|
| 1 | Start | Circle, Square, Triangle, Octagon | Circle, Square, Triangle | Circle, Square, Triangle |
| 2 | Spawn Shape picks → Octagon | Circle, Square, Triangle, Octagon | Circle, Square, Triangle | Circle, Square, Triangle |
| 3 | Create Octagon at random X,Y | Circle, Square, Triangle, Octagon | Circle, Square, Triangle, Octagon | Circle, Square, Triangle |
| 4 | Send to Canvas | Circle, Square, Triangle, Octagon | Circle, Square, Triangle, Octagon | Circle, Square, Triangle, Octagon |
