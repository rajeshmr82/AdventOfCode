# AdventOfCode

Part 1
Start from S then walk the path based on the kind of pipe to determine which direction to move. Result is the length of the path/2

Part 2

```
function scan_path(steps, step, inpxl, inpxh, inpyl, inpyh):
    inside_cells = empty set

    for y from min_y to max_y:
        winding = 0

        for x from min_x to max_x:
            if (x, y) is on the path and (x, y + 1) is on the path:
                if steps[(x, y + 1)] is (steps[(x, y)] + 1) % step:
                    increment winding
                elif steps[(x, y)] is (steps[(x, y + 1)] + 1) % step:
                    decrement winding

            if (x, y) is not on the path and winding is not 0:
                add (x, y) to inside_cells

    return inside_cells
```

Retrieve Path Information:

    Calls the trace_path(map) function (details assumed to be documented elsewhere) to obtain a dictionary of step locations and the total step count.

Determine Map Boundaries:

    Extracts x and y coordinates from the map keys to establish the minimum and maximum extents of the map.

Identify Inside Cells:

    Iterates through each cell within the map boundaries:
        Applies the Non-Zero Winding Rule:
            Calculates winding for the cell, representing how many times the path winds around it in a counter-clockwise direction.
            Conceptually, imagine a ray starting from the cell and extending infinitely upwards. The winding number counts how many times the path crosses this ray, with clockwise crossings counting as negative and counter-clockwise crossings counting as positive.
        If the cell is not part of the path itself and has a non-zero winding number, it's considered to be enclosed by the path and added to the inside_cells set.

Return Results:

    Returns the set of identified inside cells
