### `construct_map(mappings)` function:

- **Purpose**: Converts the mappings from a dictionary format to a list format.
- **Logic**:
  - Iterates through the `mappings` dictionary.
  - For each `map_name` and `map_data` in `mappings`, it converts the data into a list format where each element represents a mapping with source, range, and destination.
  - Appends these converted mappings into `mappings_list`.

### `process_range_seeds(seed_values, seed_ranges, map_data)` function:

- **Purpose**: Processes seed ranges based on given mappings.
- **Logic**:
  - Initializes lists for new seed values, ranges, and fragments.
  - Iterates while there are seed fragments:
    - Pops seed fragments to process their start, length, and end.
    - Loops through the provided map data and compares seed ranges with map ranges.
    - Depending on the comparison, it extends or appends values to `seed_fragments` and `range_fragments` and updates `new_seeds` and `new_ranges`.

### `find_lowest_location(seeds, mappings)` function:

- **Purpose**: Finds the lowest location number corresponding to initial seed numbers.
- **Logic**:
  - Iterates through seed numbers in pairs.
  - For each seed range, applies the mappings using `process_range_seeds`.
  - Tracks the lowest value encountered among the processed seed ranges.

### `solvePartTwo(input)` function:

- **Purpose**: Solves part two of the problem using provided input.
- **Logic**:
  - Extracts seed ranges and mappings from the input.
  - Converts mappings to a list format using `construct_map`.
  - Uses `find_lowest_location` to find the lowest location number for the given seed ranges and mappings.
