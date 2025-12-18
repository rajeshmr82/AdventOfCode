[![AoC](https://badgen.net/badge/AoC/2025/blue)](https://adventofcode.com/2025)
![Language](https://badgen.net/badge/Language/Python/blue)
[![Days Completed](https://badgen.net/badge/Days%20Completed/5/green)]()
[![Stars](https://badgen.net/badge/Stars/10%E2%98%85/yellow)]()

# 🎄 Advent of Code 2025 🎄

## Solutions

<!--SOLUTIONS-->
[![Day](https://badgen.net/badge/01/%E2%98%85%E2%98%85/green)](day_01)
[![Day](https://badgen.net/badge/02/%E2%98%85%E2%98%85/green)](day_02)
[![Day](https://badgen.net/badge/03/%E2%98%85%E2%98%85/green)](day_03)
[![Day](https://badgen.net/badge/04/%E2%98%85%E2%98%85/green)](day_04)
[![Day](https://badgen.net/badge/05/%E2%98%85%E2%98%85/green)](day_05)
[![Day](https://badgen.net/badge/06/%E2%98%86%E2%98%86/grey)](day_06)
[![Day](https://badgen.net/badge/07/%E2%98%86%E2%98%86/grey)](day_07)
[![Day](https://badgen.net/badge/08/%E2%98%86%E2%98%86/grey)](day_08)
[![Day](https://badgen.net/badge/09/%E2%98%86%E2%98%86/grey)](day_09)
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
| 06 | | | |
| 07 | | | |
| 08 | | | |
| 09 | | | |
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
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── README.md
│   ├── day_02/
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── README.md
│   ├── day_03/
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── README.md
│   ├── day_04/
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── README.md
│   └── ...
├── 2024/
│   └── ...
└── utils/
    └── helpers.py
```

---

## Progress Statistics

- **Total Stars**: 10 ⭐
- **Completion Rate**: 42% (5/12 days)
- **Current Streak**: 5 days 🔥
- **Last Updated**: December 18, 2025

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