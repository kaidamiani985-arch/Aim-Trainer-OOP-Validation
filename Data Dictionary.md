# Data Dictionary

| Variable | Data Type | Description |
|----------|-----------|-------------|
| `canvas` | Canvas object | The tkinter canvas |
| `x` | float | X coordinate of shape's position |
| `y` | float | Y coordinate of shape's position |
| `size` | integer | Base size of the shape |
| `reward` | integer | Score multiplier |
| `lifetime` | integer | Time the shape is meant to stay on screen |
| `id` | integer | The canvas item ID of the shape's drawing |
| `spawn_time` | float | `time.time()` when the shape spawned |
| `sides` | integer | Number of sides |
| `proper_size` | float | Half the size to calculate shapes |
| `win` | Tk object | Game window |
| `canvas` | Canvas object | Game canvas, 1000×1000 |
| `shapes` | list | All currently spawned shape objects |
| `score` | integer | Player's score |
| `spawn_speed` | integer | Milliseconds between spawns |
| `menu` | Tk object | The menu window |
