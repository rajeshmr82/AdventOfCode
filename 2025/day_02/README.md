# Invalid ID Detection - Mathematical Approach

## Problem Overview

We need to identify "invalid IDs" within given numeric ranges. Invalid IDs are numbers formed by repeating a pattern of digits multiple times.

---

## Part 1: Exactly Two Repetitions

### Problem Definition

An invalid ID is a number where **some sequence of digits is repeated exactly twice**.

**Examples:**
- `11` = "1" repeated 2 times ✓
- `6464` = "64" repeated 2 times ✓
- `123123` = "123" repeated 2 times ✓
- `1234` = Not a repeated pattern ✗

### Mathematical Intuition

When a pattern is repeated exactly twice, there's a mathematical relationship:

For a pattern `p` with `k` digits:
```
doubled_number = p followed by p
               = p × 10^k + p
               = p × (10^k + 1)
```

**Why?**
- Multiplying by `10^k` shifts the pattern left by `k` positions
- Adding `p` again places it in the remaining positions

**Examples:**
```
Pattern: 64 (k=2 digits)
Shifted: 64 × 10^2 = 6400
Add:                +   64
Result:             6464
Formula: 64 × (100 + 1) = 64 × 101 = 6464

Pattern: 123 (k=3 digits)
Shifted: 123 × 10^3 = 123000
Add:                  +  123
Result:               123123
Formula: 123 × (1000 + 1) = 123 × 1001 = 123123
```

### The Multiplier Table

| Pattern Length (k) | Multiplier (10^k + 1) | Example |
|--------------------|-----------------------|---------|
| 1                  | 11                    | 5 → 55  |
| 2                  | 101                   | 64 → 6464 |
| 3                  | 1001                  | 123 → 123123 |
| 4                  | 10001                 | 2025 → 20252025 |

### Detection Algorithm (Part 1)

**Brute Force:**
```python
def is_invalid_id_part1(n):
    s = str(n)
    length = len(s)
    
    # Must have even length
    if length % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = length // 2
    return s[:mid] == s[mid:]
```

**Mathematical Approach:**
```python
def sum_invalid_ids_part1(start, end):
    total = 0
    k = 1  # Pattern length
    
    while True:
        multiplier = 10 ** k + 1
        min_doubled = (10 ** (k - 1)) * multiplier
        
        # Stop if smallest possible doubled number exceeds range
        if min_doubled > end:
            break
        
        # Valid k-digit patterns (no leading zeros)
        min_pattern = 10 ** (k - 1)
        max_pattern = 10 ** k - 1
        
        # Find patterns that produce numbers in [start, end]
        first_pattern = max(min_pattern, (start + multiplier - 1) // multiplier)
        last_pattern = min(max_pattern, end // multiplier)
        
        if first_pattern <= last_pattern:
            # Use arithmetic series sum
            count = last_pattern - first_pattern + 1
            sum_of_patterns = count * (first_pattern + last_pattern) // 2
            total += sum_of_patterns * multiplier
        
        k += 1
    
    return total
```

### Why This Works

Instead of checking every number in the range:
1. We iterate through possible **pattern lengths** (k)
2. For each length, calculate the **multiplier** = 10^k + 1
3. Find which **patterns** produce valid doubled numbers in our range
4. Sum them using the **arithmetic series formula**

**Time Complexity:**
- Brute force: O(end - start)
- Mathematical: O(log(end)) - only iterate through pattern lengths

---

## Part 2: Two or More Repetitions

### Problem Definition

An invalid ID is a number where **some sequence of digits is repeated 2 or more times**.

**Examples:**
- `12341234` = "1234" repeated 2 times ✓
- `123123123` = "123" repeated 3 times ✓
- `1212121212` = "12" repeated 5 times ✓
- `1111111` = "1" repeated 7 times ✓

### Mathematical Intuition

For a pattern `p` of length `k` repeated `n` times:

