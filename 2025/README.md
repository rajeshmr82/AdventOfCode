[![AoC](https://badgen.net/badge/AoC/2025/blue)](https://adventofcode.com/2025)
![Language](https://badgen.net/badge/Language/Python/blue)
[![Days Completed](https://badgen.net/badge/Days%20Completed/9/green)]()
[![Stars](https://badgen.net/badge/Stars/18%E2%98%85/yellow)]()

# 🎄 Advent of Code 2025 🎄

## Solutions

<!--SOLUTIONS-->
[![Day](https://badgen.net/badge/01/%E2%98%85%E2%98%85/green)](day_01)
[![Day](https://badgen.net/badge/02/%E2%98%85%E2%98%85/green)](day_02)
[![Day](https://badgen.net/badge/03/%E2%98%85%E2%98%85/green)](day_03)
[![Day](https://badgen.net/badge/04/%E2%98%85%E2%98%85/green)](day_04)
[![Day](https://badgen.net/badge/05/%E2%98%85%E2%98%85/green)](day_05)
[![Day](https://badgen.net/badge/06/%E2%98%85%E2%98%85/green)](day_06)
[![Day](https://badgen.net/badge/07/%E2%98%85%E2%98%85/green)](day_07)
[![Day](https://badgen.net/badge/08/%E2%98%85%E2%98%85/green)](day_08)
[![Day](https://badgen.net/badge/09/%E2%98%85%E2%98%85/green)](day_09)
[![Day](https://badgen.net/badge/10/%E2%98%86%E2%98%86/grey)](day_10)
[![Day](https://badgen.net/badge/11/%E2%98%86%E2%98%86/grey)](day_11)
[![Day](https://badgen.net/badge/12/%E2%98%86%E2%98%86/grey)](day_12)
<!--/SOLUTIONS-->

_Click a badge to go to the specific day._

---

## Results

<!--RESULTS-->

| Day | Part 1 | Part 2 | Notes |
|-----|--------|--------|-------|
| [01](day_01) | ⭐ | ⭐ | Distance calculation and similarity score |
| [02](day_02) | ⭐ | ⭐ | Invalid ID detection with pattern repetition |
| [03](day_03) | ⭐ | ⭐ | Battery joltage optimization with greedy selection |
| [04](day_04) | ⭐ | ⭐ | Forklift accessibility with cascading removal simulation |
| [05](day_05) | ⭐ | ⭐ | Ingredient database with range-based parsing |
| [06](day_06) | ⭐ | ⭐ | Arithmetic worksheet parser with spatial number representation |
| [07](day_07) | ⭐ | ⭐ | Tachyon beam splitting with unique splitter counting and quantum timeline paths |
| [08](day_08) | ⭐ | ⭐ | Junction box circuit connection with MST and Union-Find |
| [09](day_09) | ⭐ | ⭐ | Maximum rectangle from red tiles in rectilinear polygon |
| 10 | | | |
| 11 | | | |
| 12 | | | |

<!--/RESULTS-->

---

## Repository Structure

```
AdventOfCode/
├── README.md
├── 2025/
│   ├── day_01/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_1.py
│   ├── day_02/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_2.py
│   ├── day_03/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_3.py
│   ├── day_04/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_4.py
│   ├── day_05/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_5.py
│   ├── day_06/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_6.py
│   ├── day_07/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_7.py
│   ├── day_08/
│   │   ├── puzzle.py
│   │   ├── input.txt
│   │   ├── README.md
│   │   └── test_puzzle_day_8.py
│   └── ...
├── 2024/
│   └── ...
└── utils/
    └── helpers.py
```

---

## Progress Statistics

- **Total Stars**: 18 ⭐
- **Completion Rate**: 75% (9/12 days)
- **Current Streak**: 9 days 🔥
- **Last Updated**: January 4, 2026

> **Note**: Advent of Code 2025 features 12 days instead of the traditional 25 days.

---

## Highlights & Learnings

### Day 1: Historian Hysteria
- Learned about calculating distances between sorted lists
- Implemented similarity scoring with frequency counting
- **Key Insight**: Using `Counter` for efficient frequency lookups

### Day 2: Invalid IDs
- Explored pattern detection in numeric sequences
- Implemented mathematical formulas using geometric series
- **Key Insight**: Using multipliers `(10^(n×k) - 1) / (10^k - 1)` for pattern repetition
- **Challenge**: Deduplication when numbers match multiple patterns

### Day 3: Battery Joltage
- Optimized battery selection for maximum joltage output
- Implemented greedy algorithms for digit selection
- **Key Insight**: Part 1 uses brute force (O(n²)), Part 2 uses greedy left-to-right construction
- **Part 1**: Pick 2 batteries to maximize 2-digit number
- **Part 2**: Pick 12 batteries to maximize 12-digit number with "leave enough digits" constraint
- **Challenge**: Understanding that the second digit must appear after the first in sequence

### Day 4: Forklift Accessibility
- Explored grid navigation and neighbor counting patterns
- Implemented cascading removal simulation with optimization
- **Key Insight**: Track only affected cells instead of rechecking entire grid
- **Part 1**: Count rolls with < 4 neighbors (perimeter identification)
- **Part 2**: Iterative erosion - clusters shrink from outside → inside like peeling an onion
- **Challenge**: Optimizing the simulation to avoid O(k×n²×m²) complexity by tracking affected neighbors
- **Technique**: Early exit when counting neighbors (stop at 4), set operations for efficient neighbor tracking

### Day 5: Ingredient Database
- Built a memory-efficient parser for large-scale ingredient databases
- Implemented range-based storage instead of expanding billions of IDs
- **Key Insight**: Store ranges, not individual IDs - handles `1-1000000000` in 16 bytes vs 28GB!
- **Part 1**: Check which ingredients are fresh by testing membership in ranges
- **Part 2**: Count total unique fresh IDs by merging overlapping ranges first
- **Challenge**: Overlapping ranges cause double-counting - merge `10-14` and `12-18` → `10-18`
- **Technique**: Range merging algorithm sorts and combines adjacent/overlapping ranges
- **Performance**: 175 ranges with 1000 checks in ~3ms; handles billions of IDs efficiently
- **Design**: Pythonic API with properties (`db.fresh_available`), magic methods (`len(db)`), and clean function names (`parse()`)
- **Mathematics**: After merging, `total = Σ (end - start + 1)` for each non-overlapping range

### Day 6: Arithmetic Worksheet Parser
- Parsed unusual worksheet formats with spatial number representation
- Implemented two different reading methods: horizontal (standard) and vertical (Cephalopod)
- **Key Insight**: Spatial information is critical - can't convert Part 1 results to Part 2 because position data is lost
- **Part 1**: Read horizontally across rows using regex - `123 * 45 * 6 = 33,210`
- **Part 2**: Read vertically within columns, right-to-left - same input gives `356 * 24 * 1 = 8,544`
- **Challenge**: Part 2 requires character-level grid processing to preserve exact spatial positions
- **Technique**: Single-pass right-to-left scan with all-space column detection for problem boundaries
- **Algorithm**: `ljust()` padding + `range(max_length-1, -1, -1)` iteration + digit filtering per column
- **Design Decision**: Two separate parsers - Part 1 uses regex (simple), Part 2 uses character grid (spatial)
- **Edge Cases**: Varying number widths, multiple space separators, trailing spaces, adjacent problems
- **Testing**: Order-independent assertions using set comparison since problem order varies in output

### Day 7: Tachyon Manifold
- Simulated quantum beam splitting through a 2D manifold grid
- Implemented BFS-based beam propagation with splitter tracking
- **Key Insight**: Track unique splitters hit, not total beam-splitter collisions
- **Part 1**: Count unique splitters activated - beams split spatially but continue downward
- **Part 2**: Count quantum timelines using recursive path enumeration with memoization
- **Challenge**: Understanding that multiple beams can hit the same splitter (only count once)
- **Optimization**: Jump directly to next splitter using pre-indexed columns instead of stepping cell-by-cell
- **Algorithm**: Part 1 uses BFS with visited set, Part 2 uses recursive DP with memoization
- **Mathematics**: Not 2^n timelines - only count valid complete paths that reach an exit
- **Technique**: Memoization transforms exponential path counting into polynomial time
- **Design Pattern**: Same position reached via different paths has same exit count (optimal substructure)

### Day 8: Junction Box Circuits
- Connected junction boxes using minimum spanning tree (MST) with Kruskal's algorithm
- Implemented Union-Find (Disjoint Set Union) for efficient connectivity tracking
- **Key Insight**: "Attempts" vs "connections" - skipped edges still count toward attempt limit
- **Part 1**: After N connection attempts, find sizes of three largest circuits (components)
- **Part 2**: Complete the MST (N-1 edges for N nodes), return X-coordinates of final edge
- **Challenge**: Understanding that trying to connect already-connected boxes counts as an attempt
- **Algorithm**: Sort edges by Euclidean distance, greedily add shortest non-cycle-forming edges
- **Data Structure**: Union-Find with path compression (O(α(N)) ≈ O(1)) and union by size
- **Optimization**: Use squared distance instead of actual distance (avoids sqrt, same ordering)
- **Mathematics**: A tree with N nodes requires exactly N-1 edges to be fully connected
- **Technique**: Track successful unions vs attempts - component count = N - successful_unions
- **Graph Theory**: This is a partial MST problem (Part 1) and complete MST problem (Part 2)

### Day 9: Maximum Rectangle in Polygon
- Found largest rectangles within rectilinear polygons using geometric properties
- Implemented point-in-polygon tests with memoization for efficiency
- **Key Insight**: All edges are axis-aligned → rectilinear polygon enables O(1) rectangle validation
- **Part 1**: Find max rectangle using any two red tiles as opposite corners (simple O(n²))
- **Part 2**: Rectangle must contain only red (vertices) or green (boundary/interior) tiles
- **Challenge**: Largest rectangle has 1.47 billion points - can't check them all!
- **Algorithm**: Check 4 corners are inside + no edges cross interior (sufficient for rectilinear polygons)
- **Optimization**: Memoize polygon membership checks - first check O(n), subsequent O(1)
- **Edge Intersection**: Edge crosses only if it has points strictly inside rectangle interior (not just touching)
- **Mathematics**: For rectilinear polygon, corners inside + no edge crossings ⟹ all points inside
- **Technique**: Ray casting for point-in-polygon, interval overlap detection for edge crossings
- **Correctness vs Speed**: Geometric theorem avoids checking billions of points while guaranteeing correctness
- **Final Answer**: Rectangle from (5254, 66490) to (94821, 50072) with area 1,470,616,992

---

## Running the Solutions

```bash
# Run a specific day
python 2025/day_01/solution.py

# Run with custom input
python 2025/day_02/solution.py --input custom_input.txt

# Run all completed days for 2025
python run_all.py --year 2025
```

---

## Personal Goals

- [ ] Complete all 12 days
- [x] Document the mathematical intuition for each problem
- [x] Optimize solutions for performance
- [x] Write comprehensive explanations in READMEs
- [ ] Share learnings with the community

---

## Resources

- [Advent of Code 2025](https://adventofcode.com/2025)
- [Python Documentation](https://docs.python.org/3/)
- [Reddit Discussion](https://www.reddit.com/r/adventofcode/)

---

✨🎄🎁🎄🎅🎄🎁🎄✨

_"The best way to spread Christmas cheer is coding loud for all to hear!"_ 🎅

---

## Notes

- Solutions are optimized for clarity and mathematical elegance
- Each day includes detailed explanations of the approach
- Focus on learning algorithms and problem-solving techniques
- All solutions tested with provided examples before submission
- 2025 edition features 12 days of challenges

---

## Previous Years

- [2024](2024/)
- [2023](2023/)
- [2022](2022/)

---

## License

MIT License - Feel free to use these solutions for learning purposes!

---

**Happy Coding! 🎄✨**