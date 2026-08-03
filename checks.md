# Test Data

## Data Store: Shapes
Types I can spawn:
- Circle
- Square
- Triangle
- Octagon

## Data Store: Shapes List (what's on screen right now)

| Shape ID | Type   | X   | Y   |
|----------|--------|-----|-----|
| 1        | Circle | 100 | 200 |
| 2        | Square | 300 | 150 |

## Test: Spawn a shape on click

**What I did:** Clicked the mouse.

**What should happen:**
- A random shape type gets picked
- It gets a random X and Y
- It shows up on the canvas

# Desk Check

## Run 1 — I click the mouse

| Step | What just happened | Shapes List | On screen |
|------|--------------------|-------------|-----------|
| 1 | Nothing yet | Circle, Square | Circle, Square |
| 2 | Random pick → Triangle | Circle, Square | Circle, Square |
| 3 | Gave it X=250, Y=180 | Circle, Square, Triangle | Circle, Square |
| 4 | Canvas updated | Circle, Square, Triangle | Circle, Square, Triangle |

## Run 2 — I click again

| Step | What just happened | Shapes List | On screen |
|------|--------------------|-------------|-----------|
| 1 | Nothing yet | Circle, Square, Triangle | Circle, Square, Triangle |
| 2 | Random pick → Octagon | Circle, Square, Triangle | Circle, Square, Triangle |
| 3 | Gave it X=400, Y=100 | Circle, Square, Triangle, Octagon | Circle, Square, Triangle |
| 4 | Canvas updated | Circle, Square, Triangle, Octagon | Circle, Square, Triangle, Octagon |