```
repeated_number = p + p×10^k + p×10^(2k) + ... + p×10^((n-1)k)
                = p × (1 + 10^k + 10^(2k) + ... + 10^((n-1)k))
```

This is a **geometric series** with:
- First term: 1
- Common ratio: 10^k
- Number of terms: n

**Geometric Series Formula:**
```
Sum = (r^n - 1) / (r - 1)

where r = 10^k, so:

Sum = (10^(nk) - 1) / (10^k - 1)
```

Therefore:
```
repeated_number = p × (10^(nk) - 1) / (10^k - 1)
```

### Examples with Geometric Series

**Pattern: 12 (k=2), repeated 5 times (n=5)**
```
1212121212 = 12 × (1 + 100 + 10000 + 1000000 + 100000000)
           = 12 × (10^10 - 1) / (10^2 - 1)
           = 12 × 9999999999 / 99
           = 12 × 101010101
```

**Pattern: 123 (k=3), repeated 3 times (n=3)**
```
123123123 = 123 × (1 + 1000 + 1000000)
          = 123 × (10^9 - 1) / (10^3 - 1)
          = 123 × 999999999 / 999
          = 123 × 1001001
```

### Multiplier Table (Extended)

| k | n | Multiplier Formula | Example | Result |
|---|---|--------------------|---------|--------|
| 1 | 2 | (10^2 - 1) / 9 = 11 | 5 | 55 |
| 1 | 3 | (10^3 - 1) / 9 = 111 | 5 | 555 |
| 2 | 2 | (10^4 - 1) / 99 = 101 | 12 | 1212 |
| 2 | 3 | (10^6 - 1) / 99 = 10101 | 12 | 121212 |
| 3 | 2 | (10^6 - 1) / 999 = 1001 | 123 | 123123 |

### Detection Algorithm (Part 2)

**Brute Force:**
```python
def is_invalid_id_part2(n):
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths
    for k in range(1, length):
        # Check if length is divisible by k
        if length % k == 0:
            num_repetitions = length // k
            
            # Need at least 2 repetitions
            if num_repetitions >= 2:
                pattern = s[:k]
                
                # Check if entire string is this pattern repeated
                if pattern * num_repetitions == s:
                    return True
    
    return False
```

### The Deduplication Challenge

A critical issue: **some numbers match multiple patterns!**

**Example: 111111**
- Pattern "1" repeated 6 times ✓
- Pattern "11" repeated 3 times ✓
- Pattern "111" repeated 2 times ✓

All three are valid interpretations, but we should only count `111111` **once** in our sum.

### Mathematical Approach with Deduplication

```python
def sum_invalid_ids_part2(start, end):
    invalid_ids = set()  # Use set to automatically deduplicate
    
    # Try all pattern lengths
    for k in range(1, len(str(end)) + 1):
        min_pattern = 10 ** (k - 1)  # Smallest k-digit number
        max_pattern = 10 ** k - 1     # Largest k-digit number
        
        # Try all repetition counts (at least 2)
        n = 2
        while True:
            # Calculate multiplier using geometric series
            multiplier = (10 ** (n * k) - 1) // (10 ** k - 1)
            
            # Stop if smallest possible number exceeds range
            if min_pattern * multiplier > end:
                break
            
            # Find patterns whose repeated values fall in [start, end]
            first_pattern = max(min_pattern, (start + multiplier - 1) // multiplier)
            last_pattern = min(max_pattern, end // multiplier)
            
            if first_pattern <= last_pattern:
                # Add each invalid ID to set (duplicates ignored)
                for pattern in range(first_pattern, last_pattern + 1):
                    repeated_num = pattern * multiplier
                    if start <= repeated_num <= end:
                        invalid_ids.add(repeated_num)
            
            n += 1
    
    return sum(invalid_ids)
```

### Why Deduplication Matters

**Range [11, 22] in Part 2:**

