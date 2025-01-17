# --- Day 1: Historian Hysteria ---

The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.

Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants one star. Good luck!

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:

```shell
3   4
4   3
2   5
1   3
3   9
3   3

```
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?

# Solution Explanation

This repository contains a solution for a problem that involves processing numerical data from a file. The solution is implemented in Python and is structured into a class called `Solution`. Below is an explanation of the logic used in both parts of the solution.

## Overview

The solution reads numerical data from a specified input file, which can either be a real input file or a test input file. The data is processed to compute results for two different parts of the problem.

## Part 1

In Part 1, the goal is to calculate the sum of the absolute differences between two sets of numbers. The steps involved are:

1. **Data Reading**: The input file is read, and each line is split into two numbers. These numbers are stored in two separate lists: `self.left` and `self.right`.
2. **Sorting**: Both lists are sorted in ascending order.
3. **Calculation**: The absolute difference between corresponding elements of the two lists is computed using a generator expression. The sum of these absolute differences is returned as the result.

### Example

If the input data is:

```shell
3   4
4   3
2   5
1   3
3   9
3   3
```
The output for Part 1 would be:

```shell
|1-3| + |2-3| + |3-3| + |3-4| + |3-9| + |3-3| + |3-5| + |4-9| = 2 + 1 + 0 + 1 + 2 + 5 = 11
```

## Part 2

In Part 2, the objective is to calculate a weighted sum based on the frequency of numbers in the `self.right` list. The steps are as follows:

1. **Unique Values**: A list of unique values from `self.right` is created.
2. **Frequency Calculation**: A frequency dictionary is constructed, mapping each unique number to its count in the `self.right` list.
3. **Weighted Sum**: The sum is calculated by iterating over the `self.left` list and multiplying each number by its frequency from the frequency dictionary. If a number does not exist in the dictionary, it defaults to zero.

### Example

For the input data:

```shell
3   4
4   3
2   5
1   3
3   9
3   3
```

The output for Part 2 would be:

```shell
(3*3) + (4*1) + (2*0) + (1*0) + (3*3) + (3*3)= 9 + 4 + 0 + 0 + 9 + 9 = 31
```
