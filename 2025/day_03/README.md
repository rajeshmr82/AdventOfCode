# Battery Joltage Problem

## Problem Overview

You need to supply emergency power to an escalator using batteries arranged in banks. Each battery is labeled with a joltage rating (a digit from 1-9). Your goal is to maximize the total joltage output across all banks.

---

## Part 1: Two Batteries Per Bank

### Problem Statement

For each bank of batteries (represented as a row of digits), you need to turn on **exactly 2 batteries**. The joltage produced equals the 2-digit number formed by those batteries **in the order they appear**.

**Key Constraint**: You cannot rearrange batteries - the second battery must appear after the first in the sequence.

### Example

```
987654321111111
811111111111119
234234234234278
818181911112111
```

**Bank 1**: `987654321111111`
- Best choice: Pick batteries at positions 0 and 1 → `98` jolts
- Other options: positions 1,2 → `87`, positions 2,3 → `76`, etc.

**Bank 2**: `811111111111119`
- Best choice: Pick `8` (position 0) and `9` (position 14) → `89` jolts

**Bank 3**: `234234234234278`
- Best choice: Pick `7` (position 13) and `8` (position 14) → `78` jolts

**Bank 4**: `818181911112111`
- Best choice: Pick `9` (position 6) and `2` (position 11) → `92` jolts

**Total**: `98 + 89 + 78 + 92 = 357` jolts

### Strategy

**Greedy Algorithm**: For each bank, try all possible pairs (i, j) where j > i, and find the maximum value of `digit[i] * 10 + digit[j]`.

### Algorithm Complexity

- **Time**: O(n²) for each bank, where n is the number of batteries
- **Space**: O(1)

### Pseudocode

```
for each bank:
    max_joltage = 0
    for i from 0 to len(bank) - 1:
        for j from i+1 to len(bank):
            joltage = bank[i] * 10 + bank[j]
            max_joltage = max(max_joltage, joltage)
    total += max_joltage
```

---

## Part 2: Twelve Batteries Per Bank

### Problem Statement

Now you need to turn on **exactly 12 batteries** per bank. The joltage is the 12-digit number formed by those batteries in order.

### Example

Same banks as before:

```
987654321111111  (15 digits)
811111111111119  (15 digits)
234234234234278  (15 digits)
818181911112111  (15 digits)
```

**Bank 1**: `987654321111111`
- Need 12 out of 15 digits → skip 3 digits
- Best: Skip three `1`s at the end → `987654321111`

**Bank 2**: `811111111111119`
- Best: Skip three `1`s → `811111111119`

**Bank 3**: `234234234234278`
- Best: Skip `2`, `3`, `2` near the start → `434234234278`

**Bank 4**: `818181911112111`
- Best: Skip some `1`s near the front → `888911112111`

**Total**: `987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619`

### Strategy

**Greedy Left-to-Right Construction**:
1. Build the result digit by digit from left to right
2. For each position, pick the **largest available digit** 
3. **Crucial constraint**: Ensure you leave enough digits for the remaining positions

### Key Insight

If you need to pick k digits from n total digits, when selecting the digit for position `i`:
- You've already picked `i` digits
- You still need `k - i - 1` more digits
- You can search up to index `n - (k - i - 1)` 
- This ensures you leave enough digits for future positions

### Visual Example

Bank: `234234234234278` (15 digits, need 12)

```
Index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Digit:  2 3 4 2 3 4 2 3 4 2  3  4  2  7  8
```

**Position 0** (need 12 more):
- Can search indices 0-3 (must leave 11 digits)
- Largest in range [0,3]: `4` at index 2 ✓
- Result so far: `4`

**Position 1** (need 11 more):
- Start from index 3, can search up to index 4 (must leave 10 digits)
- Largest in range [3,4]: `4` at index 5 ✓
- Result so far: `43`

**Position 2** (need 10 more):
- Start from index 6, can search up to index 5 (must leave 9 digits)
- Continue this process...

Final result: `434234234278`

### Algorithm Complexity

- **Time**: O(n * k) for each bank, where n is total digits and k is digits to pick
- **Space**: O(k) to store result

### Pseudocode

```
for each bank:
    result = []
    start_index = 0
    
    for position from 0 to k-1:
        remaining_needed = k - position - 1
        max_search_index = len(bank) - remaining_needed
        
        # Find largest digit in valid range
        largest = max(bank[start_index : max_search_index])
        largest_index = index of largest (starting from start_index)
        
        result.append(largest)
        start_index = largest_index + 1
    
    convert result to number and add to total
```


## Key Takeaways

1. **Part 1** is a straightforward brute-force problem - try all pairs
2. **Part 2** requires a greedy algorithm with careful constraint management
3. Both parts share the same core concept: picking digits to form the largest number
4. Part 2 generalizes Part 1 (Part 1 is just `k=2`)
5. The "leave enough digits" constraint is crucial for Part 2's correctness

---