Without deduplication:
- Pattern "1" × 2 → 11 ✓
- Pattern "11" × 1 → 11 (not valid, needs ≥2 reps)
- Pattern "2" × 2 → 22 ✓
- Pattern "22" × 1 → 22 (not valid)

Only 11 and 22 are found, no duplicates in this case.

**Range [1, 1111]:**

Without deduplication (potential issues):
- Pattern "1" × 2 → 11
- Pattern "1" × 3 → 111
- Pattern "1" × 4 → 1111
- Pattern "11" × 2 → 1111 (duplicate!)

With set: `{11, 111, 1111}` - each counted once!

---

## Complete Implementation

### Part 1: Exactly 2 Repetitions

```python
def sum_invalid_ids_part1(start, end):
    """Sum all numbers formed by repeating a pattern exactly twice."""
    total = 0
    k = 1
    
    while True:
        multiplier = 10 ** k + 1
        min_doubled = (10 ** (k - 1)) * multiplier
        
        if min_doubled > end:
            break
        
        min_pattern = 10 ** (k - 1)
        max_pattern = 10 ** k - 1
        
        first_pattern = max(min_pattern, (start + multiplier - 1) // multiplier)
        last_pattern = min(max_pattern, end // multiplier)
        
        if first_pattern <= last_pattern:
            count = last_pattern - first_pattern + 1
            sum_of_patterns = count * (first_pattern + last_pattern) // 2
            total += sum_of_patterns * multiplier
        
        k += 1
    
    return total
```

### Part 2: Two or More Repetitions (Deduplicated)

```python
def sum_invalid_ids_part2(start, end):
    """Sum all numbers formed by repeating a pattern 2+ times."""
    invalid_ids = set()
    
    for k in range(1, len(str(end)) + 1):
        min_pattern = 10 ** (k - 1)
        max_pattern = 10 ** k - 1
        
        n = 2
        while True:
            multiplier = (10 ** (n * k) - 1) // (10 ** k - 1)
            
            if min_pattern * multiplier > end:
                break
            
            first_pattern = max(min_pattern, (start + multiplier - 1) // multiplier)
            last_pattern = min(max_pattern, end // multiplier)
            
            if first_pattern <= last_pattern:
                for pattern in range(first_pattern, last_pattern + 1):
                    repeated_num = pattern * multiplier
                    if start <= repeated_num <= end:
                        invalid_ids.add(repeated_num)
            
            n += 1
    
    return sum(invalid_ids)
```

### Processing Multiple Ranges

```python
ranges = [
    (11, 22), (95, 115), (998, 1012), 
    (1188511880, 1188511890), (222220, 222224),
    (1698522, 1698528), (446443, 446449), 
    (38593856, 38593862), (565653, 565659),
    (824824821, 824824827), (2121212118, 2121212124)
]

# Part 1
total_part1 = sum(sum_invalid_ids_part1(start, end) for start, end in ranges)
print(f"Part 1 Total: {total_part1}")

# Part 2
total_part2 = sum(sum_invalid_ids_part2(start, end) for start, end in ranges)
print(f"Part 2 Total: {total_part2}")
```

---

## Key Takeaways

### Part 1 Formula
```
doubled_number = pattern × (10^k + 1)
where k = length of pattern
```

### Part 2 Formula
```
repeated_number = pattern × (10^(n×k) - 1) / (10^k - 1)
where:
  k = length of pattern
  n = number of repetitions (≥2)
```

### Optimization Strategies

1. **Iterate over pattern lengths**, not individual numbers
2. **Use arithmetic series** to sum ranges of patterns
3. **Calculate multipliers** using geometric series
4. **Use sets** to handle deduplication automatically
5. **Break early** when patterns become too large

### Time Complexity

- **Brute Force**: O((end - start) × log(end))
- **Mathematical**: O(log²(end)) for Part 1, O(log³(end)) for Part 2 with deduplication

The mathematical approach is significantly faster for large ranges!
